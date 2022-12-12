import os

import streamlit as st
import yaml

from tgcf.config import CONFIG, read_config, write_config
from tgcf.plugin_models import FileType, Replace, Style
from tgcf.web_ui.password import check_password
from tgcf.web_ui.utils import get_list, get_string, hide_st

CONFIG = read_config()

st.set_page_config(
    page_title="Plugins",
    page_icon="🔌",
)

hide_st(st)
if check_password(st):

    with st.expander("Filter"):
        CONFIG.plugins.filter.check = st.checkbox(
            "Use this plugin: filter", value=CONFIG.plugins.filter.check
        )
        st.write("Blacklist or whitelist certain text items.")
        text_tab, users_tab, files_tab = st.tabs(["Text", "Users", "Files"])

        with text_tab:
            CONFIG.plugins.filter.text.case_sensitive = st.checkbox(
                "Case Sensitive", value=CONFIG.plugins.filter.text.case_sensitive
            )
            CONFIG.plugins.filter.text.regex = st.checkbox(
                "Interpret filters as regex", value=CONFIG.plugins.filter.text.regex
            )

            st.write("Enter one text expression per line")
            CONFIG.plugins.filter.text.whitelist = get_list(
                st.text_area(
                    "Text Whitelist",
                    value=get_string(CONFIG.plugins.filter.text.whitelist),
                )
            )
            CONFIG.plugins.filter.text.blacklist = get_list(
                st.text_area(
                    "Text Blacklist",
                    value=get_string(CONFIG.plugins.filter.text.blacklist),
                )
            )

        with users_tab:
            st.write("Enter one username/id per line")
            CONFIG.plugins.filter.users.whitelist = get_list(
                st.text_area(
                    "Users Whitelist",
                    value=get_string(CONFIG.plugins.filter.users.whitelist),
                )
            )
            CONFIG.plugins.filter.users.blacklist = get_list(
                st.text_area(
                    "Users Blacklist", get_string(CONFIG.plugins.filter.users.blacklist)
                )
            )

        flist = [item.value for item in FileType]
        with files_tab:
            CONFIG.plugins.filter.files.whitelist = st.multiselect(
                "Files Whitelist", flist, default=CONFIG.plugins.filter.files.whitelist
            )
            CONFIG.plugins.filter.files.blacklist = st.multiselect(
                "Files Blacklist", flist, default=CONFIG.plugins.filter.files.blacklist
            )

    with st.expander("Format"):
        CONFIG.plugins.fmt.check = st.checkbox(
            "Use this plugin: format", value=CONFIG.plugins.fmt.check
        )
        st.write(
            "Add style to text like **bold**, _italics_, ~~strikethrough~~, `monospace` etc."
        )
        style_list = [item.value for item in Style]
        CONFIG.plugins.fmt.style = st.selectbox(
            "Format", style_list, index=style_list.index(CONFIG.plugins.fmt.style)
        )

    with st.expander("Watermark"):
        if os.system("ffmpeg -version >> /dev/null 2>&1") != 0:
            st.warning(
                "Could not find `ffmpeg`. Make sure to have `ffmpeg` installed in server to use this plugin."
            )
        CONFIG.plugins.mark.check = st.checkbox(
            "Apply watermark to media (images and videos).",
            value=CONFIG.plugins.mark.check,
        )
        uploaded_file = st.file_uploader("Upload watermark image(png)", type=["png"])
        if uploaded_file is not None:
            with open("image.png", "wb") as f:
                f.write(uploaded_file.getbuffer())

    with st.expander("OCR"):
        st.write("Optical Character Recognition.")
        if os.system("tesseract --version >> /dev/null 2>&1") != 0:
            st.warning(
                "Could not find `tesseract`. Make sure to have `tesseract` installed in server to use this plugin."
            )
        CONFIG.plugins.ocr.check = st.checkbox(
            "Activate OCR for images", value=CONFIG.plugins.ocr.check
        )
        st.write("The text will be added in desciption of image while forwarding.")

    with st.expander("Replace"):
        CONFIG.plugins.replace.check = st.checkbox(
            "Apply text replacement", value=CONFIG.plugins.replace.check
        )
        CONFIG.plugins.replace.regex = st.checkbox(
            "Interpret as regex", value=CONFIG.plugins.replace.regex
        )

        CONFIG.plugins.replace.text_raw = st.text_area(
            "Replacements", value=CONFIG.plugins.replace.text_raw
        )
        try:
            replace_dict = yaml.safe_load(
                CONFIG.plugins.replace.text_raw
            )  # validate and load yaml
            if not replace_dict:
                replace_dict = {}
            temp = Replace(text=replace_dict)  # perform validation by pydantic
            del temp
        except Exception as err:
            st.error(err)
            CONFIG.plugins.replace.text = {}
        else:
            CONFIG.plugins.replace.text = replace_dict

        if st.checkbox("Show rules and usage"):
            st.markdown(
                """
                Replace one word or expression with another.

                - Write every replacement in a new line.
                - The original text then **a colon `:`** and then **a space** and then the new text.
                - Its recommended to use **single quotes**. Quotes are must when your string contain spaces or special characters.
                - Double quotes wont work if your regex has the character: `\` .
                    ```
                    'orginal': 'new'

                    ```
                - View [docs](https://github.com/aahnik/tgcf/wiki/Replace-Plugin) for advanced usage."""
            )

    with st.expander("Caption"):
        CONFIG.plugins.caption.check = st.checkbox(
            "Apply Captions", value=CONFIG.plugins.caption.check
        )
        CONFIG.plugins.caption.header = st.text_area(
            "Header", value=CONFIG.plugins.caption.header
        )
        CONFIG.plugins.caption.footer = st.text_area(
            "Footer", value=CONFIG.plugins.caption.footer
        )
        st.write(
            "You can have blank lines inside header and footer, to make space between the orignal message and captions."
        )

    if st.button("Save"):
        write_config(CONFIG)
