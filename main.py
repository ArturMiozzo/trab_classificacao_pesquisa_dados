import csv
import hashTable
import trieTree

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

    isfirst = True
    with open(filename, encoding='utf8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            if isfirst:
                isfirst=False
                continue
            tree.insert(row[1])
            hashTab.addItem(row[1], int(row[0]))
    return tree, hashTab
          

def playerSearch(name, tree, hashTab):
    print('searching player '+name)
    for player in tree.query(name):
        print(player + ' - '+ str(hashTab.searchItem(player).id))
    
def userSearch(user):
    print('searching user '+user)
    
def topSearch(top, position):
    print('searching top '+top + ' from position '+position)
    
def tagsSearch(tags):
    print('searching tags:')
    for tag in tags:
        print(tag)
    
tree, hashTab = readCSV('INF01124_FIFA21\players.csv')

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