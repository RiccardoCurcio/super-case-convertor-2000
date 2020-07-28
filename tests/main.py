import unittest
from converter import case

class TestCaseConverter(unittest.TestCase):

    def test_snake(self):
        string_snake = "string_case"
        string_raw = "String Case"
        string_custom = "string!!case"

        string_camel = "stringCase"
        string_pascal = "StringCase"
        string_kebab = "string-case"
        # string_flat = "snakecase"
        string_path = "string/case"
        string_piped = "stringCase"
        # string_custom_between = "snakeCase"
        # open = '<'
        # close = '>'
        string_sentence = "String case"
        string_title = "stringCase"
        string_raw = "String Case"

        self.assertEqual(case.snake(string=string_camel), 'string_case')
        self.assertEqual(case.snake(string=string_raw), 'string_case')
        self.assertEqual(case.snake(string=string_custom, replaceSeparator='!!'), 'string_case')
        self.assertEqual(case.snake(string=string_camel), 'string_case')
        self.assertEqual(case.snake(string=string_pascal), 'string_case')
        self.assertEqual(case.snake(string=string_kebab), 'string_case')
        self.assertEqual(case.snake(string=string_path, replaceSeparator='/'), 'string_case')
        self.assertEqual(case.snake(string=string_piped), 'string_case')
        self.assertEqual(case.snake(string=string_sentence), 'string_case')
        self.assertEqual(case.snake(string=string_title), 'string_case')
        self.assertEqual(case.snake(string=string_raw), 'string_case')

    def test_camel(self):
        string_snake = "string_case"
        string_raw = "String Case"
        string_custom = "string!!case"

        string_camel = "stringCase"
        string_pascal = "StringCase"
        string_kebab = "string-case"
        # string_flat = "snakecase"
        string_path = "string/case"
        string_piped = "stringCase"
        # string_custom_between = "snakeCase"
        # open = '<'
        # close = '>'
        string_sentence = "String case"
        string_title = "stringCase"
        string_raw = "String Case"

        self.assertEqual(case.camel(string=string_camel), 'stringCase')
        self.assertEqual(case.camel(string=string_raw), 'stringCase')
        self.assertEqual(case.camel(string=string_custom, replaceSeparator='!!'), 'stringCase')
        self.assertEqual(case.camel(string=string_camel), 'stringCase')
        self.assertEqual(case.camel(string=string_pascal), 'stringCase')
        self.assertEqual(case.camel(string=string_kebab), 'stringCase')
        self.assertEqual(case.camel(string=string_path, replaceSeparator='/'), 'stringCase')
        self.assertEqual(case.camel(string=string_piped), 'stringCase')
        self.assertEqual(case.camel(string=string_sentence), 'stringCase')
        self.assertEqual(case.camel(string=string_title), 'stringCase')
        self.assertEqual(case.camel(string=string_raw), 'stringCase')

    def test_pascal(self):
        string_snake = "string_case"
        string_raw = "String Case"
        string_custom = "string!!case"

        string_camel = "stringCase"
        string_pascal = "StringCase"
        string_kebab = "string-case"
        # string_flat = "snakecase"
        string_path = "string/case"
        string_piped = "stringCase"
        # string_custom_between = "snakeCase"
        # open = '<'
        # close = '>'
        string_sentence = "String case"
        string_title = "stringCase"
        string_raw = "String Case"

        self.assertEqual(case.pascal(string=string_camel), 'StringCase')
        self.assertEqual(case.pascal(string=string_raw), 'StringCase')
        self.assertEqual(case.pascal(string=string_custom, replaceSeparator='!!'), 'StringCase')
        self.assertEqual(case.pascal(string=string_camel), 'StringCase')
        self.assertEqual(case.pascal(string=string_pascal), 'StringCase')
        self.assertEqual(case.pascal(string=string_kebab), 'StringCase')
        self.assertEqual(case.pascal(string=string_path, replaceSeparator='/'), 'StringCase')
        self.assertEqual(case.pascal(string=string_piped), 'StringCase')
        self.assertEqual(case.pascal(string=string_sentence), 'StringCase')
        self.assertEqual(case.pascal(string=string_title), 'StringCase')
        self.assertEqual(case.pascal(string=string_raw), 'StringCase')

    def test_kebab(self):
        string_snake = "string_case"
        string_raw = "String Case"
        string_custom = "string!!case"

        string_camel = "stringCase"
        string_pascal = "StringCase"
        string_kebab = "string-case"
        # string_flat = "snakecase"
        string_path = "string/case"
        string_piped = "stringCase"
        # string_custom_between = "snakeCase"
        # open = '<'
        # close = '>'
        string_sentence = "String case"
        string_title = "stringCase"
        string_raw = "String Case"

        self.assertEqual(case.kebab(string=string_camel), 'string-case')
        self.assertEqual(case.kebab(string=string_raw), 'string-case')
        self.assertEqual(case.kebab(string=string_custom, replaceSeparator='!!'), 'string-case')
        self.assertEqual(case.kebab(string=string_camel), 'string-case')
        self.assertEqual(case.kebab(string=string_pascal), 'string-case')
        self.assertEqual(case.kebab(string=string_kebab), 'string-case')
        self.assertEqual(case.kebab(string=string_path, replaceSeparator='/'), 'string-case')
        self.assertEqual(case.kebab(string=string_piped), 'string-case')
        self.assertEqual(case.kebab(string=string_sentence), 'string-case')
        self.assertEqual(case.kebab(string=string_title), 'string-case')
        self.assertEqual(case.kebab(string=string_raw), 'string-case')

    def test_flat(self):
        string_snake = "string_case"
        string_raw = "String Case"
        string_custom = "string!!case"

        string_camel = "stringCase"
        string_pascal = "StringCase"
        string_kebab = "string-case"
        # string_flat = "snakecase"
        string_path = "string/case"
        string_piped = "stringCase"
        # string_custom_between = "snakeCase"
        # open = '<'
        # close = '>'
        string_sentence = "String case"
        string_title = "stringCase"
        string_raw = "String Case"

        self.assertEqual(case.flat(string=string_camel), 'stringcase')
        self.assertEqual(case.flat(string=string_raw), 'stringcase')
        self.assertEqual(case.flat(string=string_custom, replaceSeparator='!!'), 'stringcase')
        self.assertEqual(case.flat(string=string_camel), 'stringcase')
        self.assertEqual(case.flat(string=string_pascal), 'stringcase')
        self.assertEqual(case.flat(string=string_kebab), 'stringcase')
        self.assertEqual(case.flat(string=string_path, replaceSeparator='/'), 'stringcase')
        self.assertEqual(case.flat(string=string_piped), 'stringcase')
        self.assertEqual(case.flat(string=string_sentence), 'stringcase')
        self.assertEqual(case.flat(string=string_title), 'stringcase')
        self.assertEqual(case.flat(string=string_raw), 'stringcase')

if __name__ == '__main__':
    unittest.main()
