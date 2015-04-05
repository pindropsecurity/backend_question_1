class Tree(object):
    """
    n-ary Tree 
    """
    def __init__(self, val=None):
        """
        Each node will have a value and children node
        """
        self.set_val(val)
        self.children = []


    def add_child(self, val=None):
        """
        Add a Child node by creating node from plain value
        """
        child = Tree(val)
        self.children.append(child)

    
    def update_child(self, node, index=0):
        """
        Update a Node's children with given node
        """
        self.children.insert(index, node) 


    def set_val(self, val):
        """
        value setter
        """
        self.val = val


    def get_val(self):
        """
        value getter
        """
        return self.val


    def get_newborn_child(self):
        """
        get the latest child Node added to current Node
        """
        if self.children:
            return self.children[len(self.children) - 1]

    def get_children(self):
        """
        get all children list for current Node
        """
        return self.children

