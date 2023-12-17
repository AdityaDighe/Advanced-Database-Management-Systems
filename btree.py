# pip install BTrees

import time
from BTrees._IIBTree import IIBTree

btree = IIBTree()

start_time = time.perf_counter()
for i in range(100000):
    btree.update({i:2*i})
end_time = time.perf_counter()

print(f'The insertion time for the BTree is {round((end_time - start_time) * 1000, 3)} milliseconds')

key = int(input('Enter the search key: '))

start_time = time.perf_counter()
if btree.has_key(key):
    print(f'data for search key found : {btree[key]}')
else : 
    print('data for search key not found')
end_time = time.perf_counter()

print(f'The search time for the BTree is {round((end_time - start_time) * 1000, 3)} milliseconds')

