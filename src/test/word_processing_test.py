import unittest
import os
import sys
sys.path.append('..')

from  word_processing import WORD_PROCESSING


class TestWordProcessing(unittest.TestCase):

    def test_byte_count(self):
        filepath = os.path.join(os.path.dirname(__file__), '../test.txt')
        wp = WORD_PROCESSING(filepath)
        
        self.assertEqual(
            wp.byte_count,
            342190, 'File size incorrect')
        
    def test_line_count(self):
        filepath = os.path.join(os.path.dirname(__file__), '../test.txt')
        wp = WORD_PROCESSING(filepath)

        self.assertEqual(
            wp.line_count,
            7145, 'Number of lines incorrect')

    def test_words_count(self):
        filepath = os.path.join(os.path.dirname(__file__), '../test.txt')
        wp = WORD_PROCESSING(filepath)

        self.assertEqual(
            wp.word_count,
            58164, 'Number of words incorrect')

    def test_chars_count(self):
        filepath = os.path.join(os.path.dirname(__file__), '../test.txt')
        wp = WORD_PROCESSING(filepath)

        self.assertEqual(
            wp.char_count,
            339292, 'Number of characters incorrect')


if __name__ == '__main__':
    unittest.main()