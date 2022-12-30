from unary import encode


def test_unary():
    assert encode("C") == "0 0 00 0000 0 00"
    assert encode("%") == "00 0 0 0 00 00 0 0 00 0 0 0"


if __name__ == "__main__":
    test_unary()
    