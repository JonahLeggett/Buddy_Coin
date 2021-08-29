import os
import json
from typing import Container
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

@st.cache(allow_output_mutation=True)
def load_contract():
    with open(Path('./contracts/compiled/buddy_abi.json')) as f:
        buddy_abi = json.load(f)
    
    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

    contract = w3.eth.contract(
        address = contract_address, 
        abi = buddy_abi
    )

    return contract



st.title('Buddy Crowdsale')

st.header('Product Pricing')
st.write('1/8 oz = ')
st.write('1/4 oz = ')
st.write('1/2 oz = ')
st.write('1 oz = ')

st.header('Product Sales Statistics')
st.button('Total Sales in USD')
st.button('Total Sales for 1/8 oz')
st.button('Total Sales for 1/4 oz')
st.button('Total Sales for 1/2 oz')
st.button('Total Sales for 1 oz')



st.text_input('Customer Name')
st.text_input('Product Type')
st.text_input('Product Description')
st.number_input('Unit Amount (in ounce partitions)')
st.number_input('USD Price')
st.number_input('BUD Token Price')
