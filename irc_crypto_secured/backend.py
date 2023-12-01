import flask as Flask, request
import requests
import  hashlib 

app = Flask(__name__)

message_block = []
raw_chain = []
blockchain = []
parallel_crypto_chain = []

block_count = 0

# Chain initialisation
message_block = {
    "block_number": 0,
    "prev_hash": "",
    "sender": "",
    "channel": "",
    "content": "",
    "nonce": ""
}

def mining_function(message_block):
    hash = "A" * 256
    nonce = 0;
    while hash[0] == "0" && hash[1] == "0":
        message_block["nonce"] = nonce
        sha256_hash = hashlib.sha256()
        sha256_hash.update(input_string.encode('utf-8'))

        hash = 0;
        nonce += 1

app.route('/message_recieve', methods=['GET', 'POST'])
def message_recieve():
    if request.method == "POST":
        if block_count == 0:
            prev_hash = "0" * 256
        else:
            prev_hash = parallel_crypto_chain[block_count - 1]

        message_block["block_number"] = block_count
        message_block["sender"] = request.form["sender"]
        message_block["channel"] = request.form["channel"]
        message_block["content"] = request.form["content"]
        message_block["nonce"] = mining_function(message)
        return message_block.jsonify()

    else:
        return "invaid method"
        
'''
Notes:
    message revieve
    block = {
        "block_number": "block_number",
        "pre_hash": "previous_block_hash",
        "sender": "username",
        "channel": "chanel_name",
        "content": "content_of_message",
        "nonce": "nonce_to_add"
    }
    
'''


