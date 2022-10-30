import tsp_twoopt
import tsp_bruteforce
import tsp_random_permutations
import tsp_nearest_neighbor
import tmp


def test_tsp_random_permutations():
    inputs = [(485, 475), (1150, 750), (1008, 480), (1562, 134), (1155, 523)]
    shortest_distance, indexes = tsp_random_permutations.calc_distance_random_permutations(inputs)
    route = " ".join(indexes)
    assert "0 2 3 4 1 0" == route


def test_tsp_twoopt():
    inputs = [(485, 475), (1150, 750), (1008, 480), (1562, 134), (1155, 523)]
    shortest_distance, indexes = tsp_twoopt.tsp_two_opt(inputs)
    route = " ".join(map(str, indexes))
    known_good = "0 1 4 3 2 0"
    assert known_good == route or known_good == route[::-1]


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


def test_compare_bruteforce_vs_twoopt():
    # inputs = [(485, 475), (1150, 750), (1008, 480), (1562, 134), (1155, 523)]
    inputs = [(477, 626), (49, 45), (1065, 568), (1247, 547), (29, 722), (1578, 692), (359, 145), (666, 822), (1312, 675), (1345, 27)]
    # inputs = [(1777, 789), (1640, 329), (1423, 735), (668, 217), (1655, 906), (945, 948), (1085, 124), (216, 965), (730, 401), (725, 360), (1611, 399), (909, 720), (1369, 174), (106, 296), (402, 285), (299, 162), (1352, 972), (259, 959), (114, 990), (1455, 766), (1287, 344), (1728, 914), (1004, 879), (1068, 687), (495, 653), (679, 43), (258, 443), (1630, 588), (1435, 254), (924, 792), (1686, 666), (754, 689), (171, 143), (276, 308), (554, 140), (759, 747), (1609, 695), (1540, 365), (1739, 886), (1068, 641), (354, 632), (1079, 606), (1331, 445), (1745, 592), (65, 454), (1084, 685), (1572, 569), (409, 933), (163, 879), (204, 420)]

    print("Running brute force")
    cost_bf, indexes_bf = tsp_bruteforce.calc_distance_brute_force(inputs)
    print("Cost brute force:", cost_bf)

    print("Running two opt")
    cost_to, indexes_to = tsp_twoopt.tsp_two_opt(inputs, randomize=True)
    print("Cost two opt:", cost_to)


if __name__ == "__main__":
    test_tsp_twoopt()

    test_compare_bruteforce_vs_twoopt()
    pass
