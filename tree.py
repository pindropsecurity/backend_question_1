class Tree(object):
    def __init__(self, val=None):
        self.set_val(val)
        self.children = []

    def add_child(self, val):
        child = Tree(val)
        self.children[len(self.children)] = child

    def add_parent(self, val):
        parent = Tree(val)
        parent.add_child(self)

    def set_val(self, val):
        self.val = val

    def get_val(self):
        return self.val

    def get_nth_child(self, index):
        return self.children[index]

