from modules import datastore

datastore.init()

players = datastore.get_store("GameData")

# set
players.set("Hráč", {"coins": 500, "level": 3})

# get
data = players.get("Hráč")
print(data["coins"])  # 500

# update — bez nutnosti ručního get/set
players.update("Hráč", lambda d: {**d, "coins": d["coins"] + 100})
print(players.get("Hráč")["coins"])  # 600

# remove klíče
players.remove("hráč")