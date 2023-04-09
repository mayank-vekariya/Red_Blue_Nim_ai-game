import sys

# ***********************************************************
# input
# ***********************************************************

num_red=int(sys.argv[1])
num_blue=int(sys.argv[2])
first_player="computer"
second_player="human"
try:
    if sys.argv[3]=="human":
        first_player="human"
        second_player = "computer"

except:
    pass
# ***********************************************************
# Node
# ***********************************************************
class Node:
    def init(self,parent=None,right=None,left=None,remaning_b=None,remaning_r=None, trun=None, value=None, path=None):
        self.parent=parent
        self.left=left
        self.right=right
        self.remaning_b=remaning_b
        self.remaning_r=remaning_r
        self.trun=trun
        self.value=value
        self.path=path


def check_node(node):
    if node.remaning_r==0 and node.remaning_b==0:
        print("wrong input")
        return False
    elif node.remaning_r==0:
        print(f"{node.trun}points -> {node.remaning_b*3}")
        return False
    elif node.remaning_b==0:
        print(f"{node.trun} win, points -> {node.remaning_r*2}")
        return False
    else:
        return True

def make_child(node):
    childs=[]
    if node.remaning_r-1>=0:
        trun=first_player
        value=0
        if node.trun==first_player:
            trun=second_player
        if trun==first_player:
            value=float('-inf')
        if trun==second_player:
            value=float('inf')
        if node.remaning_r-1==0 and trun==first_player:
            value=node.remaning_b*3
        if node.remaning_r-1==0 and trun==second_player:
            value=-node.remaning_b*3
        xx=Node(parent=node,remaning_b=node.remaning_b,remaning_r=node.remaning_r-1,trun=trun,value=value)
        childs.append(xx)
        node.left=xx
    if node.remaning_b-1>=0:
        trun=first_player
        value=0
        if node.trun==first_player:
            trun=second_player
        if trun==first_player:
            value=float('-inf')
        if trun==second_player:
            value=float('inf')
        if node.remaning_b-1 == 0 and trun == first_player:
            value = node.remaning_r * 2
        if node.remaning_b-1 == 0 and trun == second_player:
            value = -node.remaning_r * 2
        xx=Node(parent=node,remaning_b=node.remaning_b-1,remaning_r=node.remaning_r,trun=trun,value=value)
        node.right=xx
        childs.append(xx)
    return childs

def back(node):
    i=node.parent
    while i!="root":
        if i.trun==first_player:
            if i.left.value!=float('inf') and i.right.value!=float('inf'):
                if i.left.value>i.right.value:
                    i.value=i.left.value
                    i.path=i.left
                else:
                    i.value=i.right.value
                    i.path=i.right
                # print(f"-----back red : {i.remaning_r} blue : {i.remaning_b} -> value : {i.value}")
            else:
                break
        else:
            if i.left.value!=float('-inf') and i.right.value!=float('-inf'):
                if i.left.value < i.right.value:
                    i.value = i.left.value
                    i.path = i.left
                else:
                    i.value = i.right.value
                    i.path = i.right
                # print(f"------back red : {i.remaning_r} blue : {i.remaning_b} -> value : {i.value}")

            else:
                break
        i=i.parent

def dfs():
    ll=[]
    start=Node(parent="root",remaning_b=num_blue,remaning_r=num_red,trun=first_player,value=float('-inf'))
    ll.append(start)
    while len(ll)>0:
        c=ll[-1]
        # print(f"in bucket -> red : {c.remaning_r} blue : {c.remaning_b}")
        del ll[-1]
        if check_node(c):
            for i in make_child(c):
                # print(f" child -> red : {i.remaning_r} blue : {i.remaning_b}",end=" <-> ")
                if i.remaning_b==0 or i.remaning_r==0:
                    # print("\nback")
                    back(i)
                else:
                    ll.append(i)
            print()

    print(f" red -> {start.path.remaning_r} blue -> {start.path.remaning_b}")
dfs()