import argparse
import hmac
import base64 
import hashlib

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

print(data+"."+created_signature)

