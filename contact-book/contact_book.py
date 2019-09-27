class ContactBook:
    def __init__(self,store):
        self.contacts={}
        self.store=store
        self.load()
        

    def add(self,contact):
        self.contacts[contact.email]=contact

    def list(self):
        return self.contacts.values()

    def __getitem__(self,email):
        return self.contact.get(email)


    def save(self):
        self.store.write(self.contacts)

    def load(self):
        try:
            self.contacts=self.store.read()
        except:
            pass