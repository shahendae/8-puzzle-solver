from State import State
from Solver import Solver
import time

#   input puzzles to solve
puzzle = [1, 2, 0, 3, 4, 5, 6, 7, 8]
puzzle0 = [1, 3, 4, 8, 0, 5, 7, 2, 6]
puzzle1 = [1, 2, 3, 4, 5, 0, 6, 7, 8]
puzzle2 = [1, 2, 5, 3, 4, 0, 6, 7, 8]
puzzle3 = [0, 1, 3, 4, 2, 5, 7, 8, 6]
puzzle4 = [8, 3, 5, 4, 1, 6, 2, 7, 0]   # unsolvable
puzzle5 = [2, 8, 3, 1, 0, 5, 4, 7, 6]
puzzle6 = [8, 0, 6, 5, 4, 7, 2, 3, 1]
puzzle7 = [1, 2, 3, 4, 8, 0, 7, 6, 5]
puzzle8 = [1, 2, 0, 3, 4, 5, 6, 7, 8]
puzzle9 = [1, 2, 3, 4, 5, 0, 6, 7, 8]
puzzle10 = [1, 2, 3, 4, 0, 5, 6, 7, 8]
puzzle11 = [1, 2, 3, 0, 4, 5, 6, 7, 8]
puzzle12 = [3, 1, 2, 6, 4, 5, 0, 7, 8]
puzzle13 = [6, 1, 8, 4, 0, 2, 7, 3, 5]
game = State(puzzle10)
search = Solver(game)
print('\nBFS:')
print("=======================================")
start_time = time.time()
queue = search.bfs()
print('time taken:', time.time()-start_time)
print('\nDFS:')
print("=======================================")
start_time = time.time()
stack = search.dfs()
print('time taken:', time.time()-start_time)
print('\nA* by Manhattan heuristic:')
print("=======================================")
start_time = time.time()
manhattan = search.astar_manh()
print('time taken:', time.time()-start_time)
print('\nA* by Euclidean heuristic:')
print("=======================================")
start_time = time.time()
euclidean = search.astar_euc()
print('time taken:', time.time()-start_time)