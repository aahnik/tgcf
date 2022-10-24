import streamlit as st

from tgcf.web_ui.utils import hide_st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)
hide_st(st)
st.write("# Welcome to tgcf 👋")

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
