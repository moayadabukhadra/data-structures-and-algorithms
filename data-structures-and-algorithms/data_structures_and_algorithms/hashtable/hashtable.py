

class HashaTable(object):
    def __init__(self, size = 1024):
    
        self.size = size
        self.map = [None]*size

    def hash(self, key):

        sum_of_ascii = 0
        for ch in key:
            ch_ascii = ord(ch) 
            sum_of_ascii+=ch_ascii
        hashed_key = (sum_of_ascii*19)%self.size

        return hashed_key

    def set(self, key, value):

        idx = self.hash(key)
        if not self.map[idx]:
            self.map[idx] = [[key, value]]
        else:
            self.map[idx].append([key, value])



    def contains(self,key):
        idx=self.hash(key)
        if self.map[idx]:
            return True
        
        else :
            return False


    def get(self, key):
        idx = self.hash(key)
        if self.map[idx]:
            return self.map[idx][0][1]
        else:
            return self.map[idx]
        
    
    def keys(self):
        keys_list=[]
        for key in self.map:
            if key is not None:
                keys_list.append(key[0][0])
        return keys_list


if __name__ == "__main__":
    hashtable = HashaTable()
    hashtable.set("cat", "AWS")
    hashtable.set("act", "Azure")
    hashtable.set("could", "Rainy")
    hashtable.set("name", "Python")
    hashtable.set("cat", "moayad")
    print(hashtable.contains("cat"))
    print(hashtable.get("cat"))
    for i in hashtable.map:
        print(i)
    print(hashtable.keys())