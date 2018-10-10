from entity import HashTable
from entity import CacheItem

class Cache(HashTable.HashTable):

    def __init__(self):
        super(Cache, self).__init__()

    def hit_item(self, item):
        for i in self.storage.keys():
            if self.storage[i].value == item:
                self.storage[i].one_more_hit()

    def find(self, item):
            m = str(self.getHashFunction(item))

            if self.storage and self.storage.get(m) and self.storage.get(m).value == item:
                self.hit_item(item)
                return self.getHashFunction(item)
            elif self.storage and self.storage.get(m) and self.storage.get(m).value != item:
                count = 0
                slot = self.getHashFunction(item)

                try:
                    while True:
                        slot = self.doSteps(slot, count)
                        count += 1
                        if str(slot) in self.storage.keys() and self.storage[str(slot)].value == item:
                            break
                        elif not str(slot) in self.storage.keys() or (
                                self.storage[str(slot)].value != item and count == self.size):
                            return None
                    self.hit_item(item)
                    return slot
                except Exception as e:
                    print('BOOM! ' + str(e))
            else:
                return None

    def put(self, item):
        super().put(CacheItem.CacheItem(item))

    def print(self):
        for i in self.storage:
            print('Элемент: ' + self.storage[i].value + ', количество обращений: ' + str(self.storage[i].hits))