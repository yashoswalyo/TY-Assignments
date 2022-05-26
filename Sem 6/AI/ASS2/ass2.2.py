##Water jug problem using dfs
def DFS(a, b, target):

    # Map is used to store the states, every
    # state is hashed to binary value to
    # indicate either that state is visited
    # before or not
    m = {}
    isSolvable = False
    path = []
    # Stack to maintain states
    stack = []
    # Initializing with initial state
    stack.append((0, 0))
    count=0
    while len(stack) > 0:

        # Current state
        u = stack.pop() #[0,0]
        count+=1
        # If this state is already visited
        if (u[0], u[1]) in m:
            continue

        # Doesn't met jug constraints
        if u[0] > a or u[1] > b or u[0] < 0 or u[1] < 0:
            continue

        # Filling the vector for constructing
        # the solution path
        path.append([u[0], u[1]])

        # Marking current state as visited
        m[(u[0], u[1])] = 1 
        # m = {(0,0):1,
        #      ():
        # }

        # If we reach solution state, put ans=1
        if u[0] == target or u[1] == target:
            isSolvable = True

            if u[0] == target:
                if u[1] != 0:

                    # Fill final state
                    path.append([u[0], 0])
            elif u[0] != 0:
                    # Fill final state
                path.append([0, u[1]])

            # Print the solution path
            sz = len(path)
            for i in range(sz):
                print("(", path[i][0], ",", path[i][1], ")")
            break

            # If we have not reached final state
        # then, start developing intermediate
        # states to reach solution state
        if u[1] <= b:
            stack.append([u[0], b])  # Fill Jug2
        elif u[0] <= a:
            stack.append([a, u[1]])  # Fill Jug1

        for ap in range(max(a, b) + 1):

            # Pour amount ap from Jug2 to Jug1
            c = u[0] + ap
            d = u[1] - ap

            # Check if this state is possible or not
            if c == a or (d == 0 and d >= 0):
                stack.append([c, d])

            # Pour amount ap from Jug 1 to Jug2
            c = u[0] - ap
            d = u[1] + ap

            # Check if this state is possible or not
            if (c == 0 and c >= 0) or d == b:
                stack.append([c, d])
        print(stack,f"\n{count}-----------\n")

    # No, solution exists if ans=0
    if not isSolvable:
        print("No solution")


# Driver code
if __name__ == "__main__":

    Jug1, Jug2, target = 4, 3, 2
    print("Path from initial state " "to solution state ::")
    DFS(Jug1, Jug2, target)
