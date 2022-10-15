import tsp


def test_tsp():

    inputs = [(485, 475), (1150, 750), (1008, 480), (1562, 134), (1155, 523)]
    route = tsp.calc_distance_nearest_neighbor(inputs)
    assert "0 2 4 1 3 0" == route


if __name__ == "__main__":
    test_tsp()
