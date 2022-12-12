import json

import streamlit as st

from tgcf.config import CONFIG_FILE_NAME, read_config, write_config
from tgcf.utils import platform_info
from tgcf.web_ui.password import check_password
from tgcf.web_ui.utils import hide_st

CONFIG = read_config()

st.set_page_config(
    page_title="Advanced",
    page_icon="🔬",
)
hide_st(st)

if check_password(st):

    st.warning("This page is for developers and advanced users.")
    if st.checkbox("I agree"):

        with st.expander("Version & Platform"):
            st.code(platform_info())

        with st.expander("Configuration"):
            with open(CONFIG_FILE_NAME, "r") as file:
                data = json.loads(file.read())
                dumped = json.dumps(data, indent=3)
            st.download_button(
                f"Download config json", data=dumped, file_name=CONFIG_FILE_NAME
            )
            st.json(data)

        with st.expander("Special Options for Live Mode"):
            st.info(
                "Note: For userbots, the commands start with `.` instead of `/`, like `.start` and not `/start`"
            )
            CONFIG.bot_messages.start = st.text_area(
                "Bot's Reply to /start command", value=CONFIG.bot_messages.start
            )
            CONFIG.bot_messages.bot_help = st.text_area(
                "Bot's Reply to /help command", value=CONFIG.bot_messages.bot_help
            )
            CONFIG.live.delete_on_edit = st.text_input(
                "Delete a message when source edited to",
                value=CONFIG.live.delete_on_edit,
            )
            st.write(
                "When you edit the message in source to something particular, the message will be deleted in both source and destinations."
            )

            if st.button("Save"):
                write_config(CONFIG)
