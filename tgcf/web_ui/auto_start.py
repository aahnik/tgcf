"""Auto-start utilities for tgcf web UI."""

import os
import signal
import subprocess
import time

import streamlit as st

from tgcf.config import CONFIG, write_config


def auto_start_tgcf():
    """Auto-start tgcf if configured and not already running."""
    if CONFIG.auto_run and CONFIG.pid == 0:
        mode = "live" if CONFIG.mode == 0 else "past"
        try:
            with open("logs.txt", "w") as logs:
                process = subprocess.Popen(
                    ["tgcf", "--loud", mode],
                    stdout=logs,
                    stderr=subprocess.STDOUT,
                )
            CONFIG.pid = process.pid
            write_config(CONFIG)
            st.success(f"Auto-started tgcf in {mode} mode!")
            time.sleep(2)
            return True
        except Exception as err:
            st.error(f"Failed to auto-start tgcf: {err}")
            return False
    return False


def check_and_auto_start():
    """Check if tgcf should auto-start and trigger it."""
    if CONFIG.auto_run:
        if CONFIG.pid == 0:
            st.info("Auto-start is enabled. Starting tgcf...")
            return auto_start_tgcf()
        else:
            st.info("tgcf is already running (auto-start was previously triggered)")
            # Check if process is still alive
            try:
                os.kill(CONFIG.pid, signal.SIGCONT)
                st.success("tgcf is running successfully")
            except Exception:
                st.warning("Previous tgcf process died. Auto-starting...")
                CONFIG.pid = 0
                write_config(CONFIG)
                return auto_start_tgcf()
    return False