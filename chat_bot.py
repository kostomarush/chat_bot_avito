import requests

url = 'https://www.avito.ru/profile'
session = requests.session()

# Set the cookie
session.cookies.set('sessid', '83fb5246402cfd7ad638e2a4016f2c24.1713303842')
https_proxy = 'https://114.132.202.125:8080'
http = 'http://104.21.69.223:80'

proxies = {
              "http" : http,
              "https": https_proxy
            }
# Make a request
response = session.get(url, verify=False, proxies = {'http': http})

# Handle response
print(response)