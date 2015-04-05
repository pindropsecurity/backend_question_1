class Tree(object):
    def __init__(self, val=None):
        self.set_val(val)
        self.children = []


    def add_child(self, val=None):
        child = Tree(val)
        self.children.append(child)


    def set_val(self, val):
        self.val = val


    def get_val(self):
        return self.val


    def get_newborn_child(self):
        if self.children:
            return self.children[len(self.children) - 1]


