from datetime import datetime

class TestCase:
    def __init__(self, input, output):
        self.input = input
        self.output = output

"""
   Run tests given test cases and test function.

    Args:
        test_cases (list[TestCase]): The string to check.

    Prints test results to the console.
"""
def test_runner(test_cases: list[TestCase], func: callable):
    test_count = len(test_cases)
    failed_tests = 0
    passed_tests = 0

    for test_case in test_cases:
        input = test_case['input']
        expected_output = test_case['output']
        test_status = 'FAILED'

        print(f'Input: {input}')
        start_time = datetime.now()
        output = func(input)
        end_time = datetime.now()
        print(f'Expected output: {expected_output}, actual output: {output}')

        if expected_output == output:
            test_status = 'PASSED'
            passed_tests += 1
        else:
            failed_tests += 1
        
        print(f'Test Status: {test_status}\n\n')
    
    print(f'Total tests run: {test_count}, Passed: {passed_tests}, Failed: {failed_tests}, Time: {end_time - start_time}')