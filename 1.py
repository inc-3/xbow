import random
import requests

fu = "https://xbow-inc3-default-rtdb.asia-southeast1.firebasedatabase.app/user_agents/ver.json"

def get_ua():
    try:
        response = requests.get(fu, timeout=5)
        if response.status_code == 200:
            return response.text.strip().replace('"', '')
        else:
            print(f"Error: Failed to fetch (HTTP {response.status_code})")
    except requests.exceptions.RequestException as e:
        print(f"Network error")
    
    return ""
e = get_ua()
def user_agent():
    s = "[FBAN/FB4A;FBAV/" + str(random.randint(111, 999)) + '.0.0.' + str(random.randrange(9, 99)) + str(
        random.randint(111, 999)) + ";FBBV/" + str(random.randint(111111111, 999999999))
    if not e:
        return None
    ua = s + e
    return ua

# Example usage
user_agent = user_agent()
if user_agent:
    print("Generated User-Agent:", user_agent)
