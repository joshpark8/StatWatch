import requests
import json
import time

usernames = ["Park-12632", "GolexFan69-2977", "YZNSA3-2687", "EchoFlex-1763"]

def writeSR(role, sr):
    f = open(f"C:/Users/wljos/Documents/Coding/projects/StatWatch/logs/{username}_{role}.log", 'a')
    f.write(str(sr) + "\n")
    print(f"updated {username}_{role}.log")

def checkFile(role):
    try:
        f = open(f"C:/Users/wljos/Documents/Coding/projects/StatWatch/logs/{username}_{role}.log", 'r')
        last_line = f.readlines()[-1:]
        split = str(last_line).split("'")[1].split("\\")[0]
        return int(split)
    except IOError:
        f = open(f"C:/Users/wljos/Documents/Coding/projects/StatWatch/logs/{username}_{role}.log", 'a')    
        return -1

def getSR(username, doPrint):
    r = requests.get(f"https://ow-api.com/v1/stats/pc/us/{username}/profile")
    r = r.json()
    json_formatted = json.dumps(r, indent=2) #

    # r = requests.get(f"https://ow-api.com/v1/stats/pc/us/{username}/complete")
    # r = r.json()
    # json_formatted = json.dumps(r, indent=2) #
    # f = open(f"{username}_complete.log", "a")
    # f.write(json_formatted)

    for arr in r['ratings']:
        role = arr['role']
        sr = arr['level']
        fileExists = checkFile(role)

        if role == 'tank':
            if doPrint == True:
                print("\t" + role + ": " + str(sr))
            if fileExists != sr or fileExists == -1:
                writeSR(role, sr)
                tankRating = sr
        elif role == 'damage':
            if doPrint == True:
                print("\t" + role + ": " + str(sr))
            if fileExists != sr or fileExists == -1:
                writeSR(role, sr)
                damageRating = sr
        elif role == 'support':
            if doPrint == True:
                print("\t" + role + ": " + str(sr))
            if fileExists != sr or fileExists == -1:
                writeSR(role, sr)
                supportRating = sr

if __name__ == "__main__":
    for username in usernames:
        print(username.split("-")[0])
        getSR(username, True)
    while True:
        for username in usernames:
            getSR(username, False)
            time.sleep(60)