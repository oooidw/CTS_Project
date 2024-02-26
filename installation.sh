#!/bin/bash

# Name of the application
APP_NAME="my_application"

# Create installation directory
INSTALL_DIR="/opt/$APP_NAME"
mkdir -p "$INSTALL_DIR"

# Copy bash start script and Python files to appropriate path
cp execute.sh "$INSTALL_DIR"
cp script.py "$INSTALL_DIR"

# Assign execution permissions
chmod +x "$INSTALL_DIR/execute.sh"
chmod +x "$INSTALL_DIR/script.py"

# Modify PYTHONPATH and system PATH for single command execution
echo "export PYTHONPATH=\$PYTHONPATH:$INSTALL_DIR" >> ~/.bashrc
echo "export PATH=\$PATH:$INSTALL_DIR" >> ~/.bashrc

# Update current shell session with new configurations
source ~/.bashrc

echo "Installation completed successfully. The application is now ready to be executed with a single command."
