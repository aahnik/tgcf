import os
import signal
import streamlit as st

from tgcf.web_ui.utils import hide_st, switch_theme
from tgcf.config import read_config

CONFIG = read_config()

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)
hide_st(st)
switch_theme(st,CONFIG)
st.write("# Welcome to tgcf 👋")

# Check actual service status
def get_service_status():
    if CONFIG.pid != 0:
        try:
            os.kill(CONFIG.pid, signal.SIGCONT)
            return "running"
        except Exception:
            return "stopped"
    return "stopped"

service_status = get_service_status()

# Service status indicator
if service_status == "running":
    st.success(f"✅ tgcf is running (PID: {CONFIG.pid})")
elif CONFIG.auto_run:
    st.warning("⚠️ Auto-start is enabled but tgcf is not running")
else:
    st.info("ℹ️ tgcf is not running - Click the Run button to start")

html = """
<p align="center">
<img src = "https://user-images.githubusercontent.com/66209958/115183360-3fa4d500-a0f9-11eb-9c0f-c5ed03a9ae17.png" alt = "tgcf logo"  width=120>
</p>
"""

st.components.v1.html(html, width=None, height=None, scrolling=False)
with st.expander("Features"):
    st.markdown(
        """
    tgcf is the ultimate tool to automate custom telegram message forwarding.

    The key features are:

    - Forward messages as "forwarded" or send a copy of the messages from source to destination chats. A chat can be anything: a group, channel, person or even another bot.

    - Supports two modes of operation past or live. The past mode deals with all existing messages, while the live mode is for upcoming ones.

    - You may login with a bot or an user account. Telegram imposes certain limitations on bot accounts. You may use an user account to perform the forwards if you wish.

    - Perform custom manipulation on messages. You can filter, format, replace, watermark, ocr and do whatever else you need !

    - Detailed wiki + Video tutorial. You can also get help from the community.

    - If you are a python developer, writing plugins for tgcf is like stealing candy from a baby. Plugins modify the message before they are sent to the destination chat.

    What are you waiting for? Star the repo and click Watch to recieve updates.

        """
    )

st.warning("Please press Save after changing any config.")
