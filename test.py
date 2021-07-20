import csv
from blockchain import Block
from blockchain import Blockchain

# read data records
with open('./database/records.csv', newline='') as f:
    reader = csv.reader(f)
    database = list(reader)

def main():
    
    blockchain = Blockchain()
    num = 0
    
    for data in database:
        num +=1
        blockchain.mine(Block(data, num))
    
    for block in blockchain.chain:
        print(block)

    # change data of a block manually
    # validate functioin will report False
    blockchain.chain[776].data = "NEW DATA"
    print(blockchain.validate())

    # mine the blockhchain after changing the data
    # validate function will still report False
    blockchain.mine(blockchain.chain[2])
    print(blockchain.validate())

    

if __name__ == "__main__":
    main()