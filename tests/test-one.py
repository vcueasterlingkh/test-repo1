from testrepo1 import one


class TestClass:

    def testAddTwo_3_4(self):
        assert one.add_two(3, 4) == 7

    def testAddThree_3_4_5(self):
        assert one.add_three(3, 4, 5) == 12
