# -*- coding: utf-8 -*-
import os
import requests
import streamlit as st

ACTIAPI = os. getenv('ZH_ACTIAPI')

URL_ACTI= f"http://apidata.acti.pl/toc?token={ACTIAPI}"
URL_PRODUCTS = "http://apidata.acti.pl/products/"
URL_PRODUCT = "http://apidata.acti.pl/product/"

def run():
    count = 0
    st.header('Simple API viewer')

    iteration = st.text_input("(Produkty) Do ilu liczyć? ")
    if st.button("Submit"):
        pass
    if iteration.isdigit():
        count = int(iteration)
        if count >30:
            st.write("Za dużo, powiedzmy, że max to 30")
            count = 0
    else:
        count = 0
    for i in range(1 , count+1):
        request = requests.get(URL_PRODUCTS+str(i))
        content = request.json()
        # print(list(content)[0])
        if list(content)[0] == "message":
            st.write(f"{i} nie istnieje ")
        else:
            count = 0
            cols = st.columns(4)
            cols[count].write(f"{i} OK")
            count += 1
            for key, value in content.items():
                cols[count].write(f'np.  {value["name"]}')
                count += 1
                if count >= 3:
                    break

def clear_screen(row):
    for i in range(1, row + 1):
        st.write("")