from entity import HashTable
from entity import Set

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
# print(ht.find('zxd'))
# print(ht.find('100500'))
# print(ht.find('1005000000000'))

st = Set.Set()

print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')

st.put('5')
print('Вставили 5')
st.put('ss5')
print('Вставили ss5')
st.put('5')
print('Вставили другую 5')

print(st.storage)