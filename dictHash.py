class entry:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.next = None        

class dictHash:
    def __init__(self, tableSize):
        self.tableSize = tableSize
        self.hashTable = [None] * tableSize
        self.numberOfElements = 0

        for i in range (tableSize):
            self.hashTable[i] = entry(0, '')

    def NumberOfAllElements(self):
        return self.numberOfElements


    def Hash(self, id, HashSize):
        return int(id) % HashSize


    def removeItem(self, id):

        index = self.Hash(id,self.tableSize)

        if(self.hashTable[index].id == 0):
        
            print(id + " was not found in the Hash Table\n")
        
        elif(self.hashTable[index].id == id and self.hashTable[index].next == None):
        
            self.hashTable[index].id = 0

            self.numberOfElements -= 1
            print(id + " was removed from the Hash Table\n")
    
        elif(self.hashTable[index].id == id):
        
            self.hashTable[index] = self.hashTable[index].next
            
            self.numberOfElements -= 1
            print(id + " was removed from the Hash Table\n")
        
        else:
        
            P1 = self.hashTable[index].next
            P2 = self.hashTable[index]

            while(P1 != None and P1.id != id):
            
                P2 = P1
                P1 = P1.next
            
            if(P1 == None):
            
                print(id + " was not found in the Hash Table\n")
            
            else:
            
                P1 = P1.next
                P2.next = P1

                self.numberOfElements -= 1
                print(id + " was removed from the Hash Table\n")


    def reHash(self):

        newSize = 2*self.tableSize+1
        ExtendHashTable  = [None] * newSize

        for i in range (newSize):
            ExtendHashTable[i] = entry(0, '')

        for i in range(self.tableSize):
        
            n = self.hashTable[i]
            while(n != None):
            
                tmp = n
                n=n.next

                bucket = ExtendHashTable[self.Hash(tmp.id,newSize)]
                tmp.next = bucket
                bucket = tmp
            
        tableSize = newSize

        HashTable = ExtendHashTable
    

    def searchItem(self, id):

        index = self.Hash(id,self.tableSize)
        foundName = False
        
        Ptr = self.hashTable[index]
        
        while(Ptr != None):
            
            if(Ptr.id == id):
            
                return Ptr
            
            Ptr = Ptr.next
         
        return -1
        
    def addItem(self, id, name):
        index = self.Hash(id,self.tableSize)
        if(self.hashTable[index].id == 0):

            self.hashTable[index].id = id
            self.hashTable[index].name = name
            
        else:
        
            Ptr = self.hashTable[index]

            n = entry(id, name)
            
            while(Ptr.next != None):
            
                Ptr = Ptr.next
            
            Ptr.next = n
        
        if(self.NumberOfAllElements() == int(0.5*self.tableSize)):
        
            self.reHash()
        
        self.numberOfElements += 1
