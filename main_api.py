# -*- coding: utf-8 -*-
import os
import requests
import streamlit as st

ACTIAPI = os. getenv('ZH_ACTIAPI')

URL_ACTI= f"http://apidata.acti.pl/toc?token={ACTIAPI}"
URL_PRODUCTS = "http://apidata.acti.pl/products/"
URL_PRODUCT = "http://apidata.acti.pl/product/"

def run():
    st.header('Simple API viewer')


    request = requests.get(URL_PRODUCTS+'1')
    content = request.json()
    print(list(content)[2])
    # content = request.text


