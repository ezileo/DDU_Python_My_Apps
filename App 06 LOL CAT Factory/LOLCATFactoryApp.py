# Author: Rohit Gupta
# Date: January 31, 2017
# Version: 1.0

import datetime
import os
import platform
import cat_service
import subprocess


def main():
    print_the_header()
    folder = get_or_create_output_folder()
    print("Found or Created the folder: " + folder)
    # downlaod/ get the image from web browser
    download_cats(folder)
    # display the image
    display_cats(folder)
    print("Hello from Main")


def print_the_header():
    print("-----------------------------------")
    print("         LOL CAT FACTORY APP       ")
    print("-----------------------------------")
    print("")
    user_name = input("Can I have your name please: ")
    print("")
    print("Welcome the the LOL CAT Factory Application {}".format(user_name))
    print("")
    now = datetime.datetime.now()
    print("Current Time is " + (now.strftime("%A, %d %B %Y")))


def get_or_create_output_folder():
    base_folder = os.path.dirname(__file__)
    folder = "cat_pictures"
    full_path = os.path.join(base_folder, folder)

    if not os.path.exists(full_path) or not os.path.exists(full_path):
        print("Creating new directory at {} ".format(full_path))
        os.mkdir(full_path)

    return full_path


def download_cats(folder):
    print("Contactinf server to download cats..........")
    cat_count = 8
    for i in range(1, cat_count + 1):
        name = "lolcat_{}".format(i)
        # print(i, end=", ")
        print("Downloading cat" + name)
        cat_service.get_cat(folder, name)

    print("Done!!!!!!!!!!!")


def display_cats(folder):
    print("Displaying CATs in your OS Window")
    if platform.system() == "Darwin":
        subprocess.call({"open", folder})
    elif platform.system() == "Windows":
        subprocess.call({"explorer", folder})
    elif platform.system() == "Linux":
        subprocess.call({"xdg-open", folder})
    else:
        print("We do not support your operating system which is " + platform.system())


if __name__ == '__main__':
    main()
