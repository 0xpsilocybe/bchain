import hashlib
import datetime as date

from bchain.block import Block
from bchain.configuration import NUM_ZEROS
from bchain.synchronisation import sync
from bchain.dbmanager import insert_block


def create_first_block():
    # index zero and arbitrary previous hash
    return Block(
        index=0,
        timestamp=date.datetime.now(),
        data='First bchain block',
        previous=None,
        nonce=0
    )


def generate_header(index, previous, data, timestamp, nonce):
    header = str(index) + previous + data + str(timestamp) + str(nonce)
    return header.encode("utf-8")


def calculate_hash(index, previous, data, timestamp, nonce):
    header = generate_header(index, previous, data, timestamp, nonce)
    sha = hashlib.sha256()
    sha.update(header)
    return sha.hexdigest()


def mine(last_block):
    index = last_block.index + 1
    timestamp = date.datetime.now()
    data = "I am block #%s" % index
    prev_hash = last_block.hash_sequence
    nonce = 0
    block_hash = calculate_hash(index, prev_hash, data, timestamp, nonce)
    while str(block_hash[0:NUM_ZEROS]) != "0" * NUM_ZEROS:
        nonce += 1
        block_hash = calculate_hash(index, prev_hash, data, timestamp, nonce)
    return Block(index, timestamp, prev_hash, data, nonce)


# create first block and store
insert_block(create_first_block())

if __name__ == "__main__":
    node_blocks = sync()
    previous = node_blocks[-1]
    new_block = mine(previous)
    insert_block(new_block)
