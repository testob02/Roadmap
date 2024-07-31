class TreeNode:
    def __init__(self,data):
        self.name = data[0]
        self.designation = data[1]
        self.children = []
        self.parent = None

    def get_level(self):
        count = 0
        p = self.parent
        while p:
            count += 1
            p = p.parent

        return count

    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def print_tree(self,to_print,print_level):
        x = '   ' * self.get_level()
        x = x+'|__' if self.parent else x
        if to_print == 'both':
            if self.get_level() <= print_level():
                print(x+f'{self.name}  ({self.designation})')
            else:
                return
        if to_print == 'name':
            if self.get_level() <= print_level:
                print(x+self.name)
            else:
                return
        if to_print == 'designation':
            if self.get_level() <= print_level():
                print(x+self.designation)
            else:
                return
        if self.children:
            for child in self.children:
                child.print_tree(to_print,print_level)
    

# ceo = TreeNode(['Nilupul','CEO'])

# technical = TreeNode(['Chinmay','CTO'])
# infra_head = TreeNode(['Vishwa','Infrastructure Head'])
# infra_head.add_child(TreeNode(['Dhaval','Cloud Manager']))
# infra_head.add_child(TreeNode(['Abhijit','App Manager']))
# app_head = TreeNode(['Aamir','Application Head'])

# technical.add_child(infra_head)
# technical.add_child(app_head)

# admin = TreeNode(['Gels','HR Head'])
# admin.add_child(TreeNode(['Peter','Recruitment Manager']))
# admin.add_child(TreeNode(['Waqas','Policy Manager']))

# ceo.add_child(technical)
# ceo.add_child(admin)

# ceo.print_tree('name')
# ceo.print_tree('designation')
# ceo.print_tree('both')

# root = TreeNode(['Global',None])

# india = TreeNode(['India',None])
# guja = TreeNode(['Gujarat',None])
# guja.add_child(TreeNode(['Ahmedabad',None]))
# guja.add_child(TreeNode(['Baroda',None]))
# karna = TreeNode(['Karnataka',None])
# karna.add_child(TreeNode(['Bangluru',None]))
# karna.add_child(TreeNode(['Mysore',None]))
# india.add_child(guja)
# india.add_child(karna)

# usa = TreeNode(['USA',None])
# newj = TreeNode(['New Jersey',None])
# newj.add_child(TreeNode(['Princeton',None]))
# newj.add_child(TreeNode(['Trenton',None]))
# cali = TreeNode(['California',None])
# cali.add_child(TreeNode(['San Francisco',None]))
# cali.add_child(TreeNode(['Mountain View',None]))
# cali.add_child(TreeNode(['Palo Alto',None]))
# usa.add_child(newj)
# usa.add_child(cali)

# root.add_child(india)
# root.add_child(usa)


# root.print_tree('name',1)
# root.print_tree('name',2)
# root.print_tree('name',3)