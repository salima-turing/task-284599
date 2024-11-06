class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.is_end_of_word = True

    def search(self, prefix):
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return 0
            current_node = current_node.children[char]
        return self._count_words(current_node)

    def _count_words(self, node):
        count = 0
        if node.is_end_of_word:
            count += 1
        for child in node.children.values():
            count += self._count_words(child)
        return count

# Example usage:
trie = Trie()
trie.insert("apple")
trie.insert("app")
trie.insert("apricot")
trie.insert("banana")

print(trie.search("app"))  # Output: 2 (matches "app" and "apple")
print(trie.search("apr"))  # Output: 1 (matches "apricot")
print(trie.search("ban"))  # Output: 1 (matches "banana")
print(trie.search("bat"))  # Output: 0 (no matches)
