class HashTable:
    #constructor
    def __init__(self, size = 7):
        self.data_map = [None] * size
    #hash method
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter)*11)% len(self.data_map)
        return my_hash
    ##########################################
    def print_table(self): #O(n)
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)
    ##########################################        
    def set_item(self, key, value): #O(1)
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = [] 
        self.data_map[index].append([key, value]) 
    ##########################################
    def get_item(self, key): #O(n)
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
    ##########################################
    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys
            




my_hash_table = HashTable()
my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('bolts1', 50)
my_hash_table.set_item('lumber', 70)

my_hash_table.print_table()
print(my_hash_table.get_item('bolts1'))
print(my_hash_table.keys())