import sqlite3 as lite

from bchain.block import Block
from bchain.configuration import CONNECTION_STRING


def get_connection():
    return lite.connect(
        CONNECTION_STRING,
        detect_types=lite.PARSE_DECLTYPES | lite.PARSE_COLNAMES
    )


def create_table_blocks():
    with get_connection() as connection:
        connection.execute(
            'CREATE TABLE IF NOT EXISTS blocks('
            '  block_id INTEGER PRIMARY KEY,'
            '  timestamp DATETIME NOT NULL,'
            '  previous TEXT,'
            '  data TEXT,'
            '  nonce INTEGER NOT NULL,'
            '  hash_sequence TEXT UNIQUE NOT NULL)'
        )


def drop_table_blocks():
    with get_connection() as connection:
        connection.execute(
            'DROP TABLE blocks'
        )


def insert_block(block):
    with get_connection() as connection:
        connection.execute(
            'INSERT INTO blocks(block_id, timestamp, previous, data, nonce, hash_sequence) '
            'VALUES(:index, :timestamp, :previous, :data, :nonce, :hash_sequence)',
            block.to_dict()
        )


def insert_many_blocks(blocks):
    blocks_as_dicts = [block.as_dict() for block in blocks]
    with get_connection() as connection:
        connection.executemany(
            'INSERT INTO blocks(block_id, timestamp, previous, data, nonce, hash_sequence) '
            'VALUES(:index, :timestamp, :previous, :data, :nonce, :hash_sequence)',
            blocks_as_dicts
        )


def select_block(index):
    with get_connection() as connection:
        cursor = connection.execute(
            'SELECT block_id, timestamp as "ts [timestamp]", previous, data, nonce, hash_sequence '
            'FROM blocks '
            'WHERE id = ?', index
        )
        row = cursor.fetchone()
        return build_block(row)


def select_all_blocks():
    with get_connection() as connection:
        block_rows = connection.execute(
            'SELECT block_id, timestamp as "ts [timestamp]", previous, data, nonce, hash_sequence '
            'FROM blocks'
        )
        return [build_block(row) for row in block_rows]


def build_block(row):
   return Block(row[0], row[1], row[2], row[3], row[4], row[5])


create_table_blocks()
