# -*- coding: utf-8 -*-
# @Author: JsPako, ItsRommels
# @Webpage: https://github.com/JsPako/AmazonWatch

def generateUUID():
    import uuid
    id = uuid.uuid4()
    return str(id)[:28]


def firstTime():
    f = open("settings.txt", "a+")
    f.close()
    with open("settings.txt", "r+") as file:
        if "setup:'true'" in file.read():
            file.close()
        else:
            file.write("setup:'" + "true" + "'\n")
            file.write("uuid:'" + generateUUID() + "'\n")
            file.write("ip:'" + "'\n")
            file.write("port:'" + "'\n")


def searchFile(num):
    f = open("settings.txt", "r")
    data = []
    for line in f:
        lines = line.split("'")
        data.append(lines[1])
    f.close()
    return(data[num])


def writeFile(item, num):
    with open("settings.txt", "r") as f:
        data = f.readlines()
        f.close()
        with open("settings.txt", "w") as f:
            if num == 1:
                data[num] = "uuid:'" + setup.generateUUID() + "'\n"
                f.writelines(data)
            if num == 2:
                data[num] = "ip:'" + item + "'\n"
                f.writelines(data)
            if num == 3:
                data[num] = "port:'" + item + "'\n"
                f.writelines(data)
            f.close()


def deleteFile(num):
    with open("settings.txt", "r") as f:
        data = f.readlines()
        f.close()
        with open("settings.txt", "w") as f:
            if num == 1:
                data[num] = "uuid:'" + setup.generateUUID() + "'\n"
                f.writelines(data)
            if num == 2:
                data[num] = "ip:'" + "'\n"
                f.writelines(data)
            if num == 3:
                data[num] = "port:'" + "'\n"
                f.writelines(data)
            f.close()
