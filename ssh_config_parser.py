import os
import re

def parse_ssh_config():
    config_path = os.path.expanduser("/Users/vasu.yadav/.ssh/config")
    hosts = []
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line.lower().startswith("host ") and not line.lower().startswith("host *"):
                    parts = line.split()
                    if len(parts) > 1:
                        hosts.append(parts[1])
    return hosts