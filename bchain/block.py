import hashlib
from bchain.configuration import NUM_ZEROS


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

    def is_valid(self):
        """
        Check if the block's hash begins with at least NUM_ZEROS
        """
        self._hash_me()
        return str(self.hash_sequence[0:NUM_ZEROS]) == '0' * NUM_ZEROS

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

    def __eq__(self, other):
        return (self.index == other.index and
                self.timestamp == other.timestamp and
                self.previous == other.previous and
                self.hash_sequence == other.hash_sequence and
                self.data == other.data and
                self.nonce == other.nonce)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return "Block(%s, %s, %s, %s, %s, %s)" %\
               tuple(self.to_dict().values())

    def __repr__(self):
        data_repr = self.data if self.data else "%NO DATA%"
        return "Block<idx: %s hash: %s> - %s" %\
               (self.index, self.hash_sequence, data_repr)
