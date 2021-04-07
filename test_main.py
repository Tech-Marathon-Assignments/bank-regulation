from main import main

# Test Case 1:
# Input: 21 10000000 True 24 100000000
# Output: "Qualified"
def test_main_1(capfd):
    main(21, 10000000, True, 24, 100000000)
    out, err = capfd.readouterr()
    assert out == "Qualified\n"

# Test Case 2:
# Input: 18 10000000 False 12 100000000
# Output: "Unqualified"
def test_main_2(capfd):
    main(18, 10000000, False, 12, 100000000)
    out, err = capfd.readouterr()
    assert out == "Unqualified\n"
