import time
from datetime import datetime as dt

hosts_tmp = "hosts"
hosts_path = r"/ect/hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com", ]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("Working hours")
        with open (hots_temp, 'r+') as file:
            content = file.read()
            print(content)
            for website in website_list:
                if website in content:
                    pass 
                else:
                    file.write(redirect+" "+content"\n")
    else:
        with open(hosts_tmp, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any (website in line for website in website_list):
                    file.write(line:)
            file.truncate()
        print("Fun hours")
    time.sleep(5)
