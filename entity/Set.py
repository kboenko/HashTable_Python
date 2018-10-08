from entity import HashTable

class Set (HashTable.HashTable):

    def __init__(self):
        super(Set, self).__init__()


    def put(self, item):
        if self.find(item) is None:
            index = self.seekSlot(item)
            self.storage[str(index)] = item

    def remove(self, item):
        if super().find(item) is not None:
            slot = self.getHashFunction(item)
            del self.storage[str(slot)]

    def intersection(self, set):

        intersect = Set()
        intersect.storage = {key: self.storage[key] for key in self.storage.keys() if
                             set.find(self.storage[key]) is not None}
        return intersect

    def union(self, set):
        un = Set()
        for i in set.storage.keys():
            un.put(set.storage[i])
        for j in self.storage.keys():
            un.put(self.storage[j])
        return un

    def difference(self, set):
        diff = Set()
        diff.storage = {key: self.storage[key] for key in self.storage.keys() if
                             set.find(self.storage[key]) is None}
        return diff

    def issubset(self, set):
        return self.storage.items() == self.intersection(set).storage.items()