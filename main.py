# aids code i know (woosh#1337)
import tls_client

with open("keys.txt", "r") as f:
    keys = f.read().splitlines()

sess = tls_client.Session(client_identifier="chrome_105")
headers = {
    'authority': 'stand.gg',
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,pt;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': 'a=1',
    'dnt': '1',
    'origin': 'https://stand.gg',
    'referer': 'https://stand.gg/account/login',
    'sec-ch-ua': '^\\^Google',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '^\\^Windows^\\^',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}
 

for k in keys:
    data = {'account_id': k}
    response = sess.post('https://stand.gg/api/basic_account_info', headers=headers, data=data)
    s = response.json()
    plan_numb = s["privilege"]
    suspended = s["suspended_for"]
    if plan_numb == 1:
        if suspended == '':
            print(f"Key: {k} | Plan: Basic ({plan_numb})")
            f = open("basic.txt", "a")
            f.write(f"{k}\n")
    elif plan_numb == 2:
        if suspended == '':
            print(f"Key: {k} | Plan: Regular ({plan_numb})")
            f = open("regular.txt", "a")
            f.write(f"{k}\n")
    elif plan_numb == 3:
        if suspended == '':
            print(f"Key: {k} | Plan: Ultimate ({plan_numb})")
            f = open("ultimate.txt", "a")
            f.write(f"{k}\n")
    else:
        print(s)
        f = open("error.txt", "a")
        f.write(f"{k}\n")
