
import json
import hashlib
import time

class Block:
    def __init__(self, index, messages, previous_hash, timestamp, nonce, hash):
        self.index = index
        self.messages = messages
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.nonce = nonce
        self.hash = hash

def calculate_hash(index, messages, previous_hash, timestamp, nonce):
    block_data = f'{index}{messages}{previous_hash}{timestamp}{nonce}'.encode('utf-8')
    return hashlib.sha256(block_data).hexdigest()

def mine_block(index, messages, previous_hash, timestamp, difficulty=3):
    nonce = 0
    prefix = '0' * difficulty
    while True:
        hash_attempt = calculate_hash(index, messages, previous_hash, timestamp, nonce)
        if hash_attempt.startswith(prefix):
            return nonce, hash_attempt
        nonce += 1

def create_block(index, messages, previous_hash):
    timestamp = time.time()
    nonce, hash_value = mine_block(index, messages, previous_hash, timestamp)
    return Block(index, messages, previous_hash, timestamp, nonce, hash_value)

def update_blockchain(messages_file, blockchain_file):
    try:
        with open(messages_file, 'r') as file:
            current_messages = json.load(file)['messages']

        try:
            with open(blockchain_file, 'r') as file:
                try:
                    blockchain = json.load(file)
                except json.decoder.JSONDecodeError:
                    blockchain = []
        except FileNotFoundError:
            # If the blockchain file doesn't exist, create an empty blockchain
            blockchain = []

        if current_messages and current_messages != blockchain[-1]['messages']:
            # Create a new block with the latest messages
            index = len(blockchain) + 1
            previous_hash = blockchain[-1]['hash'] if blockchain else '0'
            new_block = create_block(index, current_messages, previous_hash)

            # Add the new block to the blockchain
            blockchain.append({
                'index': new_block.index,
                'messages': new_block.messages,
                'previous_hash': new_block.previous_hash,
                'timestamp': new_block.timestamp,
                'nonce': new_block.nonce,
                'hash': new_block.hash
            })

            # Save the updated blockchain to the file
            with open(blockchain_file, 'w') as file:
                json.dump(blockchain, file, indent=2)

    except FileNotFoundError:
        print(f"File not found: {messages_file}")

if __name__ == "__main__":
    messages_file = "messages.json"
    blockchain_file = "blockchain.json"

    while True:
        update_blockchain(messages_file, blockchain_file)
        time.sleep(10)
