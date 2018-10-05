from entity import HashTable

class Set (HashTable.HashTable):

    def __init__(self):
        super(Set, self).__init__()


    def put(self, item):
        if len(self.storage.keys())>= 0 and len(self.storage.keys()) < self.size and super().find(item) is None:
            index = super().seekSlot(item)
            self.storage[str(index)] = item

    def remove(self, item):
        if super().find(item) is not None:
            slot = super().getHashFunction(item)
            del self.storage[str(slot)]

    def intersection(self, set):

        intersect = {}

        for i in self.storage.keys():
            for j in set.storage.keys():
                if self.storage[i] == set.storage[j]:
                    intersect[i] = self.storage[i]
                    continue

        self.storage = intersect
        return self

    def union(self, set):
        for i in set.storage.keys():
            self.put(set.storage[i])
        return self

    def difference(self, set):
        #abcd intersect ecax = bd
        #ecax unoon bd = bdecax
        #bdecax intersect abcd = ex
        # result = bd union ex
        pass

    def issubset(self):
        pass