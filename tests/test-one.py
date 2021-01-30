from test-repo1 import one


class TestClass:

    def test_add_two_1(self):
        assert one.add_two(3, 4) == 7

    def test_add_three_1(self):
        assert one.add_three(3, 4, 5) == 12
