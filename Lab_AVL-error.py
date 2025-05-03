import sys 

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1 


def getHeight(node):
    if not node:
        return 0
    return node.height

def getBalance(node):
    if not node:
        return 0
    return getHeight(node.left) - getHeight(node.right)

def updateHeight(node):
    if node:
        node.height = 1 + max(getHeight(node.left), getHeight(node.right))

def rotate_right(y):
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    updateHeight(y)
    updateHeight(x)

    return x

def rotate_left(x):
    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    updateHeight(x)
    updateHeight(y)

    return y

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if not node:
            return Node(value)

        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        else:
            return node 
        
        updateHeight(node)
        
        balance = getBalance(node)

        if balance > 1 and getBalance(node.left) >= 0:
            return rotate_right(node) 
        elif balance > 1 and getBalance(node.left) < 0:
            node.left = rotate_left(node.left)
            return rotate_right(node) 
        elif balance < -1 and getBalance(node.right) <= 0:
            return rotate_left(node)
        elif balance < -1 and getBalance(node.right) > 0:
            node.right = rotate_right(node.right)
            return rotate_left(node) 
        
        return node 
    
    def eliminar(self, value):
        self.root = self._eliminar_recursive(self.root, value)

    def _eliminar_recursive(self, node, value):
        if not node:
            return node

        if value < node.value: #si el nodo que quiero eliminar es menor al nodo actual, se va por la izquierda
            node.left = self._eliminar_recursive(node.left, value)
        elif value > node.value: #si el nodo que quiero eliminar es mayor al nodo actual, se va por la derecha
            node.right = self._eliminar_recursive(node.right, value)

        else: #si no es ni mayor ni menor, se encontró el nodo a eliminar.
            if not node.left: #si no tiene hijo izquierdo, se reemplaza por su hijo derecho
                return node.right
            elif not node.right: #si no tiene hijo derecho, se reemplaza por su hijo izquierdo
                return node.left

            temp = self.find_min(node.right)
            node.value = temp.value
            node.right = self._eliminar_recursive(node.right, temp.value)

        updateHeight(node) #se actualiza el valor actual
        balance = getBalance(node)

        #rebalanceo
        if balance > 1 and getBalance(node.left) >= 0:
            return rotate_right(node)
        if balance > 1 and getBalance(node.left) < 0:
            node.left = rotate_left(node.left)
            return rotate_right(node)
        if balance < -1 and getBalance(node.right) <= 0:
            return rotate_left(node)
        if balance < -1 and getBalance(node.right) > 0:
            node.right = rotate_right(node.right)
            return rotate_left(node)

        return node

    def find_min(self, node):
        current = node
        while current.left:
            current = current.left
        return current
    
    def inorder(self):
        resultado = []
        self._inorder_recursive(self.root, resultado)
        return resultado

    def _inorder_recursive(self, node, resultado):
        if node:
            self._inorder_recursive(node.left, resultado)
            resultado.append(node.value)
            self._inorder_recursive(node.right, resultado) 

avl = AVLTree()
values_to_insert = [10, 20, 30, 40, 50, 25]

print("Insertando valores:", values_to_insert)
for val in values_to_insert:
    avl.insert(val)

print("\n--- Después de inserciones ---")
