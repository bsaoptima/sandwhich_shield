'''

Executor executes the Subtrades if the Proposer is accepted.

Notes:
-Switch for Exact IN to Exact OUT

'''

from configparser import ConfigParser
from web3 import Web3
from web3.middleware import geth_poa_middleware
from abi_list import abi_dict
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

# middleware
w3.middleware_onion.inject(geth_poa_middleware, layer=0)


''' UNISWAP '''

def uniswap_swap(in_token_address, out_token_address, amount):
    router_address = "0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D" # basically the contract address
    router_abi = abi_dict['uniswap']
    router_contract = w3.eth.contract(router_address, abi=router_abi)

    nonce = w3.eth.getTransactionCount(account)
    swap_path = [in_token_address, out_token_address]    


    # build transaction
    swap_transaction = router_contract.functions.swapExactTokensForTokens(
        w3.toWei(amount, 'ether'), #uint amountIn 
        0.0003 * w3.toWei(amount, 'ether'), #uint amountOutMin,
        swap_path, #address[] calldata path,
        account,#address to,
        int(time.time()) + (60*20)#uint deadline
    )

    tx = swap_transaction.buildTransaction({
        'from': account,
        'nonce': nonce,
        'gasPrice': w3.eth.gas_price
    })

    signed_tx = w3.eth.account.signTransaction(tx, private_key)
    sent_tx = w3.eth.sendRawTransaction(signed_tx.rawTransaction)


''' SUSHISWAP '''

def sushiswap_swap(in_token_address, out_token_address, amount):

    # connect to Smart Contract
    router_address = "0xd9e1cE17f2641f24aE83637ab66a2cca9C378B9F"
    router_abi = abi_dict['sushiswap']
    router_contract = w3.eth.contract(router_address, router_abi)

    nonce = w3.eth.getTransactionCount(account)
    swap_path = [in_token_address, out_token_address]    

    # build transaction
    swap_transaction = router_contract.functions.swapExactTokensForTokens(
        w3.toWei(amount, 'ether'), #uint amountIn 
        0.0003 * w3.toWei(amount, 'ether'), #uint amountOutMin,
        swap_path, #address[] calldata path,
        account,#address to,
        int(time.time()) + (60*20)#uint deadline
    )

    tx = swap_transaction.buildTransaction({
        'from': account,
        'nonce': nonce,
        'gasPrice': w3.eth.gas_price
    })

    signed_tx = w3.eth.account.signTransaction(tx, private_key)
    sent_tx = w3.eth.sendRawTransaction(signed_tx.rawTransaction)