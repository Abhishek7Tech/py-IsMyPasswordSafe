from base64 import encode
import requests
import hashlib
import sys

url = 'https://api.pwnedpasswords.com/range/1e75a'
req = requests.get(url)
print(req)

def fetch_api(char):
    url = f'https://api.pwnedpasswords.com/range/{char}'
    req = requests.get(url)
    print(req)
    if(req.status_code != 200):
        raise RuntimeError("ERROR FETCHING")
    return req

def no_of_times_pawned(hashes, hash_to_check):
    hashed = (line.split(':') for line in hashes.splitlines())
    for h, count in hashed:
        if(h == hash_to_check):
            return count
    return 0

def hash_pass(password):
    hashedPass = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first_five, tail = hashedPass[:5], hashedPass[5:]
    response = fetch_api(first_five)
    count = no_of_times_pawned(response.text,tail)
    return count


def main(args):
    print(args)
    for passwords in args:
        count = hash_pass(passwords)
        if count:
            print(f"your password has been pawned {count} Times!")
        else:
            print("You are safe!")

main(sys.argv[1:])
