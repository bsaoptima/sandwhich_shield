from configparser import ConfigParser
from web3 import Web3
from web3.middleware import geth_poa_middleware
import time

import constructor, proposer, executor

# read config.ini
config = ConfigParser()
config.read('config.ini')

# account details section
account = config.get('Account_Details', 'account')
private_key = config.get('Account_Details', 'private_key')

# connection details section
http_rpc_url = config.get('Connection_Details', 'http_rpc_url')

# connect to Ethereum Blockchain
w3 = Web3(Web3.HTTPProvider(http_rpc_url))

# middleware
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

if __name__ == "__main__":
    
    #start by asking the user for the InputTrade
    input_tokenin = input("Specify tokenIn :")
    input_tokenout = input("Specify tokenOut :")
    input_amount = input("How much :")
    
    #create the InputTrade dictionnary
    InputTrade = {
        'tokenIn' : input_tokenin,
        'tokenOut': input_tokenout,
        'amount' : input_amount
    }
    
    #place InputTrade in constructor
    