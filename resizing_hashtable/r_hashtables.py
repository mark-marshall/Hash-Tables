

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
        # loop through the linked pairs until we get to a pre-existing key or the end pair
        current_pair = hash_table.storage[hashed_key]
        while current_pair.next:
            if current_pair.key == key:
                current_pair.value = value
                return None
            # set new next pair as current_pair
            current_pair = current_pair.next
        # check to see if the last pair in the list matches the key
        if current_pair.key == key:
            current_pair.value = value
        # add the linked pair as the next item
        else:
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
        # check to see if its the first pair in the list
        if current_pair.key == key:
            # check to see if its the only pair at that index
            if current_pair.next == None:
                hash_table.storage[hashed_key] = None
            # set the new starter pair if it's not the only pair
            else:
                hash_table.storage[hashed_key] = current_pair.next
            return None
        # loop through the pairs if its not the first pair
        while current_pair.next:
            # check to see if the target pair is at the next position
            if current_pair.next == key:
                # set the target pair to a variable
                target_pair = current_pair.next
                # if the target pair has a next pair, hook that up to the current pair
                if target_pair.next:
                    current_pair.next = target_pair.next
                # otherwise, set the current pairs next to None
                else:
                    current_pair.next = None
                return None
            # set the next pair as current_pair.next to continue to the loop
            current_pair = current_pair.next
        # check to see if the last pair in the list matches the key
        if current_pair.key == key:
            # set the key to zero so its effectively removed from future searches
            current_pair.key = None
        else:
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
    if proposed_index is None:
        return None
    else:
        # loop through the pairs until we find the key
        current_pair = hash_table.storage[hashed_key]
        while current_pair.next:
            if current_pair.key == key:
                return current_pair.value
            current_pair = current_pair.next
        # check to see if its the last pair in the list
        if current_pair.key == key:
            return current_pair.value
        # return none if the key is not found
        else:
            return None


# '''
# Doubles the capacity of the hash table
# '''
def hash_table_resize(hash_table):
    # save the original hash_table storage
    original_storage = hash_table.storage
    # set new capacity to double
    hash_table.capacity = hash_table.capacity * 2
    # initialize a new list for the storage
    hash_table.storage = [None] * hash_table.capacity
    # copy over the elements
    for i in range(len(original_storage)):
        # save the first pair
        first_pair = original_storage[i]
        # check to see whether the index has any content
        if not first_pair:
            continue
        # loop over all pairs and all nested pairs and use the insert method
        if first_pair.next:
            cur_pair = original_storage[i]
            while cur_pair.next:
                hash_table_insert(hash_table, cur_pair.key, cur_pair.value)
                cur_pair = cur_pair.next
            # insert the last pair in the list
            hash_table_insert(hash_table, cur_pair.key, cur_pair.value)
        else:
            hash_table_insert(hash_table, first_pair.key, first_pair.value)
    # return the updated hash table
    return hash_table

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
