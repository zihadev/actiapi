# -*- coding: utf-8 -*-
import os
import requests
import streamlit as st

ACTIAPI = os.getenv('ZH_ACTIAPI')

URL_ACTI = f"http://apidata.acti.pl/toc?token={ACTIAPI}"
URL_PRODUCTS = "http://apidata.acti.pl/products/"
URL_PRODUCT = "http://apidata.acti.pl/product/"


def run():
    if 'count' not in st.session_state:
        st.session_state['count'] = ''
        # count = 0

    st.header('API')
    st.subheader('Co jest w Produkty i co w Produkt')
    options = ['Wybierz opcję', 'Produkty', 'Produkt']
    selected_option = st.selectbox('Wybierz opcję:', options)
    if selected_option != 'Wybierz opcję':

        match selected_option:
            case 'Produkty':
                products()
            case 'Produkt':
                product()
            case _:
                st.write('Wybierz opcję')


def clear_screen(row):
    for i in range(1, row + 1):
        st.write("")
    st.session_state['count'] = ''


def products():
    count = interation_question(name="Products")
    for i in range(1, count + 1):
        request = requests.get(URL_PRODUCTS + str(i))
        content = request.json()
        # print("długie na: ", len(list(content)))
        if list(content)[0] == "message":
            st.write(f"{i} nie istnieje ")
        else:
            count = 0
            cols = st.columns(4)
            cols[count].write(f"{i} OK")
            count += 1
            for key, value in content.items():
                name = value.get("name", "No name available")
                cols[count].write(f'np.  {name}')
                count += 1
                if count >= 3:
                    cols[count].write(f'elementów:  {len(list(content))}')
                    break


def product():
    count = interation_question(name="Product")
    for i in range(1, count + 1):
        request = requests.get(URL_PRODUCT + str(i))
        content = request.json()
        # print("długie na: ", len(content))
        if list(content)[0] == "message":
            st.write(f"{i} nie istnieje ")
        else:
            count = 0
            cols = st.columns(4)
            cols[count].write(f"{i} OK")
            count += 1
            name = content.get("name", "No name available")
            cols[count].write(f'To:  {name}')
            count += 1
            if count >= 3:
                break


def interation_question(name=None):
    iteration = st.text_input(f"({name}) Do ilu liczyć?", key="count",
                              placeholder="Wpisz tu liczbę. Ostrożnie, nie za dużo, zacznij od 10-20")
    if st.button("Submit"):
        pass
    if iteration.isdigit():
        count = int(iteration)
    else:
        count = 0
    return count
