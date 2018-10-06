from entity import HashTable

class Set (HashTable.HashTable):

    def __init__(self):
        super(Set, self).__init__()


    def put(self, item):
        if len(self.storage.keys())>= 0 and len(self.storage.keys()) < self.size and self.find(item) is None:
            index = self.seekSlot(item)
            self.storage[str(index)] = item

    def remove(self, item):
        if super().find(item) is not None:
            slot = self.getHashFunction(item)
            del self.storage[str(slot)]

    def intersection(self, set):

        intersect = Set()

        for i in self.storage.keys():
            if set.find(self.storage[i]) is not None:
                intersect.storage[i] = self.storage[i]
        return intersect

    def union(self, set):
        for i in set.storage.keys():
            self.put(set.storage[i])
        return self

    def difference(self, set):

        diff = Set()

        for i in self.storage.keys():
            if set.find(self.storage[i]) is None:
                diff.storage[i] = self.storage[i]
        return diff

    def issubset(self, set):
        return self.storage.items() == self.intersection(set).storage.items()