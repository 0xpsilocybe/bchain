import hashlib


class Block:
    def __init__(self, index, timestamp, previous, data, nonce=0, hash_sequence=None):
        self._index = int(index)
        self._timestamp = timestamp
        self._previous = previous
        self._data = data
        self._nonce = nonce
        if not hash_sequence:
            hash_sequence = self._hash_me()
        self._hash_sequence = hash_sequence

    @property
    def index(self):
        return self._index

    @property
    def timestamp(self):
        return self._timestamp

    @property
    def previous(self):
        return self._previous

    @property
    def data(self):
        return self._data

    @property
    def nonce(self):
        return self._nonce

    @property
    def hash_sequence(self):
        return self._hash_sequence

    def header_string(self):
        header = str(self.index) + str(self.previous) + self.data + str(self.timestamp) + str(self.nonce)
        return header.encode("utf-8")

    def to_dict(self):
        return {
            'index': self.index,
            'timestamp': self.timestamp,
            'previous': self.previous,
            'data': self.data,
            'nonce': self.nonce,
            'hash_sequence': self.hash_sequence
        }

    def _hash_me(self):
        sha = hashlib.sha256()
        sha.update(self.header_string())
        return sha.hexdigest()

    def __str__(self):
        return "Block<prev: %s, hash: %s>" % (self.previous, self.hash_sequence)

    def __repr__(self):
        return "Block<hash: %s> - %s" % (self.hash_sequence, self.data)
