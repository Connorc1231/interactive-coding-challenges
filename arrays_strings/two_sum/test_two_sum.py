from nose.tools import assert_equal, assert_raises

class Solution(object):

    def two_sum(self, nums, val):
        if nums is None:
            raise TypeError('ERROR! Type None')
        if len(nums) == 0:
            raise ValueError('ERROR! Empty array')
        results = []
        for ind1, i in enumerate(nums):
            for ind2, j in enumerate(nums): 
                if i + j == val and (ind1 not in results and ind2 not in results):
                    results.append(ind1)
                    results.append(ind2)
        return results


class TestTwoSum(object):

    def test_two_sum(self):
        solution = Solution()
        assert_raises(TypeError, solution.two_sum, None, None)
        assert_raises(ValueError, solution.two_sum, [], 0)
        target = 7
        nums = [1, 3, 2, -7, 5]
        expected = [2, 4]
        assert_equal(solution.two_sum(nums, target), expected)
        print('Success: test_two_sum')


def main():
    test = TestTwoSum()
    test.test_two_sum()


if __name__ == '__main__':
    main()