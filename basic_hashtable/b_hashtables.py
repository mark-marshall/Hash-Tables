

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

# turn the key into a index where values are stored in an array

# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    # hash the key
    hashed_key = self.hash(key)
    # check to see whether the current storage already contains a value at that index
    if self.storage[hashed_key]:
        print(f"WARNING: This insertion will overwrite an existing key:value")
    # add the value at the hash index
    self.storage[hashed_key] = value

# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    pass


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    pass


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
