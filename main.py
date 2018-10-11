#from entity import HashTable
#from entity import Set
import entity.Set as Set
import entity.HashTable as HashTable
import entity.Cache as Cache
import entity.CacheItem as cash_item

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

cache = Cache.Cache()

cache.put(cash_item.CacheItem('5'))
cache.put(cash_item.CacheItem('dd'))
cache.put(cash_item.CacheItem('99'))
cache.put(cash_item.CacheItem('88'))
cache.put(cash_item.CacheItem('a'))
cache.put(cash_item.CacheItem('bb'))
cache.put(cash_item.CacheItem('ccc'))
cache.put(cash_item.CacheItem('dddd'))
cache.put(cash_item.CacheItem('ee1'))
cache.put(cash_item.CacheItem('fff4'))
cache.put(cash_item.CacheItem('g4444'))
cache.put(cash_item.CacheItem('hh77'))
cache.put(cash_item.CacheItem('i12'))
cache.put(cash_item.CacheItem('j767676'))
cache.put(cash_item.CacheItem('kkk9'))
cache.put(cash_item.CacheItem('ll345'))
cache.put(cash_item.CacheItem('m6655'))
cache.put(cash_item.CacheItem('n34'))
cache.put(cash_item.CacheItem('o369'))
cache.put(cash_item.CacheItem('ppppppppppppp'))
cache.put(cash_item.CacheItem('ppppppppppppp555'))
cache.put(cash_item.CacheItem('ppppppppppppp8888'))
cache.put(cash_item.CacheItem('ppppppppppppp0000'))
cache.put(cash_item.CacheItem('ppppppppppppp3333'))

print(cache.storage)

cache.print()

print(cache.find('dd'))


print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
cache.print()

