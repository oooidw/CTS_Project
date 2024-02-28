#!/bin/bash

clear

APP_NAME=my_application

INSTALL_DIR=~/$APP_NAME
mkdir $INSTALL_DIR
mkdir $INSTALL_DIR/Images

wget -O "$INSTALL_DIR/execute.sh" "https://raw.githubusercontent.com/oooidw/Esame_Ab_Inf/main/Files/execute.sh" 
wget -O "$INSTALL_DIR/script.py" "https://raw.githubusercontent.com/oooidw/Esame_Ab_Inf/main/Files/script.py"

chmod +x "$INSTALL_DIR/execute.sh"
chmod +x "$INSTALL_DIR/script.py"

echo export "PYTHONPATH=\$PYTHONPATH:$INSTALL_DIR/" >> ~/.bashrc
echo export "PATH=\$PATH:$INSTALL_DIR/" >> ~/.bashrc

source ~/.bashrc

echo "Installation completed successfully. To run the application type 'execute.sh'."
