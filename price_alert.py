import requests
from bs4 import BeautifulSoup
import smtplib
from dotenv import load_dotenv
import os




# ========== CONFIGURATION ==========

#URL = "https://appbrewery.github.io/instant_pot/"
URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

TARGET_PRICE = 100.00

load_dotenv()  # load variables from .env into environment
MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")
TO_EMAIL = os.getenv("TO_EMAIL")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

# ===================================

"""
# Full headers would look something like this
header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
    "Dnt": "1",
    "Priority": "u=1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
}

# A minimal header would look like this:
# header = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
#     "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
# }
"""


if __name__=="__main__":

    data = requests.get(URL, headers=headers)
    soup = BeautifulSoup(data.content, "html.parser")
    print(soup.prettify())

    """
    price_whole = soup.find("span",class_="a-price-whole")
    price_fraction = soup.find("span",class_="a-price-fraction")
    str_of_price = price_whole.getText()  + price_fraction.getText()
    #price = float(str_of_price)
    #print(" price: " ,price)
    #print(type(price))
    """

    # Find the HTML element that contains the price
    price = soup.find(class_="a-offscreen").get_text()

    # Remove the dollar sign using split
    price_without_currency = price.split("$")[1]

    # Convert to floating point number
    price_as_float = float(price_without_currency)
    print(price_as_float)

    title = soup.find("span", id="productTitle").getText().strip()

    # ----- Check and Send Email -----
    if price_as_float < TARGET_PRICE:

        subject = "Subject:Amazon Price Alert!"
        body = f"""\
        The price has dropped!

        Product: {title}
        Current Price: ${price_as_float}
        Buy now: {URL}
        """
        # Combine subject and body into a properly formatted message
        message = f"Subject: {subject}\n\n{body}"

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=TO_EMAIL,
                msg=message.encode("utf-8")
            )
        print("Email sent!")
    else:
        print("Price is still too high:", price)