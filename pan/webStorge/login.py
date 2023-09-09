import os
import json
from flask import request

def accrUSER():
    user = request.args.get("user")
    passwd = request.args.get("passwd")
    
    userData = json.load(open("webStorge/user.json"))
    
    if user in userData.keys():
        
        if passwd == userData[user]["passwd"]:
            return userData[user]["dir"]
        else:
            return "Password is wrong."

    else:
        return "Username is wrong."
    
    