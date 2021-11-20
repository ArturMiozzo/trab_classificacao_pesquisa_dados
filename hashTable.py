class item:
    def __init__(self, key, id, pos, tag, rating, totalRating, countRating):
        self.key = key
        self.id = id
        self.pos = pos
        self.tag = tag
        self.rating = rating
        self.totalRating = totalRating
        self.countRating = countRating
        self.next = None        

class hash:
    def __init__(self, tableSize):
        self.tableSize = tableSize
        self.hashTable = [None] * tableSize
        self.numberOfElements = 0

        for i in range (tableSize):
            self.hashTable[i] = item('empty', -1,'','',0,0,0)

    def NumberOfAllElements(self):
        return self.numberOfElements


    def Hash(self, key, HashSize):

        hashsum = 0

        for i in range(len(key)):
        
            hashsum = (hashsum * 31) + ord(key[i])
        
        return hashsum % HashSize


    def removeItem(self, key):

        index = self.Hash(key,self.tableSize)

        if(self.hashTable[index].key == "empty"):
        
            print(key + " was not found in the Hash Table\n")
        
        elif(self.hashTable[index].key == key and self.hashTable[index].next == None):
        
            self.hashTable[index].key = "empty"

            self.numberOfElements -= 1
            print(key + " was removed from the Hash Table\n")
    
        elif(self.hashTable[index].key == key):
        
            self.hashTable[index] = self.hashTable[index].next
            
            self.numberOfElements -= 1
            print(key + " was removed from the Hash Table\n")
        
        else:
        
            P1 = self.hashTable[index].next
            P2 = self.hashTable[index]

            while(P1 != None and P1.key != key):
            
                P2 = P1
                P1 = P1.next
            
            if(P1 == None):
            
                print(key + " was not found in the Hash Table\n")
            
            else:
            
                P1 = P1.next
                P2.next = P1

                self.numberOfElements -= 1
                print(key + " was removed from the Hash Table\n")


    def reHash(self):

        newSize = 2*self.tableSize+1
        ExtendHashTable  = [None] * newSize

        for i in range (newSize):
            ExtendHashTable[i] = item('empty', -1, '', '',0,0,0)

        for i in range(self.tableSize):
        
            n = self.hashTable[i]
            while(n != None):
            
                tmp = n
                n=n.next

                bucket = ExtendHashTable[self.Hash(tmp.key,newSize)]
                tmp.next = bucket
                bucket = tmp
            
        tableSize = newSize

        HashTable = ExtendHashTable
    

    def searchItem(self, key):

        index = self.Hash(key,self.tableSize)
        foundName = False
        
        Ptr = self.hashTable[index]

        while(Ptr != None):
    
            if(Ptr.key == key):
            
                return Ptr
            
            Ptr = Ptr.next
         
        return -1
        
    def addItem(self, key, id, pos):

        index = self.Hash(key,self.tableSize)

        if(self.hashTable[index].key == "empty"):
        
            self.hashTable[index].key = key
            self.hashTable[index].id = id
            self.hashTable[index].pos = pos
            
        else:
        
            Ptr = self.hashTable[index]

            n = item(key, id, pos, '',0,0,0)
            
            while(Ptr.next != None):
            
                Ptr = Ptr.next
            
            Ptr.next = n
        
        if(self.NumberOfAllElements() == int(0.5*self.tableSize)):
        
            self.reHash()
        
        self.numberOfElements += 1

    def addTag(self, key, tag):
        Ptr = self.searchItem(key)
        if Ptr != -1:
            if Ptr.tag == '':
                Ptr.tag = tag
            else:
                Ptr.tag = Ptr.tag+', '+tag

    def addRating(self, key, rating):
        Ptr = self.searchItem(key)
        if Ptr != -1:
            Ptr.totalRating = Ptr.totalRating + float(rating)
            Ptr.countRating = Ptr.countRating + 1
            Ptr.rating = Ptr.totalRating / Ptr.countRating

'''
    tableSize = 500
    hashTable = hash(tableSize)
    hashTable.addItem('1')
    hashTable.addItem('2')
    hashTable.addItem('3')
    hashTable.removeItem('2')

    value1 = hashTable.searchItem('1')
    value2 = hashTable.searchItem('2')
'''