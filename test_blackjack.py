from unittest import TestCase, main
from unittest.mock import patch
from test_helper import run_test

class TestBlackjack(TestCase):

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_example(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand less than 21.
        The dealer wins by having a higher hand than the user.

        This does not count as one of your tests.
        '''
        output = run_test([3, 5, 8], ['y', 'n'], [3, 5, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "You have 8. Hit (y/n)? y\n" \
                   "Drew an 8\n" \
                   "You have 16. Hit (y/n)? n\n" \
                   "Final hand: 16.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "Dealer has 8.\n" \
                   "Drew a 10\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_my_code(self, input_mock, randint_mock):
        '''
        The player wins because the player gets below 21 and the dealer busts.
        '''
        output = run_test([2, 9, 6], ['y','n'], [9, 6, 8], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 2\n" \
                   "Drew a 9\n" \
                   "You have 11. Hit (y/n)? y\n" \
                   "Drew a 6\n" \
                   "You have 17. Hit (y/n)? n\n" \
                   "Final hand: 17.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 9\n" \
                   "Drew a 6\n" \
                   "Dealer has 15.\n" \
                   "Drew an 8\n" \
                   "Final hand: 23.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_my_code(self, input_mock, randint_mock):
        '''
        The game ends as push because both dealer and the player get blackjack
        '''
        output = run_test([10, 8, 3], ['y','n'], [10, 6, 5], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 10\n" \
                   "Drew an 8\n" \
                   "You have 18. Hit (y/n)? y\n" \
                   "Drew a 3\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 10\n" \
                   "Drew a 6\n" \
                   "Dealer has 16.\n" \
                   "Drew a 5\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Push.\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_my_code(self, input_mock, randint_mock):
        '''
        The game ends as push because both dealer and the player get the same final hand
        '''
        output = run_test([2, 9, 6], ['y','n'], [9, 5, 3], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 2\n" \
                   "Drew a 9\n" \
                   "You have 11. Hit (y/n)? y\n" \
                   "Drew a 6\n" \
                   "You have 17. Hit (y/n)? n\n" \
                   "Final hand: 17.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 9\n" \
                   "Drew a 5\n" \
                   "Dealer has 14.\n" \
                   "Drew a 3\n" \
                   "Final hand: 17.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Push.\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_my_code(self, input_mock, randint_mock):
        '''
        The player wins because the player has a higher hand than the dealer
        '''
        output = run_test([2, 9, 9], ['y','n'], [9, 6, 3], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 2\n" \
                   "Drew a 9\n" \
                   "You have 11. Hit (y/n)? y\n" \
                   "Drew a 9\n" \
                   "You have 20. Hit (y/n)? n\n" \
                   "Final hand: 20.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 9\n" \
                   "Drew a 6\n" \
                   "Dealer has 15.\n" \
                   "Drew a 3\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)
    
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_my_code(self, input_mock, randint_mock):
        '''
        The player wins because the player has blackjack and the dealer has a hand below 21
        '''
        output = run_test([2, 9, 10], ['y'], [9, 6, 3], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 2\n" \
                   "Drew a 9\n" \
                   "You have 11. Hit (y/n)? y\n" \
                   "Drew a 10\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 9\n" \
                   "Drew a 6\n" \
                   "Dealer has 15.\n" \
                   "Drew a 3\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_my_code(self, input_mock, randint_mock):
        '''
        The dealer wins because the dealer has blackjack and the player is below 21
        '''
        output = run_test([2, 9, 9], ['y','n'], [9, 6, 6], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 2\n" \
                   "Drew a 9\n" \
                   "You have 11. Hit (y/n)? y\n" \
                   "Drew a 9\n" \
                   "You have 20. Hit (y/n)? n\n" \
                   "Final hand: 20.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 9\n" \
                   "Drew a 6\n" \
                   "Dealer has 15.\n" \
                   "Drew a 6\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_my_code(self, input_mock, randint_mock):
        '''
       The dealer wins because the dealer has a higher hand than the player
        '''
        output = run_test([2, 9, 5], ['y','n'], [9, 6, 5], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 2\n" \
                   "Drew a 9\n" \
                   "You have 11. Hit (y/n)? y\n" \
                   "Drew a 5\n" \
                   "You have 16. Hit (y/n)? n\n" \
                   "Final hand: 16.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 9\n" \
                   "Drew a 6\n" \
                   "Dealer has 15.\n" \
                   "Drew a 5\n" \
                   "Final hand: 20.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)
        self.assertEqual(output, expected)
    
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_my_code(self, input_mock, randint_mock):
        '''
        The dealer wins because the player busts and the dealer is under 21
        '''
        output = run_test([9, 9, 9], ['y'], [9, 6, 3], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 9\n" \
                   "Drew a 9\n" \
                   "You have 18. Hit (y/n)? y\n" \
                   "Drew a 9\n" \
                   "Final hand: 27.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 9\n" \
                   "Drew a 6\n" \
                   "Dealer has 15.\n" \
                   "Drew a 3\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_my_code(self, input_mock, randint_mock):
        '''
        The dealer wins because both player and dealer bust
        '''
        output = run_test([9, 9, 9], ['y'], [9, 6, 9], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 9\n" \
                   "Drew a 9\n" \
                   "You have 18. Hit (y/n)? y\n" \
                   "Drew a 9\n" \
                   "Final hand: 27.\n" \
                   "BUST.\n"\
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 9\n" \
                   "Drew a 6\n" \
                   "Dealer has 15.\n" \
                   "Drew a 9\n" \
                   "Final hand: 24.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_my_code(self, input_mock, randint_mock):
        '''
        The player wins because the player has blackjack and the dealer busts
        '''
        output = run_test([3, 9, 9], ['y'], [9, 6, 9], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 9\n" \
                   "You have 12. Hit (y/n)? y\n" \
                   "Drew a 9\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 9\n" \
                   "Drew a 6\n" \
                   "Dealer has 15.\n" \
                   "Drew a 9\n" \
                   "Final hand: 24.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_my_code(self, input_mock, randint_mock):
        '''
        The dealer wins because the dealer has blackjack and the player busts.
        '''
        output = run_test([9, 9, 9], ['y','n'], [9, 6, 6], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 9\n" \
                   "Drew a 9\n" \
                   "You have 18. Hit (y/n)? y\n" \
                   "Drew a 9\n" \
                   "Final hand: 27.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 9\n" \
                   "Drew a 6\n" \
                   "Dealer has 15.\n" \
                   "Drew a 6\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)



if __name__ == '__main__':
    main()