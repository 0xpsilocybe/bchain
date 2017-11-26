from bchain.dbmanager import select_all_blocks


def sync():
    return select_all_blocks()
