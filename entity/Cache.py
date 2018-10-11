from entity import HashTable
from math import fabs

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

    def remove(self, item):
        if self.find(item) is not None:
            slot = self.getHashFunction(item)
            del self.storage[str(slot)]

    def seekSlot(self, item):
            slot = self.getHashFunction(item)
            count = 0

            if str(slot) in self.storage.keys():
                while True:
                    slot = self.doSteps(slot, count)
                    if not (str(slot) in self.storage.keys()):
                        break
                    else:
                        self.hit_item(item)
            return slot

    def put(self, item):
        if len(self.storage.keys()) and len(self.storage.keys()) == self.size:
            min_hits = min(set([item.hits for item in self.storage.values()]))
            items_with_min_hits = [item.value for item in self.storage.values() if item.hits == min_hits]
            self.remove(items_with_min_hits[0])

        if len(self.storage.keys()) >= 0 and len(self.storage.keys()) < self.size:
            index = self.seekSlot(item.value)
            self.storage[str(index)] = item

    def print(self):
        for i in self.storage:
            print('Элемент: ' + self.storage[i].value + ', количество обращений: ' + str(self.storage[i].hits))