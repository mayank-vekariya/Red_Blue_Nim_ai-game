def future_eval(r,b,turn):
    x=abs(r-b)
    if turn:
        if x%2==0:
            return -2
        else:
            return 2
    else:
        if x%2==0:
            return 2
        else:
            return -2

def minimax(red,blue,depth,max_turn):

    if depth==0:
        if red == 0:
            # print(f"start -> {red, blue, depth, max_turn}")
            return blue * 3 if max_turn else -blue * 3
        elif blue == 0:
            # print(f"start -> {red, blue, depth, max_turn}")
            return red * 2 if max_turn else -red * 2
        else:
            return future_eval(red,blue,max_turn)




    possible_new_states = []
    if red>0 and blue>0:
        possible_new_states.append([red-1,blue])
        possible_new_states.append([red,blue-1])


    # print(red,blue,possible_new_states,max_turn)
    if max_turn:
        scores = [
            minimax(new_state[0],new_state[1],depth-1,max_turn=False)
            for new_state in possible_new_states
        ]
        # print(f"max -> {scores,red,blue} point -> {max(scores)}")
        return max(scores)
    else:
        scores = [
            minimax(new_state[0],new_state[1],depth-1,max_turn=True)
            for new_state in possible_new_states
        ]
        # print(f"min -> {scores,red,blue} point -> {min(scores)}")
        return min(scores)




import sys

num_red=0
num_blue=0
first_player="computer"
second_player="human"
depth=0
try:
    num_red = sys.argv[1]
    num_blue = sys.argv[2]
    depth=num_red+num_blue
    try:
        depth=int(sys.argv[3])
    except:
        try:
            if sys.argv[3] == "human":
                first_player = "human"
                second_player = "computer"
            else:
                print("wrong player!")
            try:
                depth=int(sys.argv[4])
            except:
                pass
        except:
            pass

    print("The input is correct!!")



except:
    print("!!WRONG!! -> Error in the input, CORRECT CMD  ->  red_blue_nim.py <num-red> <num-blue> <first-player> <depth>")

print(num_red,num_blue,first_player,second_player,depth)


while True:
    pass