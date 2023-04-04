import requests
url = 'http://10.10.42.3/drcom/logout?callback=dr1680327504919&_=1680327490216'
response = requests.get(url).status_code  
print("状态码{}".format(response))  