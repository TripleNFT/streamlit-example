import subprocess
import streamlit as st
import requests
from bs4 import BeautifulSoup

def install_dependencies(package_file):
    with open(package_file, "r") as f:
        packages = f.readlines()
        for package in packages:
            package = package.strip()
            subprocess.run(["pip", "install", package])

install_dependencies("Packages.txt")

def get_price():
    URL = "https://www.homedepot.ca/product/frigidaire-gallery-30-inch-5-4-cu-ft-front-control-slide-in-electric-range-with-air-fry-in-stainless-steel/1001318565"

    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    price = soup.find('span', class_='price').get_text()

    return price

st.title("Frigidaire Range Price")
st.write("The price of the Frigidaire range is: $" + get_price())
