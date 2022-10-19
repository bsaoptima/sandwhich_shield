'''
Get the Main Trade and Splits it into SubTrades based on some rules.

Notes:
-Code is working
-Define the addresses in token_list.py

'''

from token_list import token_dict
import math

def constructor(InputTrade, limit):
    '''
    
    for now please input only integers
    
    InputTrade:
    -tokenIn
    -tokenOut
    -amount
    
    '''
    amount_limit = limit #in eth units so here 2 ETH
    subTrade_list = []

    if InputTrade['amount'] > amount_limit:
        
        if (InputTrade['amount'] % limit) == 0:
            number_of_subtrades = int(InputTrade['amount'] / amount_limit)
            
            for i in range(0, number_of_subtrades):
                subTrade = {
                    'tokenIN': InputTrade['tokenIN'],
                    'addressIN': token_dict[InputTrade['tokenIN']],
                    'tokenOUT': InputTrade['tokenOUT'],
                    'addressOUT': token_dict[InputTrade['tokenOUT']],
                    'amount': amount_limit,
                    'exchange': "To be Defined"
                }
                subTrade_list.append(subTrade)
        
        else:
            number_of_subtrades = int(math.floor(InputTrade['amount'] / amount_limit))

            for k in range(0, number_of_subtrades):
                subTrade = {
                    'tokenIN': InputTrade['tokenIN'],
                    'addressIN': token_dict[InputTrade['tokenIN']],
                    'tokenOUT': InputTrade['tokenOUT'],
                    'addressOUT': token_dict[InputTrade['tokenOUT']],
                    'amount': amount_limit,
                    "exchange": "To be Defined"
                }
                subTrade_list.append(subTrade)

            subTrade_unit = {
                'tokenIN': InputTrade['tokenIN'],
                'addressIN': token_dict[InputTrade['tokenIN']],
                'tokenOUT': InputTrade['tokenOUT'],
                'addressOUT': token_dict[InputTrade['tokenOUT']],
                'amount': InputTrade['amount'] - amount_limit * number_of_subtrades, # remainder should be less than limit
                'exchange': "To be Defined"
            }

            subTrade_list.append(subTrade_unit)
    
    return subTrade_list


trade = {
    'tokenIN' : "WETH",
    'tokenOUT' : 'UNI',
    'amount' : 7
}

subTrades = constructor(trade, 2)
print(subTrades)