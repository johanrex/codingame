import tsp_twoopt
import tsp_bruteforce
import tsp_random_permutations
import tsp_nearest_neighbor


def test_tsp_random_permutations():
    inputs = [(485, 475), (1150, 750), (1008, 480), (1562, 134), (1155, 523)]
    shortest_distance, indexes = tsp_random_permutations.calc_distance_random_permutations(inputs)
    route = " ".join(indexes)
    assert "0 2 3 4 1 0" == route


def test_tsp_twoopt():
    inputs = [(485, 475), (1150, 750), (1008, 480), (1562, 134), (1155, 523)]
    shortest_distance, indexes = tsp_twoopt.tsp_two_opt(inputs)
    route = " ".join(indexes)
    assert "0 1 4 3 2 0" == route


def test_tsp_bruteforce():
    inputs = [(485, 475), (1150, 750), (1008, 480), (1562, 134), (1155, 523)]
    shortest_distance, indexes = tsp_bruteforce.calc_distance_brute_force(inputs)
    route = " ".join(indexes)
    assert "0 2 3 4 1 0" == route


def test_tsp_nearest_neighbor():
    inputs = [(485, 475), (1150, 750), (1008, 480), (1562, 134), (1155, 523)]
    shortest_distance, indexes = tsp_nearest_neighbor.calc_distance_nearest_neighbor(inputs)
    route = " ".join(indexes)
    assert "0 2 4 1 3 0" == route


if __name__ == "__main__":
    # test_tsp_twoopt()
    # test_tsp_random_permutations()

    inputs = [(485, 475), (1150, 750), (1008, 480), (1562, 134), (1155, 523)]

    shortest_distance_bf, indexes_bf = tsp_bruteforce.calc_distance_brute_force(inputs)
    route_bf = " ".join(indexes_bf)

    shortest_distance_to, indexes_to = tsp_twoopt.tsp_two_opt(inputs)
    route_to = " ".join(indexes_to)
    pass

    # inputs = [(485, 475), (1150, 750), (1008, 480), (1562, 134), (1155, 523)]
    # best_cost, indexes = tsp_twoopt.tsp_two_opt()
