from room import Room
from player import Player
from world import World
from util import Stack
from graph import Graph

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# You may find the commands `player.current_room.id`, `player.current_room.get_exits()` and `player.travel(direction)` useful.

current_room = player.current_room.id
# print("current room:", current_room)
exits = player.current_room.get_exits()
# print("exits:", exits)
random_exit = random.choice(exits)
# print("random exit:", random_exit)
print("Room Graph:", room_graph)
print()

# for room in room_graph:
#     exit_dic = room_graph[room][-1]
#     print(room, exit_dic)

# for exit in exit_dic:
# print(room, exit_dic[exit])

# Algorithm:
# Use DFT
# Pick a random unexplored direction from current room
# Travel and log that direction

# instantiate a graph
graph = Graph()
# loop through array of tuples
# for exit in exits:
#     # add numbers to set of possible vertices
#     if exit not in graph.vertices:
#         graph.add_vertex(exit)

for room in room_graph:
    graph.add_vertex(room)

for room in room_graph:
    exit_dic = room_graph[room][-1]

    for exit in exit_dic:
        graph.add_edge(room, exit_dic[exit])
print("Vertices:", graph.vertices)

# find paths to every possible vertex using recursion
path_list = []
for vertex in graph.vertices:
    path = graph.dfs_recursive(current_room, vertex)
    # Filter out None values
    # if path is not None:
    path_list.append(path)
print(path_list)


# def dft(starting_vertex):
#     """
#     Print each vertex in depth-first order
#     beginning from starting_vertex.
#     """
#     # Create an empty stack
#     s = Stack()
#     # Push the starting vertex_id to the stack
#     s.push(starting_vertex)
#     # Create an empty set to store visited nodes
#     visited = set()
#     # While the stack is not empty...
#     while s.size() > 0:
#         # Pop the first vertex
#         exit = s.pop()
#         # Check if it's been visited
#         # If it has not been visited...
#         if exit not in visited:
#             # Mark it as visited
#             print(exit)
#             visited.add(exit)
#             # Then push all neighbors to the top of the stack
#             for neighbor in self.get_neighbors(v):
#                 s.push(neighbor)


# DFT = dft(22)
# print("DFT:", DFT)


# Loop
# if all directions are explored...
# Walk back to nearest room that contains an unexplored path
# Use modified BFS
# Put explored exits into queue
# BFS will return path as list of room id's
# Convert this to a list of n/s/e/w directions before adding to traversal path

# Done when all paths have been explored


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
