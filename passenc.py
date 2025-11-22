import base64
import io
import struct
import time
import json
import requests
from Cryptodome.Cipher import AES, PKCS1_v1_5
from Cryptodome.PublicKey import RSA
from Cryptodome.Random import get_random_bytes

def encrypt_password(password, public_key=None, key_id="25"):
    if public_key is None:
        try:
            pwd_key_fetch = 'https://b-graph.facebook.com/pwd_key_fetch'
            pwd_key_fetch_data = {
                'version': '2',
                'flow': 'CONTROLLER_INITIALIZATION',
                'method': 'GET',
                'fb_api_req_friendly_name': 'pwdKeyFetch',
                'fb_api_caller_class': 'com.facebook.auth.login.AuthOperations',
                'access_token': '438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28'
            }
            response = requests.post(pwd_key_fetch, params=pwd_key_fetch_data).json()
            public_key = response.get('public_key')
            key_id = str(response.get('key_id', key_id))
        except Exception as e:
            raise Exception(f"Không thể lấy public key từ API: {e}")


    try:
        rand_key = get_random_bytes(32) 
        iv = get_random_bytes(12)

        pubkey = RSA.import_key(public_key)
        cipher_rsa = PKCS1_v1_5.new(pubkey)

        encrypted_rand_key = cipher_rsa.encrypt(rand_key)

        cipher_aes = AES.new(rand_key, AES.MODE_GCM, nonce=iv)
        current_time = int(time.time())
        cipher_aes.update(str(current_time).encode("utf-8"))
        encrypted_passwd, auth_tag = cipher_aes.encrypt_and_digest(password.encode("utf-8"))

        buf = io.BytesIO()
        buf.write(bytes([1, int(key_id)]))
        buf.write(iv)  # IV
        buf.write(struct.pack("<h", len(encrypted_rand_key)))
        buf.write(encrypted_rand_key)
        buf.write(auth_tag) 
        buf.write(encrypted_passwd)
        encoded = base64.b64encode(buf.getvalue()).decode("utf-8")
        return f"#PWD_FB4A:2:{current_time}:{encoded}"
    except Exception as e:
        raise Exception(f"Lỗi khi mã hóa mật khẩu: {e}")

password = "itvanhai.dev9x"
encrypted_password = encrypt_password(password)
print(encrypted_password)