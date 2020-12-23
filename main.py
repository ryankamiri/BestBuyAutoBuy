from time import sleep
import random
import keyboard
import pyautogui
import requests
from bs4 import BeautifulSoup

canbuy = False #False
url = "https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442"
rep = input(str("Please input product url: "))
ut = input(str("Please input ut cookie: "))
bm_sz = input(str("Please input bm_sz cookie: "))

if rep != "":
    url = rep
skuid = url.split("?skuId=")[1]

while (not canbuy):
    fheaders = {
        "accept": "application/json",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "content-length": "31",
        "content-type": "application/json; charset=UTF-8",
        "origin": "https://www.bestbuy.com",
        "referer": url,
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
    }
    r = requests.get(url=url, headers=fheaders)
    soup = BeautifulSoup(r.text, 'html.parser')
    button = soup.findAll("button", {"class": "btn btn-disabled btn-lg btn-block add-to-cart-button"})
    if button == []:
        canbuy = True
        break
    sleep(3)
    print("Product not available yet.")
print("Product is available!")

headers = {
    "accept": "application/json",
    "content-type": "application/json; charset=UTF-8",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
}

cookies = {
    "ut": ut,
    "bm_sz": bm_sz
}

payload = {
    "items": [
        {
            "skuId":skuid
        }
    ]
}

r = requests.post("https://www.bestbuy.com/cart/api/v1/addToCart", headers=headers, json=payload, cookies=cookies, timeout=15)

if r.status_code == 200:
    print("Added Item to Cart")
    pyautogui.click(200, 50)
    keyboard.write("https://www.bestbuy.com/checkout/c/r/fast-track")
    keyboard.press_and_release('enter')
    print("Checking out product!")
    sleep(5)
    pyautogui.click(200, 50)
    #keyboard.write("javascript:{document.querySelector('.btn.btn-lg.btn-block.btn-primary.button__fast-track').click();}") #uncomment this on release
    keyboard.press_and_release('enter')
    print("Bought Item!")
    print("Finished executing.")

    #Made by RedBall
else:
    print(f"ERRER BUY IT YOURSELF!!!! {r.status_code} {r.text}")