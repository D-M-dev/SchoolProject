from Components.Utils import datastore

def init_config():
    datastore.init()
    config = datastore.get_store("AppConfig")
    

    if not config.get("NastaveniProgramu"):

        config.set("NastaveniProgramu", "placeholder") 
    
    return config