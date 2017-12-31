
from hashlib import md5


def pass_crack():
    with open("passwords.txt","r") as f:
        password_list = f.read().splitlines()
    for i in password_list:
        m = md5()
        m.update(str(i).encode("utf-8"))
        test_hash = m.hexdigest()
        with open("hash.txt","a") as file:
            file.write(i+":"+test_hash+"\n")
        file.close()


pass_crack()
