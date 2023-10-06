#!/usr/bin/env python

import html
import json
import subprocess

status = subprocess.run(
    ["todo-tui", "status"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    universal_newlines=True,
    text=True,
    check=True
)
details = subprocess.run(
    ["todo-tui", "details"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    universal_newlines=True,
    text=True,
    check=True
)

data = {}

data['text'] = status.stdout.strip()
data['tooltip'] = html.escape(details.stdout.strip())

print(json.dumps(data))
