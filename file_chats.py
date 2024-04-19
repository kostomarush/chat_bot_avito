import requests, json

cookies = {
    'srv_id': '0-zbLg0V_A7gmf1v.ylePT_etsf0Mj5_HD8c--YicI7AtvIQ9h2R0gkdLW_k7AAJymhACSTGO4a-nuwHiTMZG.APNQh78LwnB6O4fUwptvaIs69WWtBsP1Ceh17YKi2dU=.web',
    'gMltIuegZN2COuSe': 'EOFGWsm50bhh17prLqaIgdir1V0kgrvN',
    'u': '32g3b3di.1cw9tfr.1cswg3f3y8c50',
    'buyer_laas_location': '643190',
    'luri': 'orel',
    'buyer_location_id': '643190',
    'sx': 'H4sIAAAAAAAC%2FwTASw7CMAwE0LvMmgWWmzHObUqSsgAZiaCoH%2FXufQdIslTj4vTEid7s2dSrpXspVh35wEBGD%2FmKxvz6z%2Fv4jNiWqv2dQn9939YVNzRkMVHKQyc5zysAAP%2F%2Fi584QFsAAAA%3D',
    'v': '1713530791',
    '_gcl_au': '1.1.1876166976.1713530796',
    '_ga_M29JC28873': 'GS1.1.1713530796.1.1.1713535927.60.0.0',
    '_ga': 'GA1.1.1349482374.1713530796',
    'uxs_uid': 'dc0dc8f0-fe4a-11ee-bef5-073e6e44bfc4',
    'tmr_lvid': '860aeef0a461f19cb3e798bd3b32d108',
    'tmr_lvidTS': '1713530797690',
    'tmr_detect': '1%7C1713535913468',
    'domain_sid': 'jgKQ2xNWXbxoPw9Wadn6b%3A1713530798856',
    'f': '5.0c4f4b6d233fb90636b4dd61b04726f147e1eada7172e06c47e1eada7172e06c47e1eada7172e06c47e1eada7172e06cb59320d6eb6303c1b59320d6eb6303c1b59320d6eb6303c147e1eada7172e06c8a38e2c5b3e08b898a38e2c5b3e08b890df103df0c26013a7b0d53c7afc06d0b2ebf3cb6fd35a0ac7b0d53c7afc06d0b8b1472fe2f9ba6b9c99dece94c5a563168e2978c700f15b6831064c92d93c390fa5be3b03511ce6d04dbcad294c152cb8b1472fe2f9ba6b9ba0ac8037e2b74f9268a7bf63aa148d22ebf3cb6fd35a0ac8b1472fe2f9ba6b97b0d53c7afc06d0b71e7cb57bbcb8e0f03c77801b122405c03c77801b122405c2da10fb74cac1eab0df103df0c26013a20f3d16ad0b1c546b892c6c84ad16848a9b4102d42ade879dcb5a55b9498f642e759de1b6e2d1c4c02881b3738617d7d72d5d938a62138b67ec92593838cd9f565019b20d24bbadb68a460b021ac18e9b3f5b7836c57843afb0fb526bb39450a46b8ae4e81acb9fa46b8ae4e81acb9fadc0d86d9e44006d831449ae70b6919501d3c8616112ebeec2da10fb74cac1eab2da10fb74cac1eabf7a7ae2e9667d377f40d61b2c0299cae',
    'ft': '"3m9tuC8Ot477kc0NV57NzY8HtvbQxq00lcOPpH/E7Dn/5myipDqW2Lzi2q7h9XPquMcJLG35OWVM04LQoqlibSk7a92y1wwsh7Uez7cwGH/18XrqTTUm2eCFOBj2UaCSl8cStDqo9X8IPH0WKINM84vubtrXvTIJpOq7RyuA2qEO8mtqEaxMYU6XQFfKbL8u"',
    'sessid': 'c47da57b21a7da2f2cf2f7cdd01077b3.1713523217',
    '_ga_ZJDLBTV49B': 'GS1.1.1713530810.1.1.1713534298.0.0.0',
    '_ga_WW6Q1STJ8M': 'GS1.1.1713530810.1.1.1713534298.0.0.0',
    'buyer_from_page': 'main',
    'cartCounter': '0',
    'pageviewCount': '4',
}

headers = {
    'Host': 'www.avito.ru',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0',
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/json',
    # 'Content-Length': '122',
    'Origin': 'https://www.avito.ru',
    'Referer': 'https://www.avito.ru/profile/messenger',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    # Requests doesn't support trailers
    # 'Te': 'trailers',
    # 'Cookie': 'srv_id=0-zbLg0V_A7gmf1v.ylePT_etsf0Mj5_HD8c--YicI7AtvIQ9h2R0gkdLW_k7AAJymhACSTGO4a-nuwHiTMZG.APNQh78LwnB6O4fUwptvaIs69WWtBsP1Ceh17YKi2dU=.web; gMltIuegZN2COuSe=EOFGWsm50bhh17prLqaIgdir1V0kgrvN; u=32g3b3di.1cw9tfr.1cswg3f3y8c50; buyer_laas_location=643190; luri=orel; buyer_location_id=643190; sx=H4sIAAAAAAAC%2FwTASw7CMAwE0LvMmgWWmzHObUqSsgAZiaCoH%2FXufQdIslTj4vTEid7s2dSrpXspVh35wEBGD%2FmKxvz6z%2Fv4jNiWqv2dQn9939YVNzRkMVHKQyc5zysAAP%2F%2Fi584QFsAAAA%3D; v=1713530791; _gcl_au=1.1.1876166976.1713530796; _ga_M29JC28873=GS1.1.1713530796.1.1.1713535927.60.0.0; _ga=GA1.1.1349482374.1713530796; uxs_uid=dc0dc8f0-fe4a-11ee-bef5-073e6e44bfc4; tmr_lvid=860aeef0a461f19cb3e798bd3b32d108; tmr_lvidTS=1713530797690; tmr_detect=1%7C1713535913468; domain_sid=jgKQ2xNWXbxoPw9Wadn6b%3A1713530798856; f=5.0c4f4b6d233fb90636b4dd61b04726f147e1eada7172e06c47e1eada7172e06c47e1eada7172e06c47e1eada7172e06cb59320d6eb6303c1b59320d6eb6303c1b59320d6eb6303c147e1eada7172e06c8a38e2c5b3e08b898a38e2c5b3e08b890df103df0c26013a7b0d53c7afc06d0b2ebf3cb6fd35a0ac7b0d53c7afc06d0b8b1472fe2f9ba6b9c99dece94c5a563168e2978c700f15b6831064c92d93c390fa5be3b03511ce6d04dbcad294c152cb8b1472fe2f9ba6b9ba0ac8037e2b74f9268a7bf63aa148d22ebf3cb6fd35a0ac8b1472fe2f9ba6b97b0d53c7afc06d0b71e7cb57bbcb8e0f03c77801b122405c03c77801b122405c2da10fb74cac1eab0df103df0c26013a20f3d16ad0b1c546b892c6c84ad16848a9b4102d42ade879dcb5a55b9498f642e759de1b6e2d1c4c02881b3738617d7d72d5d938a62138b67ec92593838cd9f565019b20d24bbadb68a460b021ac18e9b3f5b7836c57843afb0fb526bb39450a46b8ae4e81acb9fa46b8ae4e81acb9fadc0d86d9e44006d831449ae70b6919501d3c8616112ebeec2da10fb74cac1eab2da10fb74cac1eabf7a7ae2e9667d377f40d61b2c0299cae; ft="3m9tuC8Ot477kc0NV57NzY8HtvbQxq00lcOPpH/E7Dn/5myipDqW2Lzi2q7h9XPquMcJLG35OWVM04LQoqlibSk7a92y1wwsh7Uez7cwGH/18XrqTTUm2eCFOBj2UaCSl8cStDqo9X8IPH0WKINM84vubtrXvTIJpOq7RyuA2qEO8mtqEaxMYU6XQFfKbL8u"; sessid=c47da57b21a7da2f2cf2f7cdd01077b3.1713523217; _ga_ZJDLBTV49B=GS1.1.1713530810.1.1.1713534298.0.0.0; _ga_WW6Q1STJ8M=GS1.1.1713530810.1.1.1713534298.0.0.0; buyer_from_page=main; cartCounter=0; pageviewCount=4',
}

params = {
    'app_name': 'web',
    'app_version': '7.309.5',
    'old_notify': 'false',
    'id_version': 'v2',
    'my_hash_id': 'aae01879ec3f6ccdbbe75a93b468e142',
}

json_data = {
    'method': 'avito.getChats.v4',
    'params': {
        'limit': 8,
        'offset': 0,
        'filters': {
            'excludeTags': [
                's',
                'p',
            ],
        },
    },
    'id': 11,
    'jsonrpc': '2.0',
}

http = 'http://127.0.0.1:8080'

response = requests.post(
    'https://www.avito.ru/web/1/socket/fallback',
    params=params,
    cookies=cookies,
    headers=headers,
    json=json_data,
    verify=False,
    proxies={'http': http, 'https': http}
)

data = response.json()

# Получение нужных данных

channels = data["result"]["channels"]

# Проход по всем каналам и вывод их идентификаторов
for channel in channels:
    channel_id = channel["channelId"]
    print("Channel ID:", channel_id)
    print('Text: ', channel['lastMessage']['body']['text'])

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"method":"avito.getChats.v4","params":{"limit":8,"offset":0,"filters":{"excludeTags":["s","p"]}},"id":11,"jsonrpc":"2.0"}'
#response = requests.post(
#    'https://www.avito.ru/web/1/socket/fallback',
#    params=params,
#    cookies=cookies,
#    headers=headers,
#    data=data,
#    verify=False,
#)