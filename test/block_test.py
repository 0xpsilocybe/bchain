"""
Test methods for Block class.
"""

import pytest
from bchain.block import Block


def test_block_is_defined():
    _ = Block(
        index=0,
        data="",
        previous=None,
        timestamp=None
    )


def test_block_throws_when_index_is_not_of_integer_type():
    with pytest.raises(ValueError):
        _ = Block(
            index="string index",
            data="",
            previous=None,
            timestamp=None
        )


def test_block_hash_calculated_correctly():
    block = Block(
        index=0,
        nonce=631412,
        timestamp=1508895381,
        data="First block data",
        previous=""
    )
    assert block.hash_sequence == "000002f9c703dc80340c08462a0d6acdac9d0e10eb4190f6e57af6bb0850d03c"


def test_block_with_valid_data_is_valid():
    block = Block(
        index=1,
        nonce=1225518,
        timestamp=1508895386,
        hash_sequence="00000c575050241e0a4df1acd7e6fb90cc1f599e2cc2908ec8225e10915006cc",
        previous="000002f9c703dc80340c08462a0d6acdac9d0e10eb4190f6e57af6bb0850d03c",
        data="Block #1"
    )
    assert block.is_valid()


def test_block_with_invalid_data_is_invalid():
    block = Block(
        index=11,
        nonce=13,
        timestamp=1507855352,
        # Invalid hash sequence
        hash_sequence="10000c575050241e0a4df1acd7e6fb90cc1f599e2cc2908ec8225e10915006cc",
        previous="000002f9c703dc80340c08462a0d6acdac9d0e10eb4190f6e57af6bb0850d03c",
        data="Block #1"
    )
    assert not block.is_valid()


def test_blocks_with_same_properties_are_equal():
    block = Block(index=0, timestamp=1500000000, data="BLOCK", previous="")
    block_copy = Block(index=0, timestamp=1500000000, data="BLOCK", previous="")
    assert block == block_copy


def test_blocks_with_different_index_are_not_equal():
    block = Block(index=0, timestamp=1500000000, data="BLOCK", previous="")
    block_other = Block(index=1, timestamp=1500000000, data="BLOCK", previous="")
    assert block != block_other


def test_blocks_with_different_previous_hash_are_not_equal():
    block = Block(index=0, timestamp=1500000000, data="BLOCK", previous="")
    block_other = Block(index=0, timestamp=1611111111, data="BLOCK", previous="")
    assert block != block_other


def test_blocks_with_different_data_are_not_equal():
    block = Block(index=0, timestamp=1500000000, data="BLOCK", previous="")
    block_other = Block(index=0, timestamp=1500000000, data="DIFFERENT DATA", previous="")
    assert block != block_other


def test_blocks_with_different_timestamp_are_not_equal():
    block = Block(index=0, timestamp=1500000000, data="BLOCK",
                  previous="10000c575050241e0a4df1acd7e6fb90cc1f599e2cc2908ec8225e10915006cc")
    block_other = Block(index=0, timestamp=1500000000, data="BLOCK",
                        previous="00000221653e89d7b04704d4690abcf83fdb144106bb0453683c8183253fabad")
    assert block != block_other


def test_blocks_with_different_nonce_are_not_equal():
    block = Block(index=0, timestamp=1500000000, data="BLOCK", previous="", nonce=0)
    block_other = Block(index=0, timestamp=1500000000, data="BLOCK", previous="", nonce=132)
    assert block != block_other


def test_blocks_with_different_hash_are_not_equal():
    block = Block(
        index=2,
        nonce=1315081,
        timestamp=1508895393,
        data="Data of 2nd block",
        hash_sequence="000003cf81f6b17e60ef1e3d8d24793450aecaf65cbe95086a29c1e48a5043b1",
        previous="00000c575050241e0a4df1acd7e6fb90cc1f599e2cc2908ec8225e10915006cc"
    )
    block_other = Block(
        index=3,
        nonce=24959,
        timestamp=1508895777,
        data="Data of 3rd block",
        hash_sequence="00000221653e89d7b04704d4690abcf83fdb144106bb0453683c8183253fabad",
        previous="000003cf81f6b17e60ef1e3d8d24793450aecaf65cbe95086a29c1e48a5043b1"
    )
    assert block != block_other
