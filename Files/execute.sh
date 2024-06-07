#!/bin/bash

clear

# Ask the user for the name of the file to download
echo "Enter the name of the file to download:"
read filename

# URL of the file to download
github_url="https://raw.githubusercontent.com/MilenaValentini/TRM_Dati/main/$filename"

# Path where the file will be downloaded
local_path="/opt/my_application/$filename"

# Download the file
echo "Downloading file $filename..."
wget -O "$local_path" "$github_url"

# Check if the file was downloaded successfully
if [ $? -eq 0 ]; then
    echo "File downloaded successfully."

    # Check if the required libraries are installed
    if python3 -c 'import matplotlib' &> /dev/null; then
        echo "matplotlib ok"
    else
        echo "ERROR: matplotlib is not installed."
        exit 1
    fi
    if python3 -c 'import pandas' &> /dev/null; then
        echo "pandas ok"
    else
        echo "ERROR: pandas is not installed."
        exit 1
    fi 
    if python3 -c 'import numpy' &> /dev/null; then
        echo "numpy ok"
    else
        echo "ERROR: numpy is not installed."
        exit 1
    fi 

    # Run the script
    script.py "$filename"

else
    echo "An error occurred while downloading the file."
fi