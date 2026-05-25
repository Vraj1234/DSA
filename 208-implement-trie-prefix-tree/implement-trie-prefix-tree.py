class Trie:
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.is_end = False

    def __init__(self):
        self.root = self.TrieNode()
        

    def insert(self, word: str) -> None:
        temp = self.root
        for letter in word:
            if letter not in temp.children:
                temp.children[letter] = self.TrieNode()
            temp = temp.children[letter]
        temp.is_end = True
        

    def search(self, word: str) -> bool:
        temp = self.root
        for letter in word:
            if letter in temp.children:
                temp = temp.children[letter]
            else:
                return False
        return temp.is_end
        
        
    def startsWith(self, prefix: str) -> bool:
        temp = self.root
        for letter in prefix:
            if letter in temp.children:
                temp = temp.children[letter]
            else:
                return False
            
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)