

# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# '''
# Basic hash table
# '''
class BasicHashTable:
    def __init__(self, capacity):
        # max length of hash table
        self.capacity = capacity
        # underlying data structure for storing values
        self.storage = [None] * capacity

# '''
# djb2 hash function
# '''
def hash(string, max):
    hash = 5381
    for char in string:
        hash = (hash * 33) + ord(char)
    return hash % max

# '''
# Inserts a key:value pair and returns warning where collisions occur
# '''
def hash_table_insert(hash_table, key, value):
    # create a new instance of the Pair class
    new_pair = Pair(key, value)
    # hash the key
    hashed_key = hash(new_pair.key, hash_table.capacity)
    # check to see whether the current storage already contains a key at that index
    if hash_table.storage[hashed_key]:
        print(f"WARNING: This insertion will overwrite an existing key with {value}")
    # add the value at the hash index
    hash_table.storage[hashed_key] = new_pair

# '''
# Removes a key:value pair and returns warning where key doesn't exist
# '''
def hash_table_remove(hash_table, key):
    # hash the key
    hashed_key = hash(key, hash_table.capacity)
    # check to see whether the current storage contains the key
    if not hash_table.storage[hashed_key]:
        print(f"WARNING: The key {key} does not yet exist in the table")
    else:
        hash_table.storage[hashed_key] = None

# '''
# Returns the value stored at the key and None if the key is unoccupied
# '''
def hash_table_retrieve(hash_table, key):
    # hash the key
    hashed_key = hash(key, hash_table.capacity)
    # check to see whether the current storage contains the key
    if not hash_table.storage[hashed_key]:
        return None
    # otherwise return the value
    else:
        return hash_table.storage[hashed_key].value


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
