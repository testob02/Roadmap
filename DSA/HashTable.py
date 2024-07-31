class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for _ in range(self.MAX)] 

    def get_hash(self, string):
        hash = 0
        for char in string:
            hash += ord(char)
        return hash % self.MAX

    def __setitem__(self, key, value):
        key_hash = self.get_hash(key)
        for idx, element in enumerate(self.arr[key_hash]):
            if element[0] == key:
                self.arr[key_hash][idx][1] =  value
                return
        self.arr[key_hash].append([key, value])

    def __getitem__(self, key):
        key_hash = self.get_hash(key)
        for _, element in enumerate(self.arr[key_hash]):
            if element[0] == key:
                return element[1]
        return None

    def __delitem__(self, key):
        hash_key = self.get_hash(key)
        for idx, element in enumerate(self.arr[hash_key]):
            if element[0] == key:
                del self.arr[hash_key][idx]
                return

word_count = HashTable()

with open('poem.txt','r') as f:
    for line in f:
        words = line.split(' ')
        for word in words:
            word = word.replace('\n','')
            if word_count[word]:
               word_count[word] += 1
            else:
               word_count[word] = 1

print(f"'diverged': {word_count['diverged']}")
print(f"'in': {word_count['in']}")
print(f"'I': {word_count['I']}")

