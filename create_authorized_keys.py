import os

user_keys = os.listdir("./users")
open('authorized_keys', 'r+').truncate(0)
for key in user_keys:
    with open("./users/{}".format(key), "r") as file_1, open("authorized_keys", "a") as file_2:
        for line in file_1:
            if "ssh-rsa" in line:
                file_2.write(line)
