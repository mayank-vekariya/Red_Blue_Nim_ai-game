import sys

num_red=0
num_blue=0
first_player="computer"
second_player="human"
depth=0
try:
    num_red = int(sys.argv[1])
    num_blue = int(sys.argv[2])
    depth=num_red+num_blue
    try:
        depth=int(sys.argv[3])
        if depth<=0:
            print("depth<=0")
            depth = num_red + num_blue
    except:
        try:
            if sys.argv[3] == "human":
                first_player = "human"
                second_player = "computer"
            try:
                depth=int(sys.argv[4])
            except:
                pass
        except:
            pass

    print("*"*90+"\nThe input is correct!!, Let's Start Game......")

except:
    print("!!WRONG!! -> Error in the input, CORRECT CMD  ->  red_blue_nim.py <num-red> <num-blue> <first-player> <depth>")

print("`"*90+"\n"+"="*34+">"+"   red_blue_nim   "+"<"+"="*36+"\n"+"*"*90)
print()
print("~"*27)
print("initial step")
print("~"*27)
print(f"* num_red : {num_red}")
print(f"* num_blue : {num_blue}")
print(f"* first_player : {first_player}")
print(f"* next_player : {second_player}")
print(f"* tree_depth : {depth}")
print("~"*27)
print()

print()
print("~"*27)
print("step 1")
print("~"*27)
print(f"* num_red : {num_red}")
print(f"* num_blue : {num_blue}")
print(f"* first_player : {first_player}")
print(f"* next_player : {second_player}")
print(f"* tree_depth : {depth}")
print("~"*27)
print()