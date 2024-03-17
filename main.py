import requests
import threading
from pystyle import Colors, Colorate

RED = '\033[31m'
GREEN = '\033[32m'
RESET = '\033[0m'
BLUE = '\033[96m'

title = '''
 _ _                 _      
| \ | ___  ___  _ _ | | ___ 
|   |/ ._>/ . || | || |<_> |
|_\_|\___.\_. |`___||_|<___|
          <___'             

'''
print(Colorate.Horizontal(Colors.purple_to_blue, str(title), 1))

url = 'https://ngl.link/api/submit'

num_threads = int(input("How many threads >>> "))

requests_per_thread = int(input("How many requests per thread >>> "))

headers = {
    'Cookie': 'mp_e8e1a30fe6d7dacfa1353b45d6093a00_mixpanel=%7B%22distinct_id%22%3A%20%22%24device%3A18e3938e556f78-09cc1797b762ed-673e5551-100200-18e3938e556f78%22%2C%22%24device_id%22%3A%20%2218e3938e556f78-09cc1797b762ed-673e5551-100200-18e3938e556f78%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%7D; _ga_5DV1ZR5ZHG=GS1.1.1710357014.1.0.1710357014.0.0.0; _ga=GA1.1.2098580779.1710357015',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
    'Origin': 'https://ngl.link',
    'Referer': 'https://ngl.link/pep0n._mp0112',
    'X-Requested-With': 'XMLHttpRequest',
}

data = {
    'username': '',
    'question': '',
    'deviceId': 'dc8d5332-7411-41ad-a6a3-4b4f7ebe8ec0',
    'gameSlug': '',
    'referrer': ''
}

new_username = input("Enter username >>>  ")
data['username'] = new_username
new_question = input("Enter question >>>  ")
data['question'] = new_question
print("Updated data:", data)

def send_post_request(thread_id, num_requests):
    for i in range(num_requests):
        response = requests.post(url, headers=headers, data=data)
        print(f"{RED}Thread {GREEN}[{thread_id}]{RED}: Request{GREEN}[{i+1}]{RED}, Response Code: {response.status_code}{RESET} \n")



threads = []

for i in range(num_threads):
    thread = threading.Thread(target=send_post_request, args=(i+1, requests_per_thread))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
total = requests_per_thread * num_threads
print(f"{GREEN}Done. Sent: {RESET}" + str(total) + " Questions.")
input("")
