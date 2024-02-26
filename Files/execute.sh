#!/bin/bash

clear

echo "Enter the name of the file to download:"
read filename

github_url="https://raw.githubusercontent.com/MilenaValentini/TRM_Dati/main/$filename"

local_path="./$filename"

echo "Downloading file $filename..."
wget -O "$local_path" "$github_url"

if [ $? -eq 0 ]; then
    echo "File downloaded successfully."
    mkdir -p "/Images"
    script.py "$filename"
else
    echo "An error occurred while downloading the file."
fi