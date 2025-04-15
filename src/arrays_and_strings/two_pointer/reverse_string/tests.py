import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../')))

from solution import is_palindrome_1, is_palindrome_2
from src.utils.test_runner import test_runner

test_cases = [
    {
        'input': 'racecar',
        'output': True
    },
    {
        'input': '',
        'output': True
    },
    {
        'input': 'TheQuickBrownFox',
        'output': False
    },
    {
        'input': 'HhHh',
        'output': False
    },
    {
        'input': 'm',
        'output': True
    },
    {
        'input': "".join(map(str, range(100, 0, -1))),
        'output': False
    }
]


def test():
    test_runner(test_cases=test_cases, func=is_palindrome_2)

test()

