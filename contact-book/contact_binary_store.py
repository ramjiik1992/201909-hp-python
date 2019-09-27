import pickle 

class Store:
    def __init__(self, path):
        self.path=path

    def write(self, data):
        with open(self.path,'wb') as file:
            pickle.dump(data,file)

    def read(self):
        with open(self.path,'rb') as file:
            return pickle.load(file)

