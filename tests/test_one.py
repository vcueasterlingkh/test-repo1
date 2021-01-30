from testrepo1 import one


class TestClass:

    def test_add_two_3_4(self):
        """Tests Add two values together and returns the values."""
        assert one.add_two(3, 4) == 7

    def test_add_three_3_4_5(self):
        """Tests Add three values together and returns the values."""
        assert one.add_three(3, 4, 5) == 12
