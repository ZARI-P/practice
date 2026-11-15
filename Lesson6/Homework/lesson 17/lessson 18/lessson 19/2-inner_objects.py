users = {
    "zahrapakmand1390": {
        "firstname": "zahra",
        "lastname": "pakmand",
        "location": "akbarabad"
    },
    "setayeshfeyzi9248": {
        "firstname": "setayesh",
        "lastname": "feyzi",
        "location": "akbarabad"
    }
}

for username, userinfo in users.items():
    print(f"\nuser name: {username}")
    fname = f"{userinfo["firstname"]} {userinfo["lastname"]}"
    location = userinfo["location"]
    
    print(f"\nfull name: {fname}")
    print(f"\nlocation:{location}")