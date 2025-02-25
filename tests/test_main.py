import unittest

from main import analyze_text


class TestMainFunctions(unittest.TestCase):

    def test_analyze_text(self):
        text = "Hello world!"
        word_count, sorted_chars = analyze_text(text)

        # Check word count
        self.assertEqual(word_count, 2)

        # Check character count
        expected_sorted_chars = [('l', 3), ('o', 2), ('h', 1), ('e', 1), ('w', 1), ('r', 1), ('d', 1)]
        self.assertEqual(sorted_chars, expected_sorted_chars)


if __name__ == "__main__":
    unittest.main()
