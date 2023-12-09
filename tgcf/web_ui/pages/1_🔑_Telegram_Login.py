import streamlit as st

from tgcf.config import (
    CONFIG,
    AgentForwardingConfig,
    AgentLoginConfig,
    read_config,
    write_config,
)
from tgcf.web_ui.password import check_password
from tgcf.web_ui.utils import hide_st, switch_theme

CONFIG = read_config()

st.set_page_config(
    page_title="Telegram Login",
    page_icon="🔑",
)
hide_st(st)
switch_theme(st, CONFIG)
if check_password(st):
    CONFIG.login_cfg.tg.API_ID = int(
        st.text_input("API ID", value=str(CONFIG.login_cfg.tg.API_ID), type="password")
    )
    CONFIG.login_cfg.tg.API_HASH = st.text_input(
        "API HASH", value=CONFIG.login_cfg.tg.API_HASH, type="password"
    )
    st.write("You can get api id and api hash from https://my.telegram.org.")

    add_new = st.button("Add new Forwarding Agent")

    if add_new:
        CONFIG.login_cfg.agents.append(AgentLoginConfig())
        CONFIG.agent_fwd_cfg.append(AgentForwardingConfig())
        write_config(CONFIG)

    num = len(CONFIG.login_cfg.agents)

    tab_strs = []

    for i in range(num):
        agent = CONFIG.login_cfg.agents[i]
        if agent.alias:
            label = agent.alias
        else:
            label = "Agent " + str(i + 1)
            agent.alias = label
            write_config(CONFIG)
        tab_strs.append(label)

    tabs = st.tabs(list(tab_strs))

    for i in range(num):
        with tabs[i]:
            # todo: implement delete agent
            # when you are deleting agent from login config
            # you must also delete agent from forwarding config

            agent = CONFIG.login_cfg.agents[i]
            agent.alias = st.text_input(
                "Agent Name", key=f"agent {i}", value=agent.alias
            )

            user_type = st.radio(
                "Choose account type",
                ["Bot", "User"],
                index=agent.user_type,
                key=f"user_type {i}",
            )
            if user_type == "Bot":
                agent.user_type = 0
                agent.BOT_TOKEN = st.text_input(
                    "Enter bot token",
                    value=agent.BOT_TOKEN,
                    type="password",
                    key=f"bot_token {i}",
                )
            else:
                agent.user_type = 1
                agent.SESSION_STRING = st.text_input(
                    "Enter session string",
                    value=agent.SESSION_STRING,
                    type="password",
                    key=f"session_string {i}",
                )
                with st.expander("How to get session string ?"):
                    st.markdown(
                        """

                    Link to repl: https://replit.com/@aahnik/tg-login?v=1

                    _Click on the above link and enter api id, api hash, and phone no to generate session string._

                    **Note from developer:**

                    Due some issues logging in with a user account using a phone no is not supported in this web interface.

                    I have built a command-line program named tg-login (https://github.com/aahnik/tg-login) that can generate the session string for you.

                    You can run tg-login on your computer, or securely in this repl. tg-login is open source, and you can also inspect the bash script running in the repl.

                    What is a session string ?
                    https://docs.telethon.dev/en/stable/concepts/sessions.html#string-sessions

                    """
                    )
            with st.expander("Delete this agent"):
                if i != 0:
                    st.warning(
                        f"Clicking the 'Remove' button will **delete** this agent: **{agent.alias}**. This action cannot be reversed once done.",
                        icon="⚠️",
                    )
                    if st.button(
                        f"Remove agent **{agent.alias}**", key=f"remove_btn {i}"
                    ):
                        del CONFIG.login_cfg.agents[i]
                        del CONFIG.agent_fwd_cfg[i]
                        write_config(CONFIG)
                        st.experimental_rerun()
                else:
                    st.warning("This is the default agent and cannot be deleted!")

    if st.button("Save"):
        write_config(CONFIG)
