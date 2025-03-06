import os
import time

LOCK_FILE = "/data/data/com.termux/files/home/.session_lock"

# Write the PID to lock file
with open(LOCK_FILE, "w") as f:
    f.write(str(os.getpid()))

while True:
    # Get the list of active Termux shell sessions
    sessions = os.popen('pgrep -f "com.termux"').read().strip().split("\n")

    # Allow only 1 Termux session (the current one)
    if len(sessions) > 1:
        for session in sessions:
            if session.strip() and session != str(os.getpid()):
                os.system(f"kill -9 {session}")  # Kill new Termux sessions

    time.sleep(1)  # Check every second
