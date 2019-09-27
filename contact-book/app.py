from contact import Contact
from contact_book import ContactBook
import sys
import contact_binary_store as binary_store
import contact_json_store as json_store

def add_dummy_contacts(book):
    book.add(Contact('Vivek','vivek@gmail.com','9036084835'))
    book.add(Contact('Sanjay','sanjay@gmail.com','9036084836'))
    book.add(Contact('Shivanshi','shivanshi@gmail.com','9036084837'))

def add_contact(book):
    name=input('name?')
    email=input('email?')
    phone=input('phone?')
    contact=Contact(name,email,phone)
    book.add(contact)


def list_contact(book):
    for contact in book.list():
        print(contact)


def search_contact(book):
    email= input('email?')
    contact=book[email];
    if contact:
        print(contact)
    else:
        print('not found')


def save_contact(book):
    book.save()


def load_contact(book):
    book.load()


def exit_app(book):
    if input('save before exit?')=='y':
        book.save()
    sys.exit(0)

def menu(actions):
    for (key,value) in actions.items():
        print(f'{key}->{value.__name__}')
    while True:
        choice=int(input('choice?'))
        if choice in actions:
            return actions[choice]
        else:
            print('invalid choice')
    

def main():

    stores={
        'db':binary_store,
        'json':json_store
    }

    path=input('store path?')
    
    ext=path.split('.')[-1]
    mod=stores.get(ext,binary_store)

    store=mod.Store(path)
    contactBook=ContactBook(store)
    if (input('add dummy records?')=='YES'):
        add_dummy_contacts(contactBook)

    actions={
        1: add_contact,
        2: list_contact,
        3: search_contact,
        4: save_contact,
        5: load_contact,
        0: exit_app,
    }

    while True:
        action=menu(actions)
        action(contactBook)

main()