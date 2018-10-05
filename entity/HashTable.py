from math import fabs
import sys

class HashTable:

    def __init__(self):
        self.size = 19
        self.step = 3
        self.storage = {}

    def getHashFunction(self, item):
        hash = 0
        for i in range (len(item)):
            hash = (hash << 5) - hash + ord(item[i])
        return fabs(int(hash % self.size))

    def seekSlot(self, item):
            slot = self.getHashFunction(item)
            count = 0

            if str(slot) in self.storage.keys():
                while True:
                    slot = self.doSteps(slot, count)
                    if not (str(slot) in self.storage.keys()):
                        break
            return slot

    def doSteps(self, slot, count):
        slot += self.step
        count += 1

        if slot > self.size:
            slot -= self.size

        if count == self.size:
            return None

        return slot

    def put(self, item):
        if len(self.storage.keys()) >= 0 and len(self.storage.keys()) < self.size:
            index = self.seekSlot(item)
            self.storage[str(index)] = item

    def find(self, item):
        if self.storage[str(self.getHashFunction(item))] and self.storage[str(self.getHashFunction(item))] == item:
            return self.getHashFunction(item)
        elif self.storage[str(self.getHashFunction(item))] and self.storage[str(self.getHashFunction(item))] != item:

                count = 0
                count1 = 0
                slot = self.getHashFunction(item)

                try:
                    while True:
                        slot = self.doSteps(slot, count)
                        count += 1
                        if str(slot) in self.storage.keys() and self.storage[str(slot)] == item:
                            break
                        elif not str(slot) in self.storage.keys() or (self.storage[str(slot)] != item and count1 == self.size):
                            return None
                    return slot
                except Exception as e:
                    print('BOOM! ' + e)
                    print(sys.exc_value)
                    print(sys.exc_traceback)
        else:
            return None