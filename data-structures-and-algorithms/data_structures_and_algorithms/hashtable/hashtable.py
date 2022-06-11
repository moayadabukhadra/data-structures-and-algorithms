

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


def repeated_word(string):

    if type(string)!= type(""):
        raise Exception("the input should be a string")
    hashtable=HashaTable()
    words=string.lower().replace(","," ").split()

    if len(words)==1:
        return string
    
    for word in words:
        hashtable.set(word,"temp_value")
        for i in hashtable.map:
            if i and  len(i)>=2:
                print(i[0][0])

                return i[0][0]


def left_join(Synonyms,Antonyms):
    if type(Synonyms) and type(Antonyms) != type([]):
        raise Exception("the input should be 2 hashmaps")

    if Synonyms== [None]*1024:
        raise(Exception("the Synonyms hashmap is empty"))

    new_map=[]
    for i in  range(0,len(Synonyms)):
        if Synonyms[i] and Antonyms[i]:
            new_map.append([Synonyms[i][0][0],Synonyms[i][0][1],Antonyms[i][0][1]])
                
        elif Synonyms[i] and not Antonyms[i]:
            new_map.append([Synonyms[i][0][0],Synonyms[i][0][1],None])

    return new_map


def most_common_word(string):
    max=0
    most_common=None
    if type(string)!= type(""):
        raise Exception("the input should be a string")
    hashtable=HashaTable()
    words=string.lower().split()
    
    if len(words)==1:
        return string
        
    for word in words:
        hashtable.set(word,"temp_value")
    for i in hashtable.map:
        if i is not None:
            if len(i)>max:
                max=len(i)
                most_common=i[0][0]
    return most_common

def unique_characters(string):
    string=string.replace(" ","")
    if type(string)!= type(""):
        raise Exception("the input should be a string")
    hashtable=HashaTable()
    for ch in string:
        hashtable.set(ch,"temp_value")
        i=hashtable.hash(ch)
        if len(hashtable.map[i])>1:
            return False
    return True


    





    
        
  

if __name__ == "__main__":
    # hashtable = HashaTable()
    # hashtable.set("diligent", "employed")
    # hashtable.set("fond", "enamored")
    # hashtable.set("guide", "usher")
    # hashtable.set("outfit", "garb")
    # hashtable.set("wrath", "anger")

    # hashtable2=HashaTable()
    # hashtable2.set("diligent", "idle")
    # hashtable2.set("fond", "averse")
    # hashtable2.set("guide", "follow")
    # hashtable2.set("flow", "jam")  
    # hashtable2.set("wrath", "delight")
    # temphash=HashaTable()
    # print(left_join(hashtable.map,hashtable2.map))
    # print(most_common_word("No. Try not. Do or do not. There is no try."))

    print(unique_characters("I love cats	"))


    
    