import streamlit as st
import requests

URL = "https://www.homedepot.ca/product/frigidaire-gallery-30-inch-5-4-cu-ft-front-control-slide-in-electric-range-with-air-fry-in-stainless-steel/1001318565"

page = requests.get(URL)

html = page.content

start_index = html.index('<span class="price">')
end_index = html.index('</span>', start_index)

price = html[start_index:end_index].split('>')[-1]

st.title("Frigidaire Range Price")
st.write("The price of the Frigidaire range is: $" + price)
