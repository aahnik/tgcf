import os

import streamlit as st
import yaml

from tgcf.config import CONFIG, PluginConfig, read_config, write_config
from tgcf.plugin_models import FileType, Replace, Style
from tgcf.web_ui.password import check_password
from tgcf.web_ui.utils import get_list, get_string, hide_st, switch_theme

CONFIG = read_config()

st.set_page_config(
    page_title="Plugins",
    page_icon="🔌",
)

hide_st(st)
switch_theme(st, CONFIG)
if check_password(st):

    add_new = st.button("Add new plugin configuration")

    if add_new:
        CONFIG.plugin_cfgs.append(PluginConfig())
        write_config(CONFIG)

    num = len(CONFIG.plugin_cfgs)

    tab_strs = []
    for i in range(num):
        pc = CONFIG.plugin_cfgs[i]
        if pc.alias:
            label = pc.alias
        else:
            label = "Plugin Config " + str(i + 1)
            pc.alias = label
            write_config(CONFIG)
        tab_strs.append(label)

    tabs = st.tabs(list(tab_strs))

    for i in range(num):
        with tabs[i]:
            pc = CONFIG.plugin_cfgs[i]

            with st.expander("Core Settings"):

                pc.alias = st.text_input(
                    "Plugins Configuration Name", value=pc.alias, key=f"pcfg alias {i}"
                )
                if i != 0:
                    st.warning(
                        f"Clicking the 'Remove' button will **delete** this plugin configuration: **{pc.alias}**. This action cannot be reversed once done.",
                        icon="⚠️",
                    )
                    if st.button(
                        f"Remove plugin config **{pc.alias}**", key=f"remove_btn {i}"
                    ):
                        del CONFIG.plugin_cfgs[i]
                        write_config(CONFIG)
                        st.experimental_rerun()
                else:
                    st.warning("This is the default agent and cannot be deleted!")

            with st.expander("Filter"):
                pc.filter.check = st.checkbox(
                    "Use this plugin: filter", value=pc.filter.check, key=f"filter {i}"
                )
                st.write("Blacklist or whitelist certain text items.")
                text_tab, users_tab, files_tab = st.tabs(["Text", "Users", "Files"])

                with text_tab:
                    pc.filter.text.case_sensitive = st.checkbox(
                        "Case Sensitive",
                        value=pc.filter.text.case_sensitive,
                        key=f"case sensitive {i}",
                    )
                    pc.filter.text.regex = st.checkbox(
                        "Interpret filters as regex",
                        value=pc.filter.text.regex,
                        key=f"filter text regex {i}",
                    )

                    st.write("Enter one text expression per line")
                    pc.filter.text.whitelist = get_list(
                        st.text_area(
                            "Text Whitelist",
                            value=get_string(pc.filter.text.whitelist),
                            key=f"filter text whitelist {i}",
                        )
                    )
                    pc.filter.text.blacklist = get_list(
                        st.text_area(
                            "Text Blacklist",
                            value=get_string(pc.filter.text.blacklist),
                            key=f"filter text blacklist {i}",
                        )
                    )

                with users_tab:
                    st.write("Enter one username/id per line")
                    pc.filter.users.whitelist = get_list(
                        st.text_area(
                            "Users Whitelist",
                            value=get_string(pc.filter.users.whitelist),
                            key=f"filter users whitelist {i}",
                        )
                    )
                    pc.filter.users.blacklist = get_list(
                        st.text_area(
                            "Users Blacklist",
                            get_string(pc.filter.users.blacklist),
                            key=f"filter users blacklist {i}",
                        )
                    )

                flist = [item.value for item in FileType]
                with files_tab:
                    pc.filter.files.whitelist = st.multiselect(
                        "Files Whitelist",
                        flist,
                        default=pc.filter.files.whitelist,
                        key=f"files whitelist {i}",
                    )
                    pc.filter.files.blacklist = st.multiselect(
                        "Files Blacklist",
                        flist,
                        default=pc.filter.files.blacklist,
                        key=f"files blacklist {i}",
                    )

            with st.expander("Format"):
                pc.fmt.check = st.checkbox(
                    "Use this plugin: format", value=pc.fmt.check, key=f"format {i}"
                )
                st.write(
                    "Add style to text like **bold**, _italics_, ~~strikethrough~~, `monospace` etc."
                )
                style_list = [item.value for item in Style]
                pc.fmt.style = st.selectbox(
                    "Format",
                    style_list,
                    index=style_list.index(pc.fmt.style),
                    key=f"fmt style {i}",
                )

            with st.expander("Watermark"):
                if os.system("ffmpeg -version >> /dev/null 2>&1") != 0:
                    st.warning(
                        "Could not find `ffmpeg`. Make sure to have `ffmpeg` installed in server to use this plugin."
                    )
                pc.mark.check = st.checkbox(
                    "Apply watermark to media (images and videos).",
                    value=pc.mark.check,
                    key=f"watermark {i}",
                )
                uploaded_file = st.file_uploader(
                    "Upload watermark image(png)", type=["png"], key=f"wmark file {i}"
                )
                if uploaded_file is not None:
                    with open("image.png", "wb") as f:
                        f.write(uploaded_file.getbuffer())

            with st.expander("OCR"):
                st.write("Optical Character Recognition.")
                if os.system("tesseract --version >> /dev/null 2>&1") != 0:
                    st.warning(
                        "Could not find `tesseract`. Make sure to have `tesseract` installed in server to use this plugin."
                    )
                pc.ocr.check = st.checkbox(
                    "Activate OCR for images", value=pc.ocr.check, key=f"ocr {i}"
                )
                st.write(
                    "The text will be added in desciption of image while forwarding."
                )

            with st.expander("Replace"):
                pc.replace.check = st.checkbox(
                    "Apply text replacement",
                    value=pc.replace.check,
                    key=f"text replacement {i}",
                )
                pc.replace.regex = st.checkbox(
                    "Interpret as regex",
                    value=pc.replace.regex,
                    key=f"interpret as regex {i}",
                )

                pc.replace.text_raw = st.text_area(
                    "Replacements", value=pc.replace.text_raw, key=f"replacements {i}"
                )
                try:
                    replace_dict = yaml.safe_load(
                        pc.replace.text_raw
                    )  # validate and load yaml
                    if not replace_dict:
                        replace_dict = {}
                    temp = Replace(text=replace_dict)  # perform validation by pydantic
                    del temp
                except Exception as err:
                    st.error(err)
                    pc.replace.text = {}
                else:
                    pc.replace.text = replace_dict

                if st.checkbox("Show rules and usage", key=f"rules & usage {i}"):
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
                pc.caption.check = st.checkbox(
                    "Apply Captions", value=pc.caption.check, key=f"apply captions {i}"
                )
                pc.caption.header = st.text_area(
                    "Header", value=pc.caption.header, key=f"caption header {i}"
                )
                pc.caption.footer = st.text_area(
                    "Footer", value=pc.caption.footer, key=f"caption footer {i}"
                )
                st.write(
                    "You can have blank lines inside header and footer, to make space between the orignal message and captions."
                )

            with st.expander("Unique"):
                pc.unique.check = st.checkbox(
                    "Check if message is unique", value=pc.unique.check, key=f"apply unique {i}"
                )

            with st.expander("Sender"):
                st.write(
                    "Modify the sender of forwarded messages other than the current user/bot"
                )
                st.warning(
                    "Show 'Forwarded from' option must be disabled or else messages will not be sent",
                    icon="⚠️",
                )
                pc.sender.check = st.checkbox(
                    "Set sender to:", value=pc.sender.check, key=f"sender check {i}"
                )
                leftpad, content, rightpad = st.columns([0.05, 0.9, 0.05])
                with content:
                    user_type = st.radio(
                        "Account Type",
                        ["Bot", "User"],
                        index=pc.sender.user_type,
                        horizontal=True,
                        key=f"sender type {i}",
                    )
                    if user_type == "Bot":
                        pc.sender.user_type = 0
                        pc.sender.BOT_TOKEN = st.text_input(
                            "Bot Token",
                            value=pc.sender.BOT_TOKEN,
                            type="password",
                            key=f"sender bot token {i}",
                        )
                    else:
                        pc.sender.user_type = 1
                        pc.sender.SESSION_STRING = st.text_input(
                            "Session String",
                            pc.sender.SESSION_STRING,
                            type="password",
                            key=f"sender session str {i}",
                        )
                        st.markdown(
                            """
                        ###### How to get session string?

                        Link to repl: https://replit.com/@aahnik/tg-login?v=1

                        <p style="line-height:0px;margin-bottom:2em">
                            <i>Click on the above link and enter api id, api hash, and phone no to generate session string.</i>
                        </p>


                        > <small>**Note from developer:**<small>
                        >
                        > <small>Due some issues logging in with a user account using a phone no is not supported in this web interface.</small>
                        >
                        > <small>I have built a command-line program named tg-login (https://github.com/aahnik/tg-login) that can generate the session string for you.</small>
                        >
                        > <small>You can run tg-login on your computer, or securely in this repl. tg-login is open source, and you can also inspect the bash script running in the repl.</small>
                        >
                        > <small>What is a session string?</small>
                        > <small>https://docs.telethon.dev/en/stable/concepts/sessions.html#string-sessions</small>
                        """,
                            unsafe_allow_html=True,
                        )

            with st.expander("Google Sheets Logger"):
                pc.gsheet_logger.check = st.checkbox(
                    "Log messages to Google Sheets ?",
                    value=pc.gsheet_logger.check,
                    key=f"log to gsheet {i}",
                )
                pc.gsheet_logger.prefix = st.text_input(
                    "Prefix Match",
                    value=pc.gsheet_logger.prefix,
                    key=f"gsheet_logger prefix {i}",
                )
                pc.gsheet_logger.service_account_json = st.text_area(
                    "Google Service Account Json",
                    value=pc.gsheet_logger.service_account_json,
                    key=f"gsheet logger service account json {i}",
                )
                pc.gsheet_logger.gsheet_link = st.text_input(
                    "Google Sheet Link",
                    value=pc.gsheet_logger.gsheet_link,
                    key=f"gsheet link {i}",
                )

    if st.button("Save"):
        write_config(CONFIG)
