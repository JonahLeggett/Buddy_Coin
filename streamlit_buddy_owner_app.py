#Import required libraries
import os
import json
from typing import Container
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st

#Load in the .env file
load_dotenv()

#Defining and connecting the Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

#Create a function to load the contract into the pp
@st.cache(allow_output_mutation=True)
def load_contract():
    with open(Path('./artifacts/BuddyTokenCrowdsale.json')) as f:
        buddy_abi = json.load(f)
    
    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

    contract = w3.eth.contract(
        address = contract_address, 
        abi = buddy_abi
    )

    return contract

#Setting a variable 'contract' to the smart contract loaded in with Web3
contract = load_contract()



st.title('Welcome to the Purchasing App')

st.header('What would you like to do today?')
st.button('Purchase Product')
st.button('Purchase Buddy Tokens')
st.button('Return/Exchanges')



st.header('Purchase Order')
st.write('Please input your purchase in the sections below:')
st.text_input('Customer Name')
st.text_input('Product Type')
st.text_input('Unit Amount (Weight)')
st.text_input('Customer Name')
st.text_input('Customer Name')


#Deploy smart contract to sell product in exchange for BUD Tokens
#Allow entry for information such as:
#Customer Name
#Product Type
#Product Description
#Unit Amount (weight/size)
#USD price
#BUD Token price
#Timestamp
#Allow option to return ETHER to customer address in event of return/exchange
#View customer account balances
#Transfer 
#Mint new Tokens
#View Balance of owner’s ETHER wallet

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
