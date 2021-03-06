from nose.tools import assert_equal

def compress_string(string):
  if string is None or not string:
      return string
  result = ''
  prevChar = string[0]
  count = 0;
  for char in string:
      if char == prevChar:
          count += 1
      else:
          result += helper(prevChar, count)
          prevChar = char
          count = 1
  result += helper(prevChar, count)
  return result if len(result) < len(string) else string
            
            
def helper(prevChar, count):
  if (count == 2):
    return prevChar + prevChar
  else:
    return (prevChar + (str(count) if count > 2 else ''))



class TestCompress(object):

    def test_compress(self, func):
        assert_equal(func(None), None)
        assert_equal(func(''), '')
        assert_equal(func('AABBCC'), 'AABBCC')
        assert_equal(func('AAABCCDDDD'), 'A3BCCD4')
        print('Success: test_compress')


def main():
    test = TestCompress()
    test.test_compress(compress_string)


if __name__ == '__main__':
    main()