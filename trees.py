from queue import Queue


class BinaryTree:

    class Node:
        def __init__(self, data=None, left_child=None, right_child=None):
            self.left_child = left_child
            self.right_child = right_child
            self.data = data

    def __init__(self, root_data):
        self.root = self.Node(root_data)

    def add(self, data):

        def add_to_node(data, node):
            if(data < node.data):
                if(node.left_child):
                    add_to_node(data, node.left_child)
                else:
                    node.left_child = self.Node(data)
            elif(data > node.data):
                if(node.right_child):
                    add_to_node(data, node.right_child)
                else:
                    node.right_child = self.Node(data)

        node = self.root
        add_to_node(data, node)

    def view(self):

        def bfs(node):
            queue = Queue()
            queue.put(node)
            while(not queue.empty()):
                w_node = queue.get()
                print(w_node.data, end=' ')
                if(w_node.left_child):
                    queue.put(w_node.left_child)
                else:
                    print('-', end=' ')
                if(w_node.right_child):
                    queue.put(w_node.right_child)
                else:
                    print('-', end=' ')
        node = self.root
        bfs(node)

    def find(self, data):
        def dfs(node, data):
            if(node.data == data):
                return node
            else:
                if(node.left_child):
                    l = dfs(node.left_child, data)
                    if(l):
                        return l
                if(node.right_child):
                    r = dfs(node.right_child, data)
                    if(r):
                        return r
        node = self.root
        return dfs(node, data)

    def remove(self, data):
        def dfs(node, data):
            if node.data == data:
                return node
            else:
                if node.left_child:
                    l = dfs(node.left_child, data)
                    if(l):
                        return l
                if node.right_child:
                    r = dfs(node.right_child, data)
                    if(r):
                        return r
        node = self.root
        del_node = dfs(node, data)
        if del_node.right_child:
            del_node.data = del_node.right_child.data
            del_node.right_child = None
        elif del_node.left_child:
            del_node.data = del_node.left_child.data
            del_node.left_child = None


def main():
    tree = BinaryTree(5)
    tree.add(13)
    tree.add(4)
    tree.add(22)
    tree.view()
    print('')
    print(tree.find(5).data)
    tree.remove(13)
    tree.view()


if __name__ == '__main__':
    main()
