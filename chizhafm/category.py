class Category():
    def __init__(self,cateid,name,children=list()):
        self.cateid = cateid
        self.name = name
        self.children = children

    def __str__(self):
        return str(self.cateid) + self.name + str(len(self.children))

