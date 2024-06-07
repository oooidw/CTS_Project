#!/bin/bash

clear

# Name of the application
APP_NAME="my_application"

# Creating an installation directory
INSTALL_DIR="/opt/$APP_NAME"
mkdir -p "$INSTALL_DIR/Images"

# Downloading the necessary files
wget -O "$INSTALL_DIR/execute.sh" "https://raw.githubusercontent.com/oooidw/Esame_Ab_Inf/main/Files/execute.sh" 
wget -O "$INSTALL_DIR/script.py" "https://raw.githubusercontent.com/oooidw/Esame_Ab_Inf/main/Files/script.py"

# Setting the permissions
chmod +x "$INSTALL_DIR/execute.sh"
chmod +x "$INSTALL_DIR/script.py"

# Setting the environment variables
echo "export PYTHONPATH=\$PYTHONPATH:$INSTALL_DIR" >> ~/.bashrc
echo "export PATH=\$PATH:$INSTALL_DIR" >> ~/.bashrc

# Reload the .bashrc file
source ~/.bashrc

# Displaying the final message
echo "Installation completed successfully. To run the application type 'execute.sh'."
