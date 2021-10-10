import heapq
from itertools import permutations

def addVertex(v):
    global graph
    global vertices_no
    if not v in graph:
        vertices_no += 1
        graph[v] = {}
    
def addEdge(v1, v2, e):
    global graph
    if (v1 in graph and v2 in graph):
        graph[v1][v2] = e
        graph[v2][v1] = e


def print_graph():
  global graph
  for vertex in graph:
    for edges in graph[vertex]:
      print(vertex, " -> ", edges[0], " edge weight: ", edges[1])

def calculateDistances(starting_vertex):
  global graph
  distances = {vertex: float("infinity") for vertex in graph}
  distances[starting_vertex] = 0
  pq = [(0, starting_vertex)]
  while len(pq) > 0:
    current_distance, current_vertex = heapq.heappop(pq)
    if current_distance > distances[current_vertex]:
      continue
    for neighbor, weight in graph[current_vertex].items():
      distance = current_distance + weight
      if distance < distances[neighbor]:
        distances[neighbor] = distance
        heapq.heappush(pq, (distance, neighbor))
    return distances

def distance(cities):
  distance = 0
  for i in range(1, len(cities)):
    distance += graph[cities[i-1]][cities[i]]
  return distance


graph = {}
vertices_no = 0

file = open("input9.txt")
distances = file.read().split("\n")

for d in distances:
    nodes = d.split(" ")
    addVertex(nodes[0])
    addVertex(nodes[2])
    addEdge(nodes[0], nodes[2], int(nodes[4]))

min_distance = float("infinity")
max_distance = float("-infinity")
cities = graph.keys()
perm = permutations(cities)

for i in list(perm):
  d = distance(i)
  if(d < min_distance):
    min_distance = d
  if(d > max_distance):
    max_distance = d
  

print(max_distance)