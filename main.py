import csv
import hashTable
import trieTree
import dictHash
import userTable
import time

class entry:
    def __init__(self, userId, playerId, rating):
        self.userId = userId
        self.playerId = playerId
        self.rating = rating

def readCSV(filename):
    tree = trieTree.Trie()
    hashTab = hashTable.hash(24631)
    dictionary = dictHash.dictHash(24631)

    isfirst = True
    with open(filename, encoding='utf8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            if isfirst:
                isfirst=False
                continue
            tree.insert(row[1])
            hashTab.addItem(row[1], int(row[0]), row[2])
            dictionary.addItem(int(row[0]),row[1])
    return tree, hashTab, dictionary

def addTagsFromCSV(hashTab, dictionary, filename):
    isfirst = True
    with open(filename, encoding='utf8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            if isfirst:
                isfirst=False
                continue
            searched = dictionary.searchItem(int(row[1]))
            if searched != -1:
                hashTab.addTag(searched.name, row[2])
    return hashTab

def addRatingsFromCSV(hashTab, dictionary, filename):
        
    #tem aproximadamente 138500 usuarios, entao deixei a lista com 140000 pra ficar maior que a quantidade e não rolar colisão

    #implementação com lista do python
    usersList = [[] for x in range(140000)]
    
    #implementação com tabela hash e lista encadeada do python
    usersTab = userTable.userTable(140000)    

    lastSearch = -1
    lastID = -1
    
    lastTotalRating = 0
    LastCountRating = 0

    with open(filename, encoding='utf8') as csvfile:
        
        spamreader = csv.reader(csvfile, delimiter=',')
        next(spamreader, None)
        
        for row in spamreader:
            
            #adicionando a lista do python um objeto entry
            usersList[int(row[0])].append(entry(int(row[0]), int(row[1]), float(row[2])))

            #adicionando a tabela hash
            usersTab.addItem(int(row[0]), int(row[1]), float(row[2]))
            
            if lastID != int(row[1]):
                lastID = int(row[1])
                searched = dictionary.searchItem(lastID)

                if lastSearch != -1:
                    hashTab.addRating(lastSearch.name, LastRating)

                lastTotalRating = float(row[2])
                LastCountRating = 1
                lastSearch = searched

            else:
                lastTotalRating = lastTotalRating + float(row[2])
                LastCountRating = LastCountRating + 1


    hashTab.addRating(lastSearch.name, LastRating)
    return hashTab

def playerSearch(name, tree, hashTab):
    print('searching player '+name)
    for player in tree.query(name):
        item = hashTab.searchItem(player)
        if item != -1:
            print(player + ' - '+ str(item.id) + ' - ' + item.pos + ' - ' + str(item.rating) + ' - ' + str(item.countRating))
    
def userSearch(user):
    print('searching user '+user)
    
def topSearch(top, position):
    #tratamento da entrada
    if (position[0] != "'") or (position[len(position)-1] != "'"):
        print('Formato errado!')
        return
    position = position[1:len(position)-1]

    print('searching top '+top + ' from position '+position)

    #procura na tabela hash
    count = 0
    for player in tree.query(''):
        if count == int(top):
            break
        item = hashTab.searchItem(player)
        if (item != -1) and (position in item.pos):
            print(player + ' - '+ str(item.id) + ' - ' + item.pos + ' - ' + str(item.rating) + ' - ' + str(item.countRating))
            count = count+1
    
def tagsSearch(tags):
    #tratamento da entrada
    tags_ = []
    for tag in tags:
        if (tag[0] == "'"):
            tag_ = tag[1::]
        else:
            tag_ = tag

        if (tag_[len(tag_)-1] == "'"):
            tag_ = tag_[:len(tag_)-1:]
        tags_.append(tag_)

    print('searching tags:')
    for tag in tags_:
        print(tag)

    #procura na tabela hash
    for player in tree.query(''):
        bContains = True
        item = hashTab.searchItem(player)

        if (item != -1):
            for tag in tags_:
                bContains = bContains and (tag in item.tag)

            if bContains:
                print(player + ' - '+ str(item.id) + ' - ' + item.pos + ' - ' + str(item.rating) + ' - ' + str(item.countRating))


start = time.time()
tree, hashTab, dictionary = readCSV('INF01124_FIFA21\players.csv')
endPlayers = time.time()
print("Players table time: "+str(endPlayers - start))

hashTab = addRatingsFromCSV(hashTab, dictionary,'INF01124_FIFA21\\rating.csv')
endRatings = time.time()
print("Ratings table time: "+str(endRatings - endPlayers))
print("Total time: "+str(endRatings - start))

hashTab = addTagsFromCSV(hashTab, dictionary,'INF01124_FIFA21\\tags.csv')
endTags = time.time()
print("Tags table time: "+str(endTags - endRatings))
print("Total time: "+str(endTags - start))

while(True):

    command = input('$ ')

    if(command.startswith('player')):
        playerSearch(command[7::], tree, hashTab)
        
    if(command.startswith('user')):
        userSearch(command[5::])
        
    if(command.startswith('top')):
        top, position = command[3::].split(' ')
        topSearch(top, position)

    if(command.startswith('tags')):
        tags = command[5::].split("' ")
        tagsSearch(tags)