import os
import signal
import subprocess
import time
from importlib import resources

import tgcf.web_ui as wu
from tgcf.config import CONFIG, write_config

package_dir = resources.path(wu, "").__enter__()

def check_and_auto_start_service():
    if CONFIG.auto_run and CONFIG.pid == 0:
        mode = "live" if CONFIG.mode == 0 else "past"
        print(f"Auto-starting tgcf in {mode} mode...")
        try:
            with open("logs.txt", "w") as logs:
                process = subprocess.Popen(
                    ["tgcf", "--loud", mode],
                    stdout=logs,
                    stderr=subprocess.STDOUT,
                )
            CONFIG.pid = process.pid
            write_config(CONFIG)
            print(f"Successfully auto-started tgcf in {mode} mode with PID {process.pid}")
            return True
        except Exception as err:
            print(f"Failed to auto-start tgcf: {err}")
            return False
    elif CONFIG.auto_run and CONFIG.pid != 0:
        try:
            os.kill(CONFIG.pid, signal.SIGCONT)
            print(f"tgcf is already running with PID {CONFIG.pid}")
        except Exception:
            print("Previous tgcf process died. Auto-starting...")
            CONFIG.pid = 0
            write_config(CONFIG)
            return check_and_auto_start_service()
    return False

def main():
    print(package_dir)
    check_and_auto_start_service()
    path = os.path.join(package_dir, "0_👋_Hello.py")
    os.environ["STREAMLIT_THEME_BASE"] = CONFIG.theme
    os.environ["STREAMLIT_BROWSER_GATHER_USAGE_STATS"] = "false"
    os.environ["STREAMLIT_SERVER_HEADLESS"] = "true"
    os.system(f"streamlit run {path}")
