from nose.tools import assert_equal, assert_raises

class Solution(object):

    def fizz_buzz(self, num):
        if num is None:
            raise TypeError("num is None")
        if num is 0:
            raise ValueError("num is 0")

        result = []
        for i in xrange(1, num + 1):
            if i % 15 == 0:
                result.append('FizzBuzz')
            elif i % 5 == 0:
                result.append('Buzz')
            elif i % 3 == 0:
                result.append('Fizz')
            else:
                result.append(str(i))

        return result

class TestFizzBuzz(object):

    def test_fizz_buzz(self):
        solution = Solution()
        assert_raises(TypeError, solution.fizz_buzz, None)
        assert_raises(ValueError, solution.fizz_buzz, 0)
        expected = [
            '1',
            '2',
            'Fizz',
            '4',
            'Buzz',
            'Fizz',
            '7',
            '8',
            'Fizz',
            'Buzz',
            '11',
            'Fizz',
            '13',
            '14',
            'FizzBuzz'
        ]
        assert_equal(solution.fizz_buzz(15), expected)
        print('Success: test_fizz_buzz')


def main():
    test = TestFizzBuzz()
    test.test_fizz_buzz()


if __name__ == '__main__':
    main()
