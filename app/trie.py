import functools


def load_trie(records):
    trie = Trie()
    for record in records:
        trie.insert(record)
    return trie


class Trie(object):
    def __init__(self):
        self.children = {}
        self.leaf = False

    def __add(self, char):
        self.children[char] = Trie()

    def insert(self, word):
        node = self
        for char in word:
            if char not in node.children:
                node.__add(char)
            node = node.children[char]
        node.leaf = True

    def __suffixes(self, prefix):
        results = set()
        if self.leaf:
            results.add(prefix)
        if not self.children:
            return results
        return functools.reduce(lambda a, b: a | b, [node.__suffixes(prefix + char) for (char, node) in self.children.items()]) | results

    def search(self, prefix):
        node = self
        for char in prefix:
            if char not in node.children:
                return set()
            node = node.children[char]
        return list(node.__suffixes(prefix))
