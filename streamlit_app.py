import streamlit as st
import requests
from bs4 import BeautifulSoup

def get_price():
    URL = "https://www.homedepot.ca/product/frigidaire-gallery-30-inch-5-4-cu-ft-front-control-slide-in-electric-range-with-air-fry-in-stainless-steel/1001318565"

    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    price = soup.find('span', class_='price').get_text()

    return price

st.write("The price of the Frigidaire range is: $" + get_price())
