# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        hash = 5381
        for x in key:
            hash = (( hash << 5) + hash) + ord(x)
        return hash & 0xFFFFFFFF


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash_djb2(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        index = self._hash_mod(key)

        # print("capacity is ", self.capacity)
        # print(f'\"{value}\" came in as {index}')

        if self.storage[index] is not None:
            new_node = LinkedPair(key, value)
            new_node.next = self.storage[index]
            self.storage[index] = new_node
        else:
            self.storage[index] = LinkedPair(key, value)

        # node = self.storage[index]
        # while node is not None:
        #     print(f'Node {node.key} with value {node.value}')
        #     node = node.next


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        
        # check if selected index is empty
        if self.storage[index] is not None:
            # check if there is multiple items in the index
            if self.storage[index].next is not None:
                node = self.storage[index]
                prevNode = None
                foundKey = False
                while node is not None:
                    if key == node.key:
                        foundKey = True
                        if prevNode is None:
                            self.storage[index] = node.next
                        else:
                            prevNode.next = node.next
                    prevNode = node
                    node = node.next
                if foundKey is False:
                    print("ERROR: This is nothing at the index")
                # print(f'The next value is {self.storage[index].next.value}')
            else:
                self.storage[index] = None
        else:
            print("ERROR: This is nothing at the index")


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)

        if self.storage[index] is None:
            return None
        else:
            # check if there is multiple items in the index
            if self.storage[index].next is not None:
                node = self.storage[index]
                while node is not None:
                    if key == node.key:
                        return node.value
                    node = node.next
                return None
            else:
                return self.storage[index].value

    def printStorage(self):
        for i, pair in enumerate(self.storage):
            if pair is not None:
                if pair.next is None:
                    print(pair.key, pair.value, i)
                else:
                    linkedPair = pair
                    while linkedPair is not None:
                        print(linkedPair.key, linkedPair.value, i)
                        linkedPair = linkedPair.next

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # save a copy of the old storage
        old_storage = self.storage
        # double the capacity of storage
        self.capacity *= 2

        # create a new temp storage to copy
        self.storage = [None] * self.capacity
        # move all the elements from old to new
        for pair in old_storage:
            if pair is not None:
                if pair.next is None:
                    self.insert(pair.key, pair.value)
                else:
                    linkedPair = pair
                    while linkedPair is not None:
                        self.insert(linkedPair.key, linkedPair.value)
                        linkedPair = linkedPair.next


# hashTable = HashTable(5)
# hashTable.insert('somekey1', 'somevalue1')
# hashTable.insert('somekey2', 'somevalue2')
# hashTable.insert('somekey3', 'somevalue3')
# hashTable.insert('somekey4', 'somevalue4')

# hashTable.remove('somekey4')
# hashTable.remove('somekey1')

# hashTable.insert('somekey1', 'somevalue1')

# print(hashTable.retrieve('somekey1'))
# print(hashTable.retrieve('somekey2'))
# print(hashTable.retrieve('somekey3'))
# print(hashTable.retrieve('somekey4'))

# retrieveKey = hashTable.retrieve('somekey')
# print(f"Retrieve key that exists '{retrieveKey}'")
# retrieveKey = hashTable.retrieve('somekey2')
# print(f"Retrieve key that does not exists '{retrieveKey}'")

# hashTable.remove('somekey')

# hashTable.printStorage()

# if __name__ == "__main__":
#     ht = HashTable(2)

#     ht.insert("line_1", "Tiny hash table")
#     ht.insert("line_2", "Filled beyond capacity")
#     ht.insert("line_3", "Linked list saves the day!")

#     print("")

#     # Test storing beyond capacity
#     print(ht.retrieve("line_1"))
#     print(ht.retrieve("line_2"))
#     print(ht.retrieve("line_3"))

#     # Test resizing
#     old_capacity = len(ht.storage)
#     ht.resize()
#     new_capacity = len(ht.storage)

#     print(f"\nResized from {old_capacity} to {new_capacity}.\n")

#     # Test if data intact after resizing
#     print(ht.retrieve("line_1"))
#     print(ht.retrieve("line_2"))
#     print(ht.retrieve("line_3"))

#     print("")
