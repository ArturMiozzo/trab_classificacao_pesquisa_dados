import csv
import hashTable
import trieTree
import dictHash

class player:
    def __init__(self, key):
        self.key = key
        self.next = None
        self.sofifaID = 0
        self.name = ''
        self.positions = ''
        self.rating = 0.0
        self.globalRating = 0.0
        self.count = 0
        

def readCSV(filename):
    tree = trieTree.Trie()
    hashTab = hashTable.hash(500)
    dictionary = dictHash.dictHash(500)

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

def playerSearch(name, tree, hashTab):
    print('searching player '+name)
    for player in tree.query(name):
        item = hashTab.searchItem(player)
        if item != -1:
            print(player + ' - '+ str(item.id) + ' - ' + item.pos)
    
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
            print(player + ' - '+ str(item.id) + ' - ' + item.pos)
            count = count+1
    
def tagsSearch(tags):
    for tag in tags:
        if (tag[0] != "'") or (tag[len(tag)-1] != "'"):
            print('Encontrada tag em formato errado!')
            return
    print('searching tags:')
    for tag in tags:
        print(tag)

tree, hashTab, dictionary = readCSV('INF01124_FIFA21\players.csv')

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
        tags = command[5::].split(' ')
        tagsSearch(tags)