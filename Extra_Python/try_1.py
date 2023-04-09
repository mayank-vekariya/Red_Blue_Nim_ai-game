class Node:
    def init(self,parent=object,remaning=0, trun=None, value=0):
        self.parent=parent
        self.remaning=remaning
        self.trun=trun
        self.value=value



def make_child(node):
    childs=[]
    for i in range(1,3):
        if node.remaning-i>=0:
            trun='max'
            value=0
            if node.trun=="max":
                trun="min"
            if trun=="max":
                value=-10
            if trun=="min":
                value=10
            if node.remaning-i==0 and trun=="max":
                value=-1
            if node.remaning-i==0 and trun=="min":
                value=1
            childs.append(Node(parent=node,remaning=node.remaning-i,trun=trun,value=value))
    # print(len(childs))
    return childs

def back(node):
    i=node
    while True:
        if i.parent=="root":
            print(f" node - {i.remaning}, value -> {i.value}")
            break
        if i.parent.trun == "max":
            if i.parent.value < i.value:
                i.parent.value = i.value
        if i.parent.trun == "min":
            if i.parent.value > i.value:
                i.parent.value = i.value
        print(f" node - {i.remaning}, value -> {i.value}")

        i=i.parent

def dfs():
    ll=[]
    start=Node(parent="root",remaning=4,trun="max",value=-10)
    ll.append(start)
    while len(ll)>0:
        c=ll[-1]
        print(f" forward -> {c.remaning}")
        del ll[-1]
        if c.remaning>0:
            for i in make_child(c):
                print(f" child -> {i.remaning}",end=" - ")
                if i.remaning==0:
                    print("back")
                    back(i)

                else:
                    ll.append(i)
            print()

    print(start.value)
dfs()


