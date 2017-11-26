from bchain.block import Block


def test_block_defined():
    b = Block(
        index=0,
        data="",
        previous=None,
        timestamp=None
    )

