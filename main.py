import argparse
import hmac
import base64 
import hashlib
import os 

algorithms = {
    "SHA-256" : hashlib.sha256,
    "SHA-384" : hashlib.sha384,
    "SHA-512" : hashlib.sha512,
}


parse = argparse.ArgumentParser()
parse.add_argument('-hp' , required=True , type=str, help="the header and payload value")
parse.add_argument('-s' , required=True , type=str, help="the secret key")
parse.add_argument("-alg", choices=["SHA-256" , "SHA-384" , "SHA-512"] , help="the algorithm of signature of jwt" ,type=str , required=True)
arg = parse.parse_args()

data = arg.hp
secret = arg.s
alg = algorithms[arg.alg]

hmac_result = hmac.new(secret.encode(), data.encode(), alg)
created_signature = base64.urlsafe_b64encode(hmac_result.digest()).decode().rstrip("=")


os.system("clear")
me = "created by: "+"\033[48;5;235m"+"\033[31m"+"NakuTenshi"+"\033[0m"+"\033[0m"
print(f"""
       ___          _________ _______    _               _____                _             
      | \ \        / /__   __|__   __|  | |             / ____|              | |            
      | |\ \  /\  / /   | |     | | ___ | | _____ _ __ | |     _ __ ___  __ _| |_ ___  _ __ 
  _   | | \ \/  \/ /    | |     | |/ _ \| |/ / _ \ '_ \| |    | '__/ _ \/ _` | __/ _ \| '__|
 | |__| |  \  /\  /     | |     | | (_) |   <  __/ | | | |____| | |  __/ (_| | || (_) | |   
  \____/    \/  \/      |_|     |_|\___/|_|\_\___|_| |_|\_____|_|  \___|\__,_|\__\___/|_|  {me}  
                                                                                            
                                                                                               
"""                             
)

print("\033[32m"+"==================================================================="+"\033[0m")
print("\033[32m"+"[SUCCESS]"+"\033[0m"+" JWT Token Created")
print(f"Your JWT Token: {data}.{created_signature}")
print("\033[32m"+"==================================================================="+"\033[0m")
