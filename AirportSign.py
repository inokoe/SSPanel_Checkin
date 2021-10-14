import requests
import time
import json
import os
from bs4 import BeautifulSoup

headers = {
    'user_agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
    'referer': '',
    'sec-fetch-mode': 'navigate',
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-site': 'same-origin',
    'upgrade-insecure-requests': '1',
    'sec-fetch-dest': 'document',
    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
}

airportUrl = os.environ["AIRPORTURL"].split('&&')
userPasswd = os.environ["USERPASSWD"].split('&&')
userName = os.environ["USERNAME"].split('&&')


def airport_passport(number):
    push = ''
    params = {}
    params['email'] = userName[number]
    params['passwd'] = userPasswd[number]
    url = airportUrl[number]
    headers['referer'] = url
    url = url + '/auth/login'
    response = requests.post(url=url, params=params, headers=headers)
    if response.status_code == 200:
        headers['referer'] = airportUrl[number] + '/user'
        cookies = response.cookies.get_dict()
        print('Cookie catch success')
        count_posA = 0
        count_posB = 0
        for i in url:
            count_posA += 1
            if i == '/':
                count_posB += 1
                if count_posB == 3:
                    break
        url = url[0:count_posA] + 'user/checkin'
        real_cookie = ''
        for key in cookies.keys():
            real_cookie += key + '=' + cookies.get(key) + ';'
        headers['cookie'] = real_cookie
        try:
            msg = requests.post(url, headers=headers)
            if(msg.status_code == 200):
                msg = json.loads(msg.text)
                print('Checkin success and the result msg : ', end="")
                print(msg["msg"])
                response = requests.get(url[0:count_posA]+'user', headers=headers)
                soup = BeautifulSoup(response.text, features="html.parser")
                soup = soup.find_all("div")
                try:
                    print('Try to get usage data ... ', end="")
                    for i in soup:
                        if i.text.strip().endswith('GB') | i.text.strip().endswith('MB'):
                            s = i.text.strip().replace('\n', '').replace('\r', '')
                            if s.find('%') >= 0:
                                s = s[s.find('%')+1:]
                            temp = s.find('GB')
                            if temp > 0:
                                push = s[0:temp+1].replace('剩余流量', '').strip()
                                push = '剩余流量|Usage data:' + push
                                #push += url[0:count_posA]
                                #push += " | "
                                #push += s
                            else:
                                push += '小于1G'
                            break
                    print(push)
                    print("No."+str(number + 1) + ' SUCCESS')
                except:
                    print('Failed to get usage data' + response.status_code)
            else:
                print('Check in failed ' + msg.status_code)
        except:
            print('Check in failed ')
    else:
        print('Login failed ' + response.status_code)


if __name__ == '__main__':
    start_time = time.time()
    for i in range(len(airportUrl)):
        print("\r\nNo."+str(i+1)+" running...")
        airport_passport(i)
    end_time = time.time() - start_time
    print('\r\nALL LINK DONE:', end_time)
