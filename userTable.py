from array import array

class entry:
    def __init__(self, userId, playerId, rating):
        self.userId = userId
        self.playerId = playerId
        self.rating = rating
        self.next = None

class userTable:
    def __init__(self, tableSize):
        self.tableSize = tableSize
        self.hashTable = [entry(0, 0, 0.0) for x in range(tableSize)]
        self.numberOfElements = 0

    def NumberOfAllElements(self):
        return self.numberOfElements


    def Hash(self, userId, HashSize):
        return userId % HashSize

    def removeItem(self, userId):

        index = self.Hash(userId,self.tableSize)

        if(self.hashTable[index].userId == 0):
        
            print(userId + " was not found in the Hash Table\n")
        
        elif(self.hashTable[index].userId == userId and self.hashTable[index].next == None):
        
            self.hashTable[index].userId = 0

            self.numberOfElements -= 1
            print(userId + " was removed from the Hash Table\n")
    
        elif(self.hashTable[index].userId == userId):
        
            self.hashTable[index] = self.hashTable[index].next
            
            self.numberOfElements -= 1
            print(userId + " was removed from the Hash Table\n")
        
        else:
        
            P1 = self.hashTable[index].next
            P2 = self.hashTable[index]

            while(P1 != None and P1.userId != userId):
            
                P2 = P1
                P1 = P1.next
            
            if(P1 == None):
            
                print(userId + " was not found in the Hash Table\n")
            
            else:
            
                P1 = P1.next
                P2.next = P1

                self.numberOfElements -= 1
                print(userId + " was removed from the Hash Table\n")


    def reHash(self):

        newSize = 2*self.tableSize+1
        ExtendHashTable  = [None] * newSize

        for i in range (newSize):
            ExtendHashTable[i] = entry(0, 0, 0.0)

        for i in range(self.tableSize):
        
            n = self.hashTable[i]
            while(n != None):
            
                tmp = n
                n=n.next

                bucket = ExtendHashTable[self.Hash(tmp.userId,newSize)]
                tmp.next = bucket
                bucket = tmp
            
        tableSize = newSize

        HashTable = ExtendHashTable
    

    def searchItem(self, userId):

        index = self.Hash(userId,self.tableSize)
        foundName = False
        
        Ptr = self.hashTable[index]
        
        while(Ptr != None):
            
            if(Ptr.userId == userId):
            
                return Ptr
            
            Ptr = Ptr.next
         
        return -1
        
    def addItem(self, userId, playerId, rating):
        
        #index = self.Hash(userId,self.tableSize)
        index = userId

        if(self.hashTable[index].userId == 0):

            self.hashTable[index].userId = userId
            self.hashTable[index].playerId = playerId
            self.hashTable[index].rating = rating
        
            #self.numberOfElements += 1
            
        else:
            
            n = entry(userId, playerId, rating)
            
            n.next = self.hashTable[index]
            self.hashTable[index] = n
        
        #if(self.NumberOfAllElements() == int(0.5*self.tableSize)):
        
            #self.reHash()
