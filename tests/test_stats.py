import unittest

from stats import get_num_words, get_char_count, get_sorted_char_count


class TestStatsFunctions(unittest.TestCase):

    def test_get_num_words(self):
        self.assertEqual(get_num_words("Hello world"), 2)
        self.assertEqual(get_num_words("This is a test sentence."), 5)
        self.assertEqual(get_num_words(""), 0)
        self.assertEqual(get_num_words("OneWord"), 1)

    def test_get_char_count(self):
        text = "Hello"
        expected_count = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
        self.assertEqual(get_char_count(text), expected_count)

    def test_get_sorted_char_count(self):
        text = "banana"
        char_count = get_char_count(text)
        sorted_chars = get_sorted_char_count(char_count)
        expected_sorted = [('a', 3), ('n', 2), ('b', 1)]
        self.assertEqual(sorted_chars, expected_sorted)


if __name__ == "__main__":
    unittest.main()
