from configparser import ConfigParser

confi = ConfigParser()
confi.read("config/application.conf")


class Service:
    host = confi["service"]["host"]
    port = int(confi["service"]["port"])
    uri = confi["Mongo"]["Uri"]
    database = confi["Mongo"]["database_name"]
    collection = confi["Mongo"]["collection_name"]