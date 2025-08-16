import unittest
from sudoku.generator import PuzzleGenerator

class TestPuzzleGenerator(unittest.TestCase):

    def setUp(self):
        self.generator = PuzzleGenerator()

    def test_generate_unique_solution(self):
        puzzle = self.generator.generate_puzzle()
        self.assertTrue(self.generator.has_unique_solution(puzzle))

    def test_difficulty_classification(self):
        easy_puzzle = self.generator.generate_puzzle(difficulty='easy')
        medium_puzzle = self.generator.generate_puzzle(difficulty='medium')
        hard_puzzle = self.generator.generate_puzzle(difficulty='hard')

        self.assertEqual(self.generator.classify_difficulty(easy_puzzle), 'easy')
        self.assertEqual(self.generator.classify_difficulty(medium_puzzle), 'medium')
        self.assertEqual(self.generator.classify_difficulty(hard_puzzle), 'hard')

    def test_generate_valid_puzzle(self):
        puzzle = self.generator.generate_puzzle()
        self.assertIsNotNone(puzzle)
        self.assertEqual(len(puzzle), 9)
        for row in puzzle:
            self.assertEqual(len(row), 9)

if __name__ == '__main__':
    unittest.main()