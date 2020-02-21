from room import Room
from player import Player
from world import World
from util import Stack, Queue
from graph import Graph

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
map_file = "maps/test_loop_fork.txt"
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
print("current room:", current_room)
print()
exits = player.current_room.get_exits()
print("current room exits:", exits)
print()
random_exit = random.choice(exits)
print("random exit:", random_exit)
print()
rooms = []
for room in room_graph:
    rooms.append(room)
print("Rooms:", rooms)
print()
print("Room Graph:", room_graph)
print()

# Algorithm:
# Use DFT
q = Queue()
# Add the starting vertex_id to the queue
q.enqueue(current_room)
# Create an empty set to store visited nodes
visited = set()
# While the queue is not empty...
while q.size() > 0:
    # Dequeue, the first vertex
    room = q.dequeue()
    # Check if it's been visited
    # If it has not been visited...
    if room not in visited:
        # Mark it as visited
        print(room)
        visited.add(room)
        # Then add all neighbors to the back of the queue
        for neighbor in room_graph[current_room][-1]:
            q.enqueue(room_graph[current_room][-1][neighbor])

# Pick a random unexplored direction from current room
# Travel and log that direction
# Loop
# if all directions are explored...
# Walk back to nearest room that contains an unexplored path
# Use modified BFS
# Put explored exits into queue
# BFS will return path as list of room id's
# Convert this to a list of n/s/e/w directions before adding to traversal path

# Done when all paths have been explored

# ----- Attempt 1 ------

# instantiate a graph
# graph = Graph()

# for room in room_graph:
#     graph.add_vertex(room)

# for room in room_graph:
#     exit_dic = room_graph[room][-1]

#     for exit in exit_dic:
#         graph.add_edge(room, exit_dic[exit])
# print("Vertices:", graph.vertices)
# print()

# find paths to every possible vertex using recursion
# paths = []
# for vertex in graph.vertices:
#     paths.append(graph.dfs(current_room, vertex))
# print("Paths:", paths)
# print()

# dirs = []
# for path in paths:
#     for room in path:
#         if room in room_graph[]
# print(dirs)

# ----- End of Attempt 1 -----


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
