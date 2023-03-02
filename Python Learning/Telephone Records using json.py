
book = {}

book['Tom'] = {
    'name': 'Tom',
    'address': 'Khannagar',
    'phone': 9328740983
}

book['Bob'] = {
    'name': 'Bob',
    'address': 'Kolkata',
    'phone': 1919526548
}

import json
s= json.dumps(book)

with open('book.txt','w') as f:
    f.write(s)