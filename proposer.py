'''

After the Constructor build Subtrades, the Proposer simulates the trades and 
shows the user what the expected results are.

Notes:
-Use getAmountsOut type methods to see how much you would extract

'''

from configparser import ConfigParser
from web3 import Web3
from web3.middleware import geth_poa_middleware
from abi_list import abi_dict
from token_list import token_dict
from routers import router_dict
import time

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


# Function to get the Simulated Trade
def checkSubTrade(exchange, in_token_address, out_token_address, amount):

    # Should be general cross exchange but would have to check if each routers contain the same methods
    router_address = w3.toChecksumAddress(router_dict[str(exchange)])
    router_abi = abi_dict[str(exchange)]
    router_contract = w3.eth.contract(address = router_address, abi = router_abi)
    swap_path = [in_token_address, out_token_address]

    output = router_contract.functions.getAmountsOut(amount, swap_path).call()

    return output

def proposer(subtrade):
    
    #run the subtrade checker to see how much you would receive at the end
    output = subtrade
    print(output)
    
    #check user approval
    user_input = input("Do you want to proceed? y/n: ")
    
    #if yes then run the executor
    if input == ('y'):
        '''executor'''
    
    #else
    else:
        '''
        give the option to reroll or to quit
        '''

output = checkSubTrade('uniswap', token_dict['WETH'], token_dict['UNI'], 100000000)
print(output) #INSUFFICIENT LIQUIDITY for some reason