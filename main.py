def children(red, blue):
    possible_new_states = []
    if red > 0 and blue > 0:
        possible_new_states.append([red - 1, blue])
        possible_new_states.append([red, blue - 1])
    return possible_new_states
def future_eval(r, b, turn):
    x = abs(r - b)
    if turn:
        if x % 2 == 0:
            return -2
        else:
            return 2
    else:
        if x % 2 == 0:
            return 2
        else:
            return -2
def minimax(red, blue, depth, max_turn,alpha = float('-inf'), beta = float('inf')):
    if red == 0:
        return blue * 3 if max_turn else -blue * 3
    if blue == 0:
        return red * 2 if max_turn else -red * 2
    if depth == 0:
        return future_eval(red, blue, max_turn)
    if max_turn:
        best_score = float('-inf')
        for move in children(red, blue):
            score = minimax(move[0], move[1], depth - 1, False,alpha, beta)
            best_score = max(score, best_score)
            alpha = max(alpha, score)
            if beta <= alpha:
                break
        return best_score
    else:
        best_score = float('inf')
        for move in children(red, blue):
            score = minimax(move[0], move[1], depth - 1, True,alpha, beta)
            best_score = min(score, best_score)
            beta = min(beta, score)
            if beta <= alpha:
                break
        return best_score




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
        if depth<0:
            print("depth not < 0")
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
count=0
while True:
    print()
    print("~" * 27)
    print(f"step {count}")
    print("~" * 27)
    print(f"* num_red : {num_red}")
    print(f"* num_blue : {num_blue}")
    print(f"* first_player : {first_player}")
    print(f"* next_player : {second_player}")
    print(f"* tree_depth : {depth}")
    print("~" * 27)
    if num_blue>0 and num_red>0:
        print(f"{first_player} have two choices.")
        choices = children(num_red, num_blue)
        print(f"(a) red:{choices[0][0]}, blue {choices[0][1]} (b) red:{choices[1][0]} blue:{choices[1][1]}")
        if first_player=="computer":
            first_pick=minimax(choices[0][0],choices[0][1],depth,False)
            second_pick=minimax(choices[1][0],choices[1][1],depth,False)
            # print(first_pick,second_pick)
            if first_pick>second_pick:
                print(f"computer select -> red : {choices[0][0]}, blue : {choices[0][1]}")
                num_red = choices[0][0]
                num_blue = choices[0][1]
            else:
                print(f"computer select -> red : {choices[1][0]}, blue : {choices[1][1]}")
                num_red = choices[1][0]
                num_blue = choices[1][1]
            first_player="human"
            second_player="computer"
            depth=num_red+num_blue
        else:
            selection=input("select (a) or (b) : ")
            d_depth=int(input("depth or put it 0 : "))
            if d_depth>0:
                depth=d_depth
            if selection=="a":
                num_red=choices[0][0]
                num_blue=choices[0][1]
            else:
                num_red=choices[1][0]
                num_blue=choices[1][1]
            first_player = "computer"
            second_player = "human"
    else:
        if num_red == 0:
            if first_player=="computer":
                print(f"!! COMPUTER WIN !! POINTS -> {num_blue*3}")
            else:
                print(f"!! HUMAN WIN !! POINTS -> {num_blue*3}")

        if num_blue == 0:
            if first_player == "computer":
                print(f"!! COMPUTER WIN !! POINTS -> {num_red * 2}")
            else:
                print(f"!! HUMAN WIN !! POINTS -> {num_red * 2}")
        print("~" * 27)
        break

    print("~" * 27)
    print(" "*12+"|")
    print(" "*12+"|")
    print(" "*12+"v")
    count+=1
