class DisjointSets:
    """
    This class implements the disjoint sets data structure.
    Initially we start off with a list of discrete elements, each element being its own set.

    Supported operations:
    find_set: Returns the set leader of a certain element
    union: Merges the set of which the second element is a part of into the first set.
    """
    def __init__(self, items: list):
        self.set_map = dict(
            [(item, item) for item in items]
        )
        self.sets = dict(
            [(item, {item}) for item in items]
        )

    def find_set(self, item):
        return self.set_map[item]

    def union(self, item1, item2):
        dest_set = self.set_map[item1]
        src_set = self.set_map[item2]
        if src_set != dest_set:
            for item in self.sets[src_set]:
                self.set_map[item] = self.set_map[dest_set]
                self.sets[dest_set].add(item)
            del self.sets[src_set]

    def __len__(self):
        return len(self.sets)