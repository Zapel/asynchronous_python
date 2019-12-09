capitals = {}
capitals["Bahamas"] = "Nassau"
capitals["Croatia"] = "Zagreb"

capitals.update({"Lebanon": "Beirut",
                 "Norway": "Oslo",
                 "France": "Paris"})

print(capitals.get("Croatia"))
print(capitals.get("Japan"))
[print(capitals.get(k)) for k in ("Lebanon", "Norway", "Bahamas")]
[print(capitals.__getitem__(k)) for k in ("Lebanon", "Norway", "Bahamas")]

data = {
    "pythonscripts": {
        "url": "https://python-scripts.com/",
        "github": "pythonscripts",
        "fullname": "Python Scripts",
    }
}

print(data)
print("Norway" in capitals)