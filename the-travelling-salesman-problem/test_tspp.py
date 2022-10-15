import tssp


def test_tssp():

    inputs = [(9, 12), (24, 15), (12, 30), (4, 3), (13, 27)]
    total_distance = tssp.calc_distance_nearest_neighbor(inputs)

    assert 71 == total_distance


if __name__ == "__main__":
    test_tssp()
