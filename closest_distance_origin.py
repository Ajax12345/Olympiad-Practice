#this program finds the corridinate that is closest to the origin
import math as mt
the_points = [[1, 2], [5, 6], [6, 7], [78, 90], [4, 5], [1, 1], [0.5, 0.5]]

the_best = [[0, 0]]
shortest_distance = 0
for i in range(len(the_points)):
    distance = mt.sqrt(pow(the_points[i][0], 2)+pow(the_points[i][1], 2))
    if distance > shortest_distance:
        shortest_distance = distance

for i in range(len(the_points)):
    distance = mt.sqrt(pow(the_points[i][0], 2)+pow(the_points[i][1], 2))
    if distance < shortest_distance:
        shortest_distance = distance
        the_best[0] = [the_points[i][0], the_points[i][1]]

print the_best
