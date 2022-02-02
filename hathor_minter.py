
#	Created by Mauricio Nunes
#    url: https://github.com/mbnunes/
#    date: 02/02/2022


import requests

# Wallet ID in Hathor Headless Wallet
WALLET_ID = ""
# token name
NAME_TOKEN = ""
# token symbol
SYMBOL_TOKEN = ""
# Amount of the token to be generated
AMOUNT_TOKEN = 1
# IPFS hash where the data is
DATA_HASH_TOKEN = ""
# Wallet address where the token will be sent
ADDRESS_TO_SEND = ""
# Total tokens created, with this amount the loop will know how many times it will have to make the request
TOTAL_CREATED = 2500 
# Interval of each NFT creation, the correct one according to pedro (from hathor's team) would be 15 seconds on a public node or 5 seconds on a private node
INTERVAL = 5


url = "http://localhost:8000/wallet/create-nft"
headers = {"x-wallet-id": WALLET_ID}

import time

for i in range(1,TOTAL_CREATED+1):
    payloads = {"name": NAME_TOKEN+str(i), "symbol": SYMBOL_TOKEN+str(i), "amount": AMOUNT_TOKEN , "data": "ipfs://ipfs/"+DATA_HASH_TOKEN+"/"+str(i)+".json", "address": ADDRESS_TO_SEND}
    r = requests.post(url, headers=headers, data=payloads)

    # Console message and creating a log file for each MINT
    print("UUID "+str(i)+"\n")
    arquivo = str(i)+"_content.json"
    f = open(arquivo, "wb")
    f.write(r.text.encode())
    f.close()
    
    time.sleep(INTERVAL)
