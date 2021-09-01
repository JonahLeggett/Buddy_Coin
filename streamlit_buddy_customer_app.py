#Importing required libraries
import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st
​
#Load in the .env file
load_dotenv()
 
#Defining and connecting the Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))
 
#Create a function to load the contract into the app
@st.cache(allow_output_mutation=True)
def load_contract():
    with open(Path(r'Buddy_Token\BuddyToken2_abi.json')) as f:
        buddy_abi = json.load(f)

    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

    contract = w3.eth.contract(
        address=contract_address,
        abi= buddy_abi
    )
    return contract

#Setting a variable 'contract' to the smart contract loaded in with Web3
token = load_contract()

#Set up accounts via Web3 connection
st.image(r'C:\Users\miggs\Desktop\FinTech-Workspace\cannabis_industry\Buddy_Token\resources\BUDlogo2.png')
st.title('BUDDY COIN EXCHANGE')
accounts = w3.eth.accounts
address = st.selectbox('Select Ethereum Account', options = accounts)

#This section is the intro to the customer app for Buddy Token
st.title('Welcome to the Purchasing App')

st.header('What would you like to do today?')

#Ideally, we would want the following 3 buttons to navigate to a different page for the app
#st.button('Purchase Product')
#st.button('Purchase Buddy Tokens')
#st.button('Return/Exchanges')
 
#Creating the purchase order button for Streamlit app
st.header('Buddy Token Purchase Order')
token_quantity = st.slider('Select how many Buddy Tokens you want to purchase (whole number increments only):', 
                            min_value = 1, max_value = 999999999999999999999999999999999999)
st.write(token_quantity)
st.button('Purchase Buddy Tokens')
if st.button('Purchase Buddy Tokens'):
    tx_hash = token.functions.purchase(token_quantity).call()

st.header('Product Purchase Order')
st.write('Please select your purchase options below:')
st.text_input('Customer Name')
st.selectbox('Product Type', ['Cannabis', 'Accessories'])

product_amount = st.selectbox('Select Product Amount', ['1/8 oz', '1/4 oz', '1/2 oz', '1 oz'])

quantity = st.number_input('Quantity')

total_cost = st.button("Calculate Total Cost")
if total_cost:
    st.write(total_cost)

confirm_purchase = st.button('Confirm Purchase')
if confirm_purchase:
    #Put in order for the product
    st.write("Purchase confirmed.")

st.header('Product Sales Statistics')
st.button('Total Sales in USD')
st.button('Total Sales for 1/8 oz')
st.button('Total Sales for 1/4 oz')
st.button('Total Sales for 1/2 oz')
st.button('Total Sales for 1 oz')

