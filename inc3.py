import os

os.system("git pull")
check_vpn()
check_network()

# Reinstall modules after checking network
modules = ["requests", "chardet", "urllib3", "idna", "certifi"]
reinstall_modules(modules)

# Now that checks are complete, start the session blocker
start_session_blocker()

time.sleep(1)

# Double-check VPN and network after starting the blocker
check_vpn()

os.system("python xbow.py")
