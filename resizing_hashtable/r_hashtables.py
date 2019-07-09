

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
    # check to see if the current storage already contains a LL or LP
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
# Removes a key:value pair and returns warning where key doesn't exist
# '''
def hash_table_remove(hash_table, key):
    # hash the key
    hashed_key = hash(key, hash_table.capacity)
    # set the index of the key to be found
    proposed_index = hash_table.storage[hashed_key]
    # see if there's anything at the proposed index
    if not proposed_index:
        print(f"WARNING: The key: {key} does not exist in the hash table")
    else:
        # loop through the pairs until we find the key
        current_pair = hash_table.storage[hashed_key]
        # check to see if its the only pair in that pos
        if current_pair.key == key and current_pair.next = None:
            hash_table.storage[hashed_key] = None
            return None
        # loop through the pairs otherwie
        while current_pair.next:
            if current_pair.next == key:
                # remove the pair and reconnect the prev pair to the nodes next pair
                next_pair = current_pair.next
                current_pair.next = next_pair.next
                return None
        # if the key is not found, return the no-find error
        print(f"WARNING: The key: {key} does not exist in the hash table")

# '''
# Retrieves a key:value pair and returns None if the key is not found
# '''
def hash_table_retrieve(hash_table, key):
    # hash the key
    hashed_key = hash(key, hash_table.capacity)
    # set the index of the key to be found
    proposed_index = hash_table.storage[hashed_key]
    # see if there's anything at the proposed index
    if not proposed_index:
        print(f"WARNING: The key: {key} does not exist in the hash table")
    else:
        # loop through the pairs until we find the key
        current_pair = hash_table.storage[hashed_key]
        while current_pair.next:
            if current_pair.key == key:
                return current_pair.value
            current_pair = current_pair.next
        # if the key is not found, return the no-find error
        print(f"WARNING: The key: {key} does not exist in the hash table")


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
