class TrieNode:
    def __init__(self, bit):
        self.bit = bit

        self.is_end = False

        self.value_leaf = None

        self.children = {}

class Trie:
     def __init__(self):
         self.root = TrieNode("")

     def insert(self, node_root, bit_arr, value_leaf):
         '''
         Insert symbols and bit_arr into prefix tree
         '''
         node = node_root
         for i in range(len(bit_arr)):
             if bit_arr[i] not in node.children:
                 new_node = TrieNode(bit_arr[i])
                 node.children[bit_arr[i]] = new_node
                 node = new_node
             else:
                 node = node.children[bit_arr[i]]
         node.is_end = True
         node.value_leaf = value_leaf
         return node_root

     def getListSymbols(self, node_root, bit_string, data_len):
         '''
         Get symbols from bit_string base on prefix tree
         '''
         result = ""
         point_node = node_root
         for i in range(data_len):
             if point_node.is_end == False :
                 if point_node.children[bit_string[i]] != None:
                     new_point_node = point_node.children[bit_string[i]]
                     if new_point_node != None and new_point_node.is_end == False:
                         point_node = new_point_node
                     elif new_point_node != None and new_point_node.is_end == True:
                         result = result + new_point_node.value_leaf
                         point_node = node_root
         return result

class PrefixCodeTree:

    def __init__(self):
        '''
        Khoi tao cay
        '''
        self.node_root = TrieNode("")
        self.trie = Trie()

    def insert(self, codeword, symbol):
        '''
        Them cac gia tri nut va la cho cay
        '''
        self.node_root = self.trie.insert(self.node_root, codeword, symbol)

    def decode(self, encoded_data, data_len):
        '''
        Giai ma byte ve bit
        Dua chuoi bits vao cay de suy ra cac symbol tuong ung
        Sau do tra ve chuoi cac symbols
        '''
        bit_string = "{:08b}".format(int(encoded_data.hex(), 16))
        return self.trie.getListSymbols(self.node_root, bit_string, data_len)

# if __name__ == '__main__':
#     '''
#     Run test
#     '''
#     prefix_code_tree = PrefixCodeTree()
#     codebook = {
#          'x1': ['0'],
#          'x2': ['1', '0', '0'],
#          'x3': ['1', '0', '1'],
#          'x4': ['1', '1']
#     }
#     for symbol in codebook:
#         prefix_code_tree.insert(codebook[symbol], symbol)
#     print(prefix_code_tree.decode(b'\xd2\x9f\x20', 21))