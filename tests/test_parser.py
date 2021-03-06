import unittest
import exercises.parser as exparser
import testdata


class TestParser(unittest.TestCase):

    def assertSuccess(self, msg=None):
        self.assertTrue(True, msg)


    def test_number_parser(self):
        parser = exparser.NumberParser()

        numbers = ['5', '22', '49', '55', '30']

        for number in numbers:
            try:
                parser.parse(number)
            except Exception as e:
                self.fail(e)


    def test_number_parser_should_reject_non_number_input(self):
        string = 'potato'
        parser = exparser.NumberParser()

        with self.assertRaises(ValueError):
            parser.parse(string)


    def test_parser_should_accept_correctly_formatted_input(self):
        source_file = testdata.TEST_PARSER_DATA_1 
        parser = exparser.FileParser()

        with open(source_file, mode='r') as handle:
            try:
                parser.parse(handle)
            except Exception as e:
                self.fail(e)

    
    def test_parser_should_reject_bad_file_input(self):
        source_file = testdata.TEST_PARSER_DATA_2
        parser = exparser.FileParser()

        with open(source_file, mode='r') as handle:
            with self.assertRaises(Exception):
                parser.parse(handle)

    
    def test_parser_should_fail_if_input_length_mismatch(self):
        source_file = testdata.TEST_PARSER_DATA_3
        parser = exparser.FileParser()

        with open(source_file, mode='r') as handle:
            with self.assertRaises(ValueError):
                parser.parse(handle)
    