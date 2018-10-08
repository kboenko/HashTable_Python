#from entity import HashTable
#from entity import Set
import entity.Set as Set
import entity.HashTable as HashTable

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
print('Вставили aaa')
st.put('4a')
print('Вставили другую 5')

print(st.storage)

st.remove('5')
print(st.storage)

s1 = Set.Set()
s1.put('mama')
s1.put('papa')
s1.put('johnny')
s1.put('tree')
s1.put('eye')

s2 = Set.Set()
s2.put('papa')
s2.put('bread')
s2.put('johnny')
s2.put('log')

#print(s1.storage)
#print(s2.storage)

s3 = s1.union(s2)
#s4 = s1.intersection(s2)
#s5 = s1.difference(s2)

print(s3.storage)
#print(s4.storage)
#print(s5.storage)

# s3 = Set.Set()
# s3.put('1')
# s3.put('2')
# s3.put('3')
# s3.put('10')
# s3.put('10001')
#
#
# s4 = Set.Set()
# s4.put('3')
# s4.put('10001')
#
# print(s4.issubset(s3))