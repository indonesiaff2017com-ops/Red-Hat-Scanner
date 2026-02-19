#!/bin/bash
# Red Hat Scanner Installer
# Created by: [Md Sazid]

echo "Installing Red Hat Scanner..."
pkg install python -y
curl -O https://raw.githubusercontent.com/indonesiaff2017com-ops/Red-Hat-Scanner/main/mytool.py
echo "Installation Complete!"
python mytool.py
