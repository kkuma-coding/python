robot = {
    "name": "terminator",
    "임무": {
        1: "나는 존 코너를 보호한다",
        2: "알맞은 옷을 구해 입는다"
    }
}

print(robot["name"])

print ("나는 " + robot["name"] + "이며, "  + robot["임무"][1])
print ("나는 " + robot["name"] + "이며, "  + robot["임무"][2])