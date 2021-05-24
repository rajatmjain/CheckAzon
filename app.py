import requests
from bs4 import BeautifulSoup
import smtplib
import time


class Scraper:
    def __init__(self,url,maxValue,email):
        self.url = url
        self.maxValue = maxValue
        self.userEmail = email


    def getPrice(self):
        agent = {
            "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Safari/605.1.15'}
        page = requests.get(url=self.url, headers=agent)
        soup = BeautifulSoup(page.content, 'html.parser')
        title = soup.find(id="productTitle").get_text().strip()
        price = soup.find(id="priceblock_ourprice").get_text().strip()
        converted_price = float(price.replace(",", "").replace("₹", ""))
        print(title, price, converted_price)
        if converted_price<=self.maxValue:
            self.sendMail(title,converted_price)
        else:
            print("We will inform you when your desired value is reached.")

    def sendMail(self,productName,productPrice):
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login("<YOUR-GMAIL-ID>","<YOUR-GMAIL-PASSWORD>")
        subject = "The price of "+ productName +" fell down!"
        body = "The price for "+productName+" is "+str(productPrice)+". Hurry up and make your purchase!"+"\nLink: "+self.url
        message = """\Subject: {}\n\n{}""".format(subject,body)
        server.sendmail("<YOUR-GMAIL-ID>",self.userEmail,message)
        print("Email sent")
        server.quit()



scr1 = Scraper(input("Enter the URL of the Amazon product's page: "),float(input("Enter ther maximum value to trigger an email: ")),input("Please enter your email ID to receive a notification: "))
while(True):
    scr1.getPrice()
    time.sleep(60*60)