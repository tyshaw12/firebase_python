import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("CSE 310\Module_One\python-calls-2b1a692f912e.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

collection = db.collection('programmer_details')  # create collection

# Inserting or setting the items

def insert(ref):
    languages = []
    name  = input('What is the name of the person? ')
    age = input("How old are they? ")
    country = input("What country are they from? ")
    languages = input("What programming languages do they know? ")
    collection.document(ref).set({
        'Name': name,
        'Age': age,
        'Country': country,
        'Programming_languages': languages
    })

# Querying the items

def query(ref):
    result = collection.document(ref).get().to_dict()
    print(result)

# Updating the items

def update(ref):
    #query(ref)
    print('Current data: ')
    query(ref)
    print(f'Options: age, country, programming languages, name')
    part = input("What would you like to update? ")
    
    if part.lower() == 'name':
        name  = input('What is the name of the person? ')
        collection.document(ref).update({ # insert document
        'Name': name
    })
    if part.lower() == 'age':
        age  = input('How old is the person? ')
        collection.document(ref).update({ # insert document
        'Age': age
    })
    if part.lower() == 'country':
        country  = input('Where is the person from? ')
        collection.document(ref).update({ # insert document
        'Country': country
    })
    if part.lower() == 'programming languages':
        languages  = input('What programming languages does the person know? ')
        collection.document(ref).update({ # insert document
        'Programming_languages': languages
    })

    print('Updated data: ')
    query(ref)

# Deleting the items

def delete(ref):
    result = collection.document(ref).delete()
    print(result)





#insert('A02')
#query('A01')
#update('A02')
#delete('A02')