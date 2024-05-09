from web3 import Web3
from web3.middleware import geth_poa_middleware
from contractinfo import abi, contract_adress

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

contract = w3.eth.contract(address=contract_adress, abi=abi)

login = None

def auth():
    public_key = input("Enter public key: ")
    password = input("Enter password: ")
    try:
        w3.geth.personal.unlock_account(public_key, password)
        print("Authentication successful")
        return public_key
    except Exception as e:
        print(e)
        return None

def registration():
    password = input("Enter password: ")
    # Add password complexity checks here
    # Length check
    if len(password) < 12:
        print("Password must be at least 12 characters long.")
        return

    # Check for different types of characters - uppercase, lowercase, digits, special characters
    if not any(char.isupper() for char in password) or not any(char.islower() for char in password) or not any(char.isdigit() for char in password) or not any(char.isalnum() for char in password):
        print("Password must contain uppercase, lowercase letters, digits, and special characters.")
        return

    adress = w3.geth.personal.new_account(password)
    print(f"Address of the new account: {adress}")


def create_estate():
    login
    id_est = int(input("Введите айди недвижимости: "))
    size = int(input("Введите размер недвижимости: "))
    photo = input("Введите фото недвижимости: ")
    rooms =  int(input("Введите кол-во комнат недвижимости: "))
    type = int(input("Введите тип недвижимости: "))
    try:
        contract.functions.createEstate(id_est,size,photo,rooms, type).transact({'from': login})
        print("Вы создали недвижимость")
    except :
        print("что то пошло не так")
    pass

def create_ad():
    price = int(input("Введите стоимость: "))
    datetime = int(input("Введите дату: "))
    estate_id = int(input("Введите айди недвижимости"))
    try:
        contract.functions.createAdd(price,datetime,estate_id).transact({'from': login})
        print("Вы создали объявление")
    except:
        print("что то пошло не так")
    pass

def change_estate_status():
    id_est = int(input("Введите айди недвижимости"))
    try:
        contract.functions.updateAddStatus(id_est).transact({'from': login})
        print("Вы изменили статус недвижимости")
    except:
        print("что то пошло не так")
    pass

def change_ad_status():
    id_ad = int(input("Введите айди объявления"))
    try:
        contract.functions.updateAddStatus(id_ad).transact({'from': login})
        print("Вы изменили статус объявления")
    except:
        print("что то пошло не так")
    pass

def buy_estate():
    id_est = int(input("Введите айди недвижимости"))
    try:
        contract.functions.buyEstate(id_est).transact({'from': login})
        print("Вы купили недвижимость")
    except:
        print("что то пошло не так")
    pass

def withdraw_funds(account):
    cash = int(input("Введите сумму"))
    try:
        contract.functions.cashthrow(cash).transact({'from': login})
        print("Вы сняли средства")
    except:
        print("что то пошло не так")
    pass

def get_available_realty_info():
    # Add code here to get information about available real estate
    pass

def get_listing_info():
    # Add code here to get information about current real estate listings
    pass

def get_contract_balance(account):
    # Add code here to get information about the user's balance on the smart contract
    pass

def get_account_balance():
    # Add code here to get information about the user's balance on the account
    pass

def main():
    account = ""
    is_auth = False
    while True:
        choice = input("Select:\n1. Send Ether\n2. Check smart contract balance\n3. Withdraw funds\n4. Check account balance\n5. Logout\n")
        match choice:
            case "1":
                create_ad()



if __name__ == "__main__":
    main()