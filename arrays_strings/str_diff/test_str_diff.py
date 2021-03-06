from nose.tools import assert_equal, assert_raises

class Solution(object):

    def find_diff(self, s, t):
        if s is None or t is None:
            raise TypeError('Error!')
        a1 = list(s)
        a2 = list(t)
        for char in a1:
            if char not in a2:
                return char
            a2.remove(char)
        if len(a2):
            return a2[0]
        else:
            return False

class TestFindDiff(object):

    def test_find_diff(self):
        solution = Solution()
        assert_raises(TypeError, solution.find_diff, None)
        assert_equal(solution.find_diff('abcd', 'abcde'), 'e')
        assert_equal(solution.find_diff('aaabbcdd', 'abdbacade'), 'e')
        print('Success: test_find_diff')


def main():
    test = TestFindDiff()
    test.test_find_diff()


if __name__ == '__main__':
    main()