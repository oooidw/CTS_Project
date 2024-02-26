#!/bin/bash

clear

APP_NAME="my_application"

INSTALL_DIR="/opt/$APP_NAME"
mkdir -p "$INSTALL_DIR"

wget -O "$INSTALL_DIR/execute.sh" "https://raw.githubusercontent.com/oooidw/Esame_Ab_Inf/main/Files/execute.sh" 
wget -O "$INSTALL_DIR/script.py" "https://raw.githubusercontent.com/oooidw/Esame_Ab_Inf/main/Files/script.py"

chmod +x "$INSTALL_DIR/execute.sh"
chmod +x "$INSTALL_DIR/script.py"

echo "export PYTHONPATH=\$PYTHONPATH:$INSTALL_DIR" >> ~/.bashrc
echo "export PATH=\$PATH:$INSTALL_DIR" >> ~/.bashrc

source ~/.bashrc

echo "Installation completed successfully. The application is now ready to be executed with a single command."
