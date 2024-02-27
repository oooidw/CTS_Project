#!/bin/bash

clear

echo "Enter the name of the file to download:"
read filename

github_url="https://raw.githubusercontent.com/MilenaValentini/TRM_Dati/main/$filename"

local_path="/opt/my_application/$filename"

echo "Downloading file $filename..."
wget -O "$local_path" "$github_url"

if [ $? -eq 0 ]; then
    echo "File downloaded successfully."

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

    python script.py "$filename"

else
    echo "An error occurred while downloading the file."
fi