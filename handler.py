# -*- coding: utf-8 -*-
# @Author: JsPako
# @Webpage: https://github.com/JsPako/AmazonWatch

from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
productPrices = []


def handler():
    with open("list.txt", "r") as f:
        file = f.readlines()
        for line in file:
            lines = line.split("'")
            data = lines[1].split(",")
            productPrices.append(scrape(data[1]))
        f.close()
    updateFile()


def scrape(url):
    resp = requests.get(url, headers=headers)
    s = BeautifulSoup(resp.content, features="lxml")
    productPrice = s.select('#priceblock_ourprice')[0].get_text().strip()
    return(productPrice)


def updateFile():
    priceData = []
    with open("list.txt", "r") as f:
        file = f.readlines()
        i = 0
        f.close()
        for line in file:
            lines = line.split("'")
            data = lines[1].split(",")
            if i < len(productPrices):
                data[2] = productPrices[i]
                priceData.append(
                    "'" + data[0] + "," + data[1] + "," + data[2] + "," + data[3] + "'\n")
            i = i + 1
        f.close()
    open("list.txt", "w").close()
    with open("list.txt", "a") as f:
        f.writelines(priceData)
