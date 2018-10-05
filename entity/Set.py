from entity import HashTable

class Set (HashTable.HashTable):

    def __init__(self):
        super(Set, self).__init__()


    def put(self, item):
        if len(self.storage.keys())>= 0 and len(self.storage.keys()) < self.size and super().find(item) is None:
            index = super().seekSlot(item)
            self.storage[str(index)] = item

    def remove(self):
        pass

    def intersection(self):
        pass

    def union(self):
        pass

    def difference(self):
        pass

    def issubset(self):
        pass