def do_main():
    global j1s #jug 1 size
    j1s = int(input("Size of the Jug 1 you want:"))
    global j2s #jug 2 size
    j2s = int(input(" Size of the Jug 2 you want:"))

    gs1 = input("Goalstate of  jug1 you want:") #g1s goal state 1
    gs2 = input("Goalstate jug2 you want:") #g2s goal state 2
    

    startstate = (0, 0)
    gs = (int(gs1), int(gs2)) #gs goal state

    openlist = []
    openlist.append([startstate])

    print("Jug sizes: " + str(j1s) + ", " + str(j2s))
    print("Starting state: " + str(startstate))
    print("Goal state: " + str(gs))

    while (1):
        if len(openlist) == 0:
            print("No solution found")
            exit(0)
        curnode = openlist.pop(0)

        if curnode[-1] == gs:
            print("Found solution:")
            print(curnode)
            exit(0)

        openlist += S(curnode)


def S(node):
    returnlist = []
    state = node[-1]
    j1, j2 = state

    def checkState(new_state, old_state):
        if new_state != old_state:
            if not new_state in node:
                new_node = node.copy()
                new_node.append(new_state)
                returnlist.append(new_node)

    slist = [(j1, 0), (0, j2), (j1s, j2), (j1, j2s),
             (j1 - min(j1, j2s - j2), j2 + min(j1, j2s - j2)),
             (j1 + min(j2, j1s - j1), j2 - min(j2, j1s - j1))]
    for s in slist:
        checkState(s, state)

    return returnlist


if __name__ == "__main__":
    print("Water jug problem solver")
    do_main()