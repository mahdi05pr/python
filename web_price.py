"to this project we are recive price about gold, dollar,coin"
from datetime import datetime
import csv
import os
from bs4 import BeautifulSoup
import requests


class Webprice:
    """
    This class should fetch data from a website
    """

    def __init__(self, url="https://www.tgju.org/"):
        self.url = url

    def addrees_web(self):
        "this method want to request to web and recive information about web"
        try:
            request_web = requests.get(self.url, timeout=10)
            result_web = request_web.text
            beauty = BeautifulSoup(result_web, "html.parser")
            return beauty
        except requests.exceptions.ConnectionError:
            return "we cant connect to the server"

    def dollar(self):
        "This method retrieves the price of the dollar"
        beauty = self.addrees_web()
        find_price = beauty.find("td", class_="nf").get_text(strip=True)
        dollar_price = find_price[:9]
        return dollar_price

    def gold(self):
        "This method retrieves the price of the gold"
        beauty = self.addrees_web()
        gold_row = beauty.find("tr", {"data-market-row": "geram18"})
        gold_price = gold_row.find("td", class_="nf").get_text(strip=True)
        return gold_price

    def coin(self):
        "This method retrieves the price of the coin"
        beauty = self.addrees_web()
        coin_row = beauty.find("tr", {"data-market-row": "sekee"})
        coin_price = coin_row.find("td", class_="nf").get_text(strip=True)
        return coin_price

    def date_time(self):
        "This method retrieves the price of the date and time"
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        date = now.date()
        result = f"today is {date} at {time}"
        return result


class Useweb:
    """
    this class executes the request
    """

    def __init__(self):
        self.webprice = Webprice()

    def show_time(self):
        "this methode show date and time"
        return self.webprice.date_time()

    def show_gold(self):
        "this mothode show gold price"
        return self.webprice.gold()

    def show_dollar(self):
        "this methode show dollar price"
        return self.webprice.dollar()

    def show_coin(self):
        "this methode show coin price"
        return self.webprice.coin()

    def save_csv(self, file_csv="web_price_csv.csv"):
        "this methode save all price to (price_csv1)"
        try:
            data = {
                "datetime": self.show_time(),
                "cost_dollar": self.show_dollar(),
                "cost_gold": self.show_gold(),
                "cost_cion": self.show_coin(),
            }
            keys = list(data.keys())
            values = list(data.values())
            if not os.path.exists(file_csv):
                with open(
                    file_csv, mode="w", newline="", encoding="utf-8"
                ) as file:
                    writer_file = csv.writer(file)
                    writer_file.writerow(keys)

            with open(file_csv, mode="a", newline="", encoding="utf-8") as file:
                writer_file = csv.writer(file)
                writer_file.writerow(values)

        except FileNotFoundError:
            print("error")

    def show_mycsv(self, file_csv="web_price_csv.csv"):
        "this methode show (price_csv)file"
        try:
            with open(file_csv, mode="r", newline="", encoding="utf-8") as file:
                reader_file = csv.reader(file)
                for row in reader_file:
                    print(row)
        except FileNotFoundError:
            print("i cant found file")
