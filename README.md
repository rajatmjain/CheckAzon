CheckAzon
---------

This is a Python program that allows you to scrape the price of a product from an Amazon product page and receive an email notification when the price drops below a certain value.

Installation

To run this program, you will need Python 3.x and the following libraries:

requests
bs4
smtplib
You can install these libraries by running:

```
pip install requests bs4 smtplib
```
Usage
------

1. Run the program by running the following command in your terminal:
```
python scraper.py
```
2. Enter the URL of the Amazon product's page when prompted.
3. Enter the maximum value for the product when prompted. The program will send you an email notification if the price drops below this value.
4. Enter your email ID when prompted. You will receive an email notification when the price drops below your desired value.
5. The program will scrape the price of the product from the Amazon product page and check if the price is below your desired value. If it is, the program will send you an email notification.
6. The program will continue to scrape the price of the product every hour and check if the price has dropped below your desired value. If it has, the program will send you an email notification.
