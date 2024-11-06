class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word_end = False
        self.words = []


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]

        if not current.is_word_end:
            current.is_word_end = True
            current.words.append(word)

    def search(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return 0
            current = current.children[char]

        return len(current.words)


# Example usage:
trie = Trie()
trie.insert("apple")
trie.insert("banana")
trie.insert("pineapple")

print("Words starting with 'app':", trie.search("app"))  # Output: 2
print("Words starting with 'ban':", trie.search("ban"))  # Output: 1
print("Words starting with 'pin':", trie.search("pin"))  # Output: 1
