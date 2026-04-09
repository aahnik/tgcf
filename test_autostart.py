#!/usr/bin/env python3
"""Test script to verify auto-start functionality"""

import os
import sys
import json

# Add the current directory to Python path
sys.path.insert(0, '/app')

# Create a test config
test_config = {
    "pid": 0,
    "theme": "light", 
    "auto_run": True,
    "mode": 0,
    "login": {"API_ID": 0, "API_HASH": "", "user_type": 0, "phone_no": 91, "USERNAME": "", "SESSION_STRING": "", "BOT_TOKEN": ""},
    "admins": [],
    "forwards": [],
    "show_forwarded_from": False,
    "live": {"sequential_updates": False, "delete_sync": False, "delete_on_edit": ".deleteMe"},
    "past": {"delay": 0},
    "plugins": {"replace": {"patterns": []}, "filter": {"blacklist": [], "whitelist": []}, "caption": {"header": "", "footer": ""}, "fmt": {}, "mark": {"text": "", "opacity": 0.5, "position": "bottom_right", "size": "medium"}, "ocr": {"lang": "eng"}},
    "bot_messages": {"start": "Hi! I am alive", "bot_help": "For details visit github.com/aahnik/tgcf"}
}

# Write test config
with open('/app/tgcf.config.json', 'w') as f:
    json.dump(test_config, f)

print("Test config created with auto_run=True")

# Test imports
try:
    from tgcf.config import CONFIG, read_config
    print(f"CONFIG loaded: auto_run={CONFIG.auto_run}, pid={CONFIG.pid}")
    
    # Test our auto-start function
    from tgcf.web_ui.run import check_and_auto_start_service
    result = check_and_auto_start_service()
    print(f"Auto-start result: {result}")
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()