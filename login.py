import requests
user=input('net id: ')
passw=input('net passward: ')
url = 'http://10.10.43.3/drcom/login?callback=dr1678777892154&DDDDD='+user+'&upass='+passw+'&0MKKey=123456&R1=0&R3=0&R6=0&para=00&v6ip=&_=1678777869973'
response = requests.get(url).status_code 
print("状态码{}".format(response))  
