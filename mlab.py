import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds153869.mlab.com:53869/earthhero

host = "ds153869.mlab.com"
port = 53869
db_name = "earthhero"
user_name = "admin"
password = "admin"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
