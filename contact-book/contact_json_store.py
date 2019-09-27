import json

class ObjectEncoder(json.JSONEncoder):
    def default(self,o):
        return o.__dict__

class Store:
    def __init__(self, path):
        self.path=path
        #self.encoder=ObjectEncoder()

    def write(self, data):
        with open(self.path,'w') as file:
            json.dump(data,file,cls=ObjectEncoder)

    def read(self):
        with open(self.path,'r') as file:
            return json.load(file)

