import requests
import os

URL = input("Enter a website to search through content (https://example.com): ")
search = input("Enter keyword to search for: ")
dir = "C:\Windows\Temp"
filedir = "C:\Windows\Temp\site-content.txt"
file = ""

def check_dir(dir):

    if not os.path.exists(dir):
        os.makedirs(dir)
        print(f"Directory '{dir}' created")
    else:
        print(f"Directory '{dir}' Exists")
    # Open new or existing file "site-content.txt" 
    with open(os.path.join(dir, "site-content.txt"), "w") as file:
        file.write("")
    print("Opening site-content.txt...")

def get_site_content(URL, filedir, search):

    page = requests.get(URL, verify=False)
    page_content = page.text
    lines = page_content.splitlines()

    # Write Content into file
    with open(filedir, "w", encoding="utf-8") as file:
        file.write(page_content)

    print(f"searching for '{search}'...")
    page_content = page.text

    for line in lines:
        if search in line:
            print (line)

check_dir(dir)
get_site_content(URL, filedir, search)