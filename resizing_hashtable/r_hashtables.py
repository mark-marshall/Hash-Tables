

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# '''
# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        # max length of hash table
        self.capacity = capacity
        # underlying data structure for storing values
        self.storage = [None] * capacity


# '''
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381
    for char in string:
        hash = ((hash << 5) + hash) + ord(char)
    return hash % max


# '''
# Inserts a key:value pair as a linked pair in the list
# '''
def hash_table_insert(hash_table, key, value):
    # create a new instance of the LinedPair class
    new_pair = LinkedPair(key, value)
    # hash the key
    hashed_key = hash(new_pair.key, hash_table.capacity)
    # check to see if the current storage aalready contains a LL or LP
    if hash_table.storage[hashed_key]:
        # loop through the linked pairs until we get to the one with none at the end
        current_pair = hash_table.storage[hashed_key]
        while current_pair.next:
            # set new next pair as current_pair
            current_pair = current_pair.next
        # add the linked pair as the next item
        current_pair.next = new_pair
    else:
        hash_table.storage[hashed_key] = new_pair


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


# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    pass


def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")


Testing()
