class TrieNode:
    
    def __init__(self):
        self.data = [None] * 26
        self.isEnd = False


class Trie:

    def __init__(self):
        self.head = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.head
        for c in word:
            if curr.data[ord(c) - ord('a')] == None:
                curr.data[ord(c) - ord('a')] = TrieNode()
            curr = curr.data[ord(c) - ord('a')]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        curr = self.head
        for c in word:
            if curr.data[ord(c) - ord('a')] == None:
                return False
            curr = curr.data[ord(c) - ord('a')]
        if not curr.isEnd:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        curr = self.head
        for c in prefix:
            if curr.data[ord(c) - ord('a')] == None:
                return False
            curr = curr.data[ord(c) - ord('a')]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)