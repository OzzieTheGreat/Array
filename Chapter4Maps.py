d = {'John': '999-999-9999', 'Jay': '111-111-1111', 'Jane': '000-000-0000'}
print("\nOriginal phonebook dictionary: ", d)

d['Joe'] = '222-222-2222'
d['Doe'] = '777-777-7777'
print("\nAdding Joe and Doe to dictionary: ", d)

print("\nSearching for phone number using a name: ", d['Jay'])

del d['John']
del d['Jane']
print("\nRemoving names John and Jane: ", d)
