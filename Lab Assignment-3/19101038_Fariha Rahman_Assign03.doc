import math
import random


def AlphaBetaPruning(position, depth, alpha, beta, maximizingPlayer):
    global count2

    if depth == 0:
        count2 += 1
        return position.value

    if maximizingPlayer:
        maxEval = - math.inf
        for child in position.child:
            eval = AlphaBetaPruning(child, depth - 1, alpha, beta, False)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)

            if beta <= alpha:
                break
        return maxEval

    else:
        minEval = math.inf
        for child in position.child:
            eval = AlphaBetaPruning(child, depth - 1, alpha, beta, True)
            minEval = min(minEval, eval)
            beta = min(beta, eval)

            if beta <= alpha:
                break

        return minEval


def minimax(position, depth, maximizingPlayer):

    global count1

    if depth == 0:
        count1 += 1
        return position.value

    if maximizingPlayer:
        maxEval = - math.inf
        for child in position.child:
            eval = minimax(child, depth - 1, False)
            maxEval = max(maxEval, eval)

        return maxEval

    else:
        minEval = math.inf
        for child in position.child:
            eval = minimax(child, depth - 1, True)
            minEval = min(minEval, eval)

        return minEval


class Node:
    def __init__(self):
        self.child = []
        self.value = None

def treeGenerator(node, d):
    if d==0:
        node.value = random.randint(minimum, maximum)
        return

    for i in range(branch):
        c = Node()
        node.child.append(c)
        s = node.child[i]
        treeGenerator(s, d-1)

    return



turn = int(input("Enter number of turns for player : "))
depth = 2*turn
branch = int(input("Enter branches per node : "))
minimum = int(input("Enter minimum value of leaf nodes : "))
maximum = int(input("Enter maximum value of leaf nodes : "))

count1 = 0
count2 = 0

rootNode = Node()
treeGenerator(rootNode, depth)

minimax_amount = minimax(rootNode, depth, True)
#print(minimax_amount)

alpha_beta_amount = AlphaBetaPruning(rootNode, depth, -math.inf, math.inf, True)
#print(alpha_beta_amount)

print("Depth : ", depth)
print("Branch : ", branch)

print("Terminal states(Leaf Node) : ", branch ** depth)
print("Maximum Amount : ", minimax_amount)
print("Comparison before Alpha Beta Pruning : ", count1)
print("Comparison after Alpha Beta Pruning : ", count2)