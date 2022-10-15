import tsp

inputs = [(485, 475), (1150, 750), (1008, 480), (1562, 134), (1155, 523)]
route = tsp.calc_distance(inputs)
print(route)
