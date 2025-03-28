# SCRIPT MAKE BY YOHANES OKTANIO
# COPYING PY INSTALLER COMPILE TO /usr/bin

# Updated at 29 March 2025

cd ~
git clone https://github.com/yohanesokta/GDPS_sdk.git
cd GDPS_sdk
python3 -m venv ./venv
# bash
source ./venv/bin/activate
pip install -r requerements.txt
pip install pyinstaller
pyinstaller --onefile setup.py
cd dist
mv ./setup /usr/gdps