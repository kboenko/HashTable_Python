from entity import HashTable
from entity import CacheItem

class Cache(HashTable.HashTable):

    def __init__(self):
        super(Cache, self).__init__()

    def find(self, item):
            m = str(self.getHashFunction(item))

            if self.storage and self.storage.get(m) and self.storage.get(m).value == item:
                return self.getHashFunction(item)
            elif self.storage and self.storage.get(m) and self.storage.get(m).value != item:
                count = 0
                count1 = 0
                slot = self.getHashFunction(item)

                try:
                    while True:
                        slot = self.doSteps(slot, count)
                        count += 1
                        if str(slot) in self.storage.keys() and self.storage[str(slot)].value == item:
                            break
                        elif not str(slot) in self.storage.keys() or (
                                self.storage[str(slot)].value != item and count1 == self.size):
                            return None
                    return slot
                except Exception as e:
                    print('BOOM! ' + e)
            else:
                return None

    # def put(self, item):
    #     pass