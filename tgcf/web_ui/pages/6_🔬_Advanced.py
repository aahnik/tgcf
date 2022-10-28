import json

import streamlit as st

from tgcf.config import CONFIG_FILE_NAME, read_config
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
        with open(CONFIG_FILE_NAME, "r") as file:
            data = json.loads(file.read())
            dumped = json.dumps(data, indent=3)

        with st.expander("View config json"):
            st.code(dumped, language="json")
        st.download_button(
            f"Download config json", data=dumped, file_name=CONFIG_FILE_NAME
        )
