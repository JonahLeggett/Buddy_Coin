#Importing required libraries
import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st

#Load in the .env file
load_dotenv()
 
#Defining and connecting the Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))
 
#Create a function to load the contract into the app
@st.cache(allow_output_mutation=True)
def load_contract():
    with open(Path(r'BuddyToken2_abi.json')) as f:
        buddy_abi = json.load(f)

    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

    contract = w3.eth.contract(
        address=contract_address,
        abi= buddy_abi
    )
    return contract

#Setting a variable 'contract' to the smart contract loaded in with Web3
token = load_contract()

#Create a function to load the oracle contract into the app
@st.cache(allow_output_mutation=True)
def load_oracle_contract():
    with open(Path(r'Oracle_abi.json')) as f:
        oracle_abi = json.load(f)

    contract_address = os.getenv("ORACLE_ADDRESS")

    contract = w3.eth.contract(
        address=contract_address,
        abi= oracle_abi
    )
    return contract

#Setting a variable 'contract' to the smart contract loaded in with Web3
oracle_contract = load_oracle_contract()

#Create welcome section for the app
st.image(r'resources\BUDlogo2.png')
st.title('Welcome to the Buddy Token Customer App!')

#Display value of Ethereum on sidebar widget
#eth_price = oracle_contract.functions.getLatestPrice().call()
#st.sidebar.write(eth_price)

#Set up accounts via Web3 connection
accounts = w3.eth.accounts
address = st.sidebar.selectbox('Select Ethereum Account', options = accounts)
st.sidebar.subheader('The value of Ethereum today is:')


st.header('What would you like to do today?')

#Ideally, we would want the following 3 buttons to navigate to a different page for the app
#st.button('Purchase Product')
#st.button('Purchase Buddy Tokens')
#st.button('Return/Exchanges')
 
#Creating the purchase order button for Streamlit app
st.header('Buddy Token Purchase Order')

token_quantity = st.slider('Select how many Buddy Tokens you want to purchase (per transaction limits: min. is 1; max is 10.):', 
                            min_value = 1, max_value = 10)

st.write('You are buying', token_quantity, 'Buddy Tokens.')

if st.button('Purchase Buddy Tokens'):
    tx_hash = token.functions.purchase(token_quantity).transact({'from': address})
    st.write('Tokens Purchased!')
    st.balloons()

#Create section for customer to see their token balance
if st.button('Show Buddy Token Balance Snapshot'):
    token_balance_snapshot = token_quantity
    st.write('Your Buddy Token Balance is', token_balance_snapshot, 'Buddy Tokens.')

st.header('Product Purchase Order')
st.write('Please select your purchase options below:')
st.text_input('Customer Name')

st.selectbox('Product Type', ['Cannabis', 'Accessories'])

st.selectbox('Select Product', ['1/8 oz', '1/4 oz', '1/2 oz', '1 oz'])

quantity = st.number_input('Quantity')

total_cost = quantity
if st.button('Show Total Cost'):
    st.write(total_cost)

confirm_purchase = st.button('Confirm Purchase')
if confirm_purchase:
    #Put in order for the product
    st.write("Purchase confirmed.")