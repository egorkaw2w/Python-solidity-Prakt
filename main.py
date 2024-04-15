from web3 import Web3
from web3.middleware import geth_poa_middleware
from contractinfo import abi, contract_adress

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

contract = w3.eth.contract(address=contract_adress, abi=abi)
def get_balance():
    names = w3.eth.accounts
    counter = 0
    for i in names:
        counter+=1
        balance = w3.from_wei(w3.eth.get_balance(i), 'ether')
        print(f"{counter}. На аккаунте \"{i}\": баланс {balance}   Ether")


get_balance();
