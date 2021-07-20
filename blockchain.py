from hashlib import sha256

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
        self.chain.append({
            'hash': block.hash(),
            'prev': block.prev_hash, 
            'number': block.number, 
            'data': block.data, 
            'nonce': block.nonce
            })

    def mine(self, block):
        try:
            block.prev_hash = self.chain[-1].get('hash')
        except IndexError:
            pass
        while True:
            if block.hash()[:self.difficulty] == "0" * self.difficulty:
                self.add(block); break
            else:
                block.nonce += 1


def main():
    #block = Block("trans1", 1)
    #print(block)
    blockchain = Blockchain()
    DB = ["hello world", "what's up", "hello", "bye"]
    num = 0
    for data in DB:
        num +=1
        blockchain.mine(Block(data, num))
    #print(blockchain.chain)
    for block in blockchain.chain:
        print(block)



if __name__ == "__main__":
    main()