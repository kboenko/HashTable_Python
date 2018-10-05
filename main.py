from entity import HashTable

ht = HashTable.HashTable()

ht.put('Vvvv')
ht.put('EEEEппппыпыыпы')
ht.put('fgfgfg')
ht.put('90')
ht.put('zxc')
ht.put('zxd')
ht.put('zasxcdллл')
ht.put('Звезда по имени солнце')
ht.put('2')

print(ht.storage)


print(ht.find('2'))
print(ht.find('zxd'))
s = ht.find('100500')

if s == None:
    print('Not found')