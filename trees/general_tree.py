class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def add_child(self, child):
        child.parent = self
        self.children.append(child)


if __name__ == '__main__':
    root = TreeNode("Electronics")

    laptop = TreeNode("laptop")
    mobile = TreeNode("mobile")
    adaptors = TreeNode("adaptors")
    tv = TreeNode("tv")

    root.add_child(laptop)
    root.add_child(mobile)
    root.add_child(adaptors)
    root.add_child(tv)

    laptop.add_child(TreeNode("ASUS ROG"))
    laptop.add_child(TreeNode("HP"))

    mobile.add_child(TreeNode("IQOO Neo6"))
    mobile.add_child(TreeNode("Vivo t2x"))
    mobile.add_child(TreeNode("Samsung 22 ultra"))
    mobile.add_child(TreeNode("Iphone"))

    tv.add_child(TreeNode("LG"))
    tv.add_child(TreeNode("Samsung"))

    root.print_tree()

