import os
import signal
import subprocess
from collections import deque

import streamlit as st

from tgcf.config import CONFIG, read_config, write_config
from tgcf.web_ui.password import check_password
from tgcf.web_ui.utils import hide_st

CONFIG = read_config()


def termination():
    st.code("process terminated!")
    os.rename("logs.txt", "old_logs.txt")
    with open("old_logs.txt", "r") as f:
        st.download_button(
            "Download last logs", data=f.read(), file_name="tgcf_logs.txt"
        )
    st.warning(
        "Please reload ⟳ the page to see Run button again. Swipe down in mobile or click reload ⟳ icon in desktop. **The Download button will be gone after you reload.**"
    )
    CONFIG = read_config()
    CONFIG.pid = 0
    write_config(CONFIG)


st.set_page_config(
    page_title="Run",
    page_icon="🏃",
)
hide_st(st)
if check_password(st):
    CONFIG.show_forwarded_from = st.checkbox(
        "Show 'Forwarded from'", value=CONFIG.show_forwarded_from
    )
    mode = st.radio("Choose mode", ["live", "past"], index=CONFIG.mode)
    if mode == "past":
        CONFIG.mode = 1
        st.warning(
            "Only User Account can be used in Past mode. Telegram does not allow bot account to go through history of a chat!"
        )
        CONFIG.past.delay = st.slider(
            "Delay in seconds", 0, 100, value=CONFIG.past.delay
        )
    else:
        CONFIG.mode = 0
        CONFIG.live.delete_sync = st.checkbox(
            "Sync when a message is deleted", value=CONFIG.live.delete_sync
        )
        CONFIG.live.delete_on_edit = st.text_input(
            "Delete a message when source edited to", value=CONFIG.live.delete_on_edit
        )

    if st.button("Save"):
        write_config(CONFIG)

    st.markdown("## Logs")

    check = False

    if CONFIG.pid == 0:
        check = st.button("Run")
        st.write(
            "💡 Please ⟳ reload the browser page once after clicking 'Run' to see updates."
        )
        st.warning(
            "After clicking Run: In your mobile swipe down to reload page ⟳, in desktop, click ⟳ icon."
        )

    if CONFIG.pid != 0:
        st.warning(
            "You must click stop and then re-run tgcf to apply changes in config."
        )
        stop = st.button("Stop")
        if stop:
            try:
                os.kill(CONFIG.pid, signal.SIGSTOP)
            except Exception as err:
                st.code(err)

                CONFIG.pid = 0
                write_config(CONFIG)
                st.warning(
                    "Please reload/refresh ⟳ the page. Swipe down in mobile or click reload ⟳ icon in desktop."
                )

            else:
                termination()

    if check:
        process = subprocess.Popen(
            ["tgcf", "--loud", mode], stdout=subprocess.PIPE, stderr=subprocess.STDOUT
        )
        CONFIG.pid = process.pid
        write_config(CONFIG)

        count = 0
        qu = deque(maxlen=3000)
        while True:
            output = process.stdout.readlines(100)
            if process.poll() is not None:
                # show that bot has stopped
                st.code("tgcf has stopped")
                termination()
                break
            if output:
                str_list = [item.decode("UTF8") for item in output]
                qu.extend(str_list)
            with open("logs.txt", "w") as file:
                file.writelines(qu)

    try:
        with open("logs.txt", "r") as file:
            st.code(file.read())
    except FileNotFoundError as err:
        st.write("No present logs found")
    st.button("Load more logs")
