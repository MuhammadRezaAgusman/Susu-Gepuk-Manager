from utility import validate as vdl

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, data):

        new = Node(data)

        if self.root is None:
            self.root = new
            return

        P = self.root
        Q = self.root

        while Q is not None:

            P = Q

            # berdasarkan harga
            if new.data["harga"] < P.data["harga"]:
                Q = P.left

            else:
                Q = P.right


        if new.data["harga"] < P.data["harga"]:
            P.left = new

        else:
            P.right = new
    
    def inorder(self):

        self._inorder(self.root)


    def _inorder(self, node):

        if node is not None:

            self._inorder(node.left)

            data = node.data

            status = vdl.validasi_stok(data)

            print(
                data["kode"].ljust(12),
                data["nama"].ljust(28),
                "Rp.",str(data["harga"]).ljust(9),
                str(data["stok"]).ljust(3),
                status
            )

            self._inorder(node.right)