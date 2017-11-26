from flask import Flask, redirect, url_for
from datetime import datetime
import json

from bchain.synchronisation import sync
from bchain.dbmanager import insert_block
from bchain.mine import mine


class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        return json.JSONEncoder.default(self, o)


node = Flask(__name__)
node_blocks = sync()


@node.route("/blockchain.json", methods=["GET"])
def blockchain():
    global node_blocks
    node_blocks = sync()
    blocks = [block.to_dict() for block in node_blocks]
    return json.dumps(blocks, cls=DateTimeEncoder)


@node.route("/mine", methods=["GET"])
def mine_block():
    global node_blocks
    node_blocks = sync()
    previous = node_blocks[-1]
    new_block = mine(previous)
    insert_block(new_block)
    return redirect(url_for("blockchain"), code=302)


if __name__ == '__main__':
    node.run()
