class CacheItem:

    def __init__(self, value):
        self.value = value
        self.hits = 0

    def one_more_hit(self):
        self.hits += 1

    def get_hits(self):
        return self.hits

    def get_value(self):
        return self.value