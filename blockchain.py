from hashlib import sha256
import csv

# read data records
with open('./database/4records.csv', newline='') as f:
    reader = csv.reader(f)
    database = list(reader)

def updatehash(*args):
    hashing_text = ""
    h = sha256()
    for arg in args:
        hashing_text += str(arg)
    h.update(hashing_text.encode('utf-8'))
    return h.hexdigest() 

class Block():
    data = None
    hash = None
    nonce = 0
    prev_hash = "0" * 64 #initial block hash, 64 zero's because of sha256 hash length

    def __init__(self, data, number = 0):
        self.data = data
        self.number = number

    def hash(self):
        return updatehash(
            self.prev_hash, 
            self.number, 
            self.data, 
            self.nonce
        )
    
    #print out block
    def __str__(self):
        return str("Block no. %s\nHash %s\nPrev Hash %s\nData %s\nNonce %s" 
                    %(
                        self.number, 
                        self.hash(), 
                        self.prev_hash, 
                        self.data, 
                        self.nonce)
                    )

class Blockchain():
    
    difficulty = 4

    def __init__(self, chain = []):
        self.chain = chain
    
    def add(self, block):
        self.chain.append(block)

    def remove(self, block):
        self.chain.remove(block)

    def mine(self, block):
        try:
            block.prev_hash = self.chain[-1].hash()
        except IndexError:
            pass
        while True:
            if block.hash()[:self.difficulty] == "0" * self.difficulty:
                self.add(block); break
            else:
                block.nonce += 1

    # Validation:
    #   1.each block hash should start with the number of zeros as defined by difficulty
    #   2.blocks should be connected 
    def validate(self):
        for i in range(1, len(self.chain)):
            _prev = self.chain[i].prev_hash  
            _curr = self.chain[i-1].hash()
            if _prev != _curr or _curr[:self.difficulty] != '0' * self.difficulty:
                return False
        return True
        


def main():
    
    blockchain = Blockchain()
    num = 0
    
    for data in database:
        num +=1
        blockchain.mine(Block(data, num))
    
    for block in blockchain.chain:
        print(block)

    print(blockchain.validate())

if __name__ == "__main__":
    main()