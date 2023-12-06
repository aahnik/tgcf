import os
from typing import Dict, List
from run import package_dir
from streamlit.components.v1 import html
from tgcf.config import write_config


def get_list(string: str):
    # string where each line is one element
    my_list = []
    for line in string.splitlines():
        clean_line = line.strip()
        if clean_line != "":
            my_list.append(clean_line)
    return my_list


def get_string(my_list: List):
    string = ""
    for item in my_list:
        string += f"{item}\n"
    return string


def dict_to_list(dict: Dict):
    my_list = []
    for key, val in dict.items():
        my_list.append(f"{key}: {val}")
    return my_list


def list_to_dict(my_list: List):
    my_dict = {}
    for item in my_list:
        key, val = item.split(":")
        my_dict[key.strip()] = val.strip()
    return my_dict


def apply_theme(st,CONFIG,hidden_container):
    """Apply theme using browser's local storage"""
    if  st.session_state.theme == '☀️':
        theme = 'Light'
        CONFIG.theme = 'light'
    else:
        theme = 'Dark'
        CONFIG.theme = 'dark'
    write_config(CONFIG)
    script = f"<script>localStorage.setItem('stActiveTheme-/-v1', '{{\"name\":\"{theme}\"}}');"
    pages = os.listdir(os.path.join(package_dir,'pages'))
    for page in pages:
        script += f"localStorage.setItem('stActiveTheme-/{page[4:-3]}-v1', '{{\"name\":\"{theme}\"}}');"
    script += 'parent.location.reload()</script>'
    with hidden_container: # prevents the layout from shifting
        html(script,height=0,width=0)


def switch_theme(st,CONFIG):
    """Display the option to change theme (Light/Dark)"""
    with st.sidebar:
        leftpad,content,rightpad = st.columns([0.27,0.46,0.27])
        with content:
            st.radio (
                'Theme:',['☀️','🌒'],
                horizontal=True,
                label_visibility="collapsed",
                index=CONFIG.theme == 'dark',
                on_change=apply_theme,
                key="theme",
                args=[st,CONFIG,leftpad] # or rightpad
            )
        

def hide_st(st):
    dev = os.getenv("DEV")
    if dev:
        return
    hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
