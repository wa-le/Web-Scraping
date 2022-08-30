from bs4 import BeautifulSoup
import lxml
import requests
import smtplib
import os
from email.message import EmailMessage
import ssl

url = "https://www.amazon.com/CUCKOO-CRP-HS0657FW-Uncooked-Induction-Stainless/dp/B071H1FXFC/ref=sr_1_15?keywords=rice+cooker&qid=1661776478&sr=8-15"

headers = {
  "Accept-Language": "en,tr-TR;q=0.9,tr;q=0.8,en-US;q=0.7",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
  "Chrome/104.0.0.0 Safari/537.36"
}

buy_price = 280

# request url
response = requests.get(url, headers=headers)
print(response.status_code)

# get soup of url
soup = BeautifulSoup(response.content, "lxml")

# get price and name of product
price = soup.find("span", class_="a-offscreen")
the_price = float(price.string.split("$")[1])
#print(the_price)
prod_name = soup.find("span", id="productTitle")
product_name = prod_name.string.split("|")[0].strip(" ")
#print(product_name)


sender_email = "mainstopstore@gmail.com"
sender_pass = os.environs.get("MAINSTOPSTORE_PASS")
receive_email = "rajahquan@gmail.com"

the_price = 277
if the_price <= buy_price:
  subject = "Price Drop Alert"
  body = f"""
  {product_name} is now ${the_price}
  """
  em = EmailMessage()
  em['From'] = sender_email
  em['To'] = receive_email
  em['Subject'] = subject
  em.set_content(body)

  context = ssl.create_default_context()

  with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=context) as new_connect:
    new_connect.login(sender_email, sender_pass)
    new_connect.sendmail(sender_email, receive_email, em.as_string())
  
  