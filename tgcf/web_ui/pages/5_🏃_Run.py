import os
import signal
import subprocess
import time

import streamlit as st

from tgcf.config import CONFIG, read_config, write_config
from tgcf.web_ui.password import check_password
from tgcf.web_ui.utils import hide_st, switch_theme

CONFIG = read_config()


def termination(agent_id:int):
    st.code("process terminated!")
    os.rename(f"logs_{i}.txt", f"old_logs_{i}.txt")
    with open("old_logs.txt", "r") as f:
        st.download_button(
            "Download last logs", data=f.read(), file_name=f"tgcf_logs_{i}.txt"
        )

    CONFIG = read_config()
    CONFIG.agent_fwd_cfg[i].pid= 0
    write_config(CONFIG)
    st.button("Refresh page")


st.set_page_config(
    page_title="Run",
    page_icon="🏃",
)
hide_st(st)
switch_theme(st, CONFIG)
if check_password(st):
    num = len(CONFIG.login_cfg.agents)

    tab_strs = []

    for i in range(num):
        agent = CONFIG.login_cfg.agents[i]
        if agent.alias:
            label = agent.alias
        else:
            label = "Agent " + str(i + 1)
            agent.alias = label
        tab_strs.append(label)

    tabs = st.tabs(list(tab_strs))

    for i in range(num):
        with tabs[i]:
            agent = CONFIG.login_cfg.agents[i]

            st.write(agent.alias)
            agent_fc = CONFIG.agent_fwd_cfg[i]

            with st.expander("Configure Run"):
                agent_fc.show_forwarded_from = st.checkbox(
                    "Show 'Forwarded from'",
                    value=agent_fc.show_forwarded_from,
                    key=f"sff {i}",
                )
                mode = st.radio(
                    "Choose mode",
                    ["live", "past"],
                    index=agent_fc.mode,
                    key=f"mode {i}",
                )
                if mode == "past":
                    agent_fc.mode = 1
                    st.warning(
                        "Only User Account can be used in Past mode. Telegram does not allow bot account to go through history of a chat!"
                    )
                    agent_fc.past.delay = st.slider(
                        "Delay in seconds",
                        0,
                        100,
                        value=agent_fc.past.delay,
                        key=f"delay {i}",
                    )
                else:
                    agent_fc.mode = 0
                    agent_fc.live.delete_sync = st.checkbox(
                        "Sync when a message is deleted",
                        value=agent_fc.live.delete_sync,
                        key=f"del sync {i}",
                    )
                if st.button("Save ", key=f"save {i}"):
                    write_config(CONFIG)

            check = False

            if CONFIG.agent_fwd_cfg[i].pid == 0:
                check = st.button(f"Run {agent.alias}", type="primary")

            if CONFIG.agent_fwd_cfg[i].pid != 0:
                st.warning(
                    "You must click stop and then re-run tgcf to apply changes in config."
                )
                # check if process is running using pid
                try:
                    os.kill(CONFIG.agent_fwd_cfg[i].pid, signal.SIGCONT)
                except Exception as err:
                    st.code("The process has stopped.")
                    st.code(err)
                    CONFIG.agent_fwd_cfg[i].pid = 0
                    write_config(CONFIG)
                    time.sleep(1)
                    st.experimental_rerun()

                stop = st.button(f"Stop {agent.alias}", type="primary")
                if stop:
                    try:
                        os.kill(CONFIG.agent_fwd_cfg[i].pid, signal.SIGSTOP)
                    except Exception as err:
                        st.code(err)

                        CONFIG.agent_fwd_cfg[i].pid = 0
                        write_config(CONFIG)
                        st.button("Refresh Page")

                    else:
                        termination(i)

            if check:
                with open(f"logs_{i}.txt", "w") as logs:
                    process = subprocess.Popen(
                        ["tgcf", "--loud", mode, str(i)],
                        stdout=logs,
                        stderr=subprocess.STDOUT,
                    )
                CONFIG.agent_fwd_cfg[i].pid = process.pid
                write_config(CONFIG)
                time.sleep(2)

                st.experimental_rerun()

            try:
                lines = st.slider(
                    "Lines of logs to show",
                    min_value=100,
                    max_value=1000,
                    step=100,
                    key=f"slider {i}",
                )
                temp_logs = f"logs_n_lines{i}.txt"
                os.system(f"rm {temp_logs}")
                with open(f"logs_{i}.txt", "r") as file:
                    pass

                os.system(f"tail -n {lines} logs_{i}.txt >> {temp_logs}")
                with open(temp_logs, "r") as file:
                    st.code(file.read())
            except FileNotFoundError as err:
                st.write("No present logs found")
            st.button(f"Load more logs for {agent.alias}")
