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
        string_path = "string/case"
        string_piped = "string|case"
        string_sentence = "String case"
        string_title = "stringCase"
        string_raw = "String Case"

        self.assertEqual(case.snake(string=string_camel), 'string_case')
        self.assertEqual(case.snake(string=string_raw), 'string_case')
        self.assertEqual(
            case.snake(
                string=string_custom,
                replaceSeparator='!!'
                ),
            'string_case'
        )
        self.assertEqual(case.snake(string=string_camel), 'string_case')
        self.assertEqual(case.snake(string=string_pascal), 'string_case')
        self.assertEqual(case.snake(string=string_kebab), 'string_case')
        self.assertEqual(
            case.snake(
                string=string_path,
            ),
            'string_case'
        )
        self.assertEqual(case.snake(string=string_piped), 'string_case')
        self.assertEqual(case.snake(string=string_sentence), 'string_case')
        self.assertEqual(case.snake(string=string_title), 'string_case')
        self.assertEqual(case.snake(string=string_raw), 'string_case')

        # alias
        self.assertEqual(case.c_case(string=string_camel), 'string_case')
        self.assertEqual(case.c_case(string=string_raw), 'string_case')
        self.assertEqual(
            case.c_case(
                string=string_custom,
                replaceSeparator='!!'
                ),
            'string_case'
        )
        self.assertEqual(case.c_case(string=string_camel), 'string_case')
        self.assertEqual(case.c_case(string=string_pascal), 'string_case')
        self.assertEqual(case.c_case(string=string_kebab), 'string_case')
        self.assertEqual(
            case.c_case(
                string=string_path
            ),
            'string_case'
        )
        self.assertEqual(case.c_case(string=string_piped), 'string_case')
        self.assertEqual(case.c_case(string=string_sentence), 'string_case')
        self.assertEqual(case.c_case(string=string_title), 'string_case')
        self.assertEqual(case.c_case(string=string_raw), 'string_case')

    def test_camel(self):
        string_snake = "string_case"
        string_raw = "String Case"
        string_custom = "string!!case"
        string_camel = "stringCase"
        string_pascal = "StringCase"
        string_kebab = "string-case"
        string_path = "string/case"
        string_piped = "string|case"
        string_sentence = "String case"
        string_title = "stringCase"
        string_raw = "String Case"

        self.assertEqual(case.camel(string=string_camel), 'stringCase')
        self.assertEqual(case.camel(string=string_raw), 'stringCase')
        self.assertEqual(
            case.camel(
                string=string_custom,
                replaceSeparator='!!'
            ),
            'stringCase'
            )
        self.assertEqual(case.camel(string=string_camel), 'stringCase')
        self.assertEqual(case.camel(string=string_pascal), 'stringCase')
        self.assertEqual(case.camel(string=string_kebab), 'stringCase')
        self.assertEqual(
            case.camel(
                string=string_path
            ),
            'stringCase'
        )
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
        string_path = "string/case"
        string_piped = "string|case"
        string_sentence = "String case"
        string_title = "stringCase"
        string_raw = "String Case"

        self.assertEqual(case.pascal(string=string_camel), 'StringCase')
        self.assertEqual(case.pascal(string=string_raw), 'StringCase')
        self.assertEqual(
            case.pascal(
                string=string_custom,
                replaceSeparator='!!'
            ),
            'StringCase'
        )
        self.assertEqual(case.pascal(string=string_camel), 'StringCase')
        self.assertEqual(case.pascal(string=string_pascal), 'StringCase')
        self.assertEqual(case.pascal(string=string_kebab), 'StringCase')
        self.assertEqual(
            case.pascal(
                string=string_path
            ),
            'StringCase'
        )
        self.assertEqual(case.pascal(string=string_piped), 'StringCase')
        self.assertEqual(case.pascal(string=string_sentence), 'StringCase')
        self.assertEqual(case.pascal(string=string_title), 'StringCase')
        self.assertEqual(case.pascal(string=string_raw), 'StringCase')

        # alias

        self.assertEqual(case.capital_camel(string=string_camel), 'StringCase')
        self.assertEqual(case.capital_camel(string=string_raw), 'StringCase')
        self.assertEqual(
            case.capital_camel(
                string=string_custom,
                replaceSeparator='!!'
            ),
            'StringCase'
        )
        self.assertEqual(case.capital_camel(string=string_camel), 'StringCase')
        self.assertEqual(
            case.capital_camel(
                string=string_pascal
            ),
            'StringCase'
        )
        self.assertEqual(case.capital_camel(string=string_kebab), 'StringCase')
        self.assertEqual(
            case.capital_camel(
                string=string_path
            ),
            'StringCase'
        )
        self.assertEqual(case.capital_camel(string=string_piped), 'StringCase')
        self.assertEqual(
            case.capital_camel(
                string=string_sentence
            ),
            'StringCase'
        )
        self.assertEqual(case.capital_camel(string=string_title), 'StringCase')
        self.assertEqual(case.capital_camel(string=string_raw), 'StringCase')

    def test_kebab(self):
        string_snake = "string_case"
        string_raw = "String Case"
        string_custom = "string!!case"
        string_camel = "stringCase"
        string_pascal = "StringCase"
        string_kebab = "string-case"
        string_path = "string/case"
        string_piped = "string|case"
        string_sentence = "String case"
        string_title = "stringCase"
        string_raw = "String Case"

        self.assertEqual(case.kebab(string=string_camel), 'string-case')
        self.assertEqual(case.kebab(string=string_raw), 'string-case')
        self.assertEqual(
            case.kebab(
                string=string_custom,
                replaceSeparator='!!'
            ),
            'string-case'
        )
        self.assertEqual(case.kebab(string=string_camel), 'string-case')
        self.assertEqual(case.kebab(string=string_pascal), 'string-case')
        self.assertEqual(case.kebab(string=string_kebab), 'string-case')
        self.assertEqual(
            case.kebab(
                string=string_path
            ),
            'string-case'
        )
        self.assertEqual(case.kebab(string=string_piped), 'string-case')
        self.assertEqual(case.kebab(string=string_sentence), 'string-case')
        self.assertEqual(case.kebab(string=string_title), 'string-case')
        self.assertEqual(case.kebab(string=string_raw), 'string-case')

        # alias
        self.assertEqual(case.caterpillar(string=string_camel), 'string-case')
        self.assertEqual(case.caterpillar(string=string_raw), 'string-case')
        self.assertEqual(
            case.caterpillar(
                string=string_custom,
                replaceSeparator='!!'
            ),
            'string-case'
        )
        self.assertEqual(case.caterpillar(string=string_camel), 'string-case')
        self.assertEqual(case.caterpillar(string=string_pascal), 'string-case')
        self.assertEqual(case.caterpillar(string=string_kebab), 'string-case')
        self.assertEqual(
            case.caterpillar(
                string=string_path
            ),
            'string-case'
        )
        self.assertEqual(case.caterpillar(string=string_piped), 'string-case')
        self.assertEqual(
            case.caterpillar(
                string=string_sentence
            ),
            'string-case'
        )
        self.assertEqual(case.caterpillar(string=string_title), 'string-case')
        self.assertEqual(case.caterpillar(string=string_raw), 'string-case')

        self.assertEqual(case.dash(string=string_camel), 'string-case')
        self.assertEqual(case.dash(string=string_raw), 'string-case')
        self.assertEqual(
            case.dash(
                string=string_custom,
                replaceSeparator='!!'
            ),
            'string-case'
        )
        self.assertEqual(case.dash(string=string_camel), 'string-case')
        self.assertEqual(case.dash(string=string_pascal), 'string-case')
        self.assertEqual(case.dash(string=string_kebab), 'string-case')
        self.assertEqual(
            case.dash(
                string=string_path
            ),
            'string-case'
        )
        self.assertEqual(case.dash(string=string_piped), 'string-case')
        self.assertEqual(case.dash(string=string_sentence), 'string-case')
        self.assertEqual(case.dash(string=string_title), 'string-case')
        self.assertEqual(case.dash(string=string_raw), 'string-case')

        self.assertEqual(case.hyphen(string=string_camel), 'string-case')
        self.assertEqual(case.hyphen(string=string_raw), 'string-case')
        self.assertEqual(
            case.hyphen(
                string=string_custom,
                replaceSeparator='!!'
            ),
            'string-case'
        )
        self.assertEqual(case.hyphen(string=string_camel), 'string-case')
        self.assertEqual(case.hyphen(string=string_pascal), 'string-case')
        self.assertEqual(case.hyphen(string=string_kebab), 'string-case')
        self.assertEqual(
            case.hyphen(
                string=string_path
            ),
            'string-case'
        )
        self.assertEqual(case.hyphen(string=string_piped), 'string-case')
        self.assertEqual(case.hyphen(string=string_sentence), 'string-case')
        self.assertEqual(case.hyphen(string=string_title), 'string-case')
        self.assertEqual(case.hyphen(string=string_raw), 'string-case')

        self.assertEqual(case.lisp(string=string_camel), 'string-case')
        self.assertEqual(case.lisp(string=string_raw), 'string-case')
        self.assertEqual(
            case.lisp(
                string=string_custom,
                replaceSeparator='!!'
            ),
            'string-case'
        )
        self.assertEqual(case.lisp(string=string_camel), 'string-case')
        self.assertEqual(case.lisp(string=string_pascal), 'string-case')
        self.assertEqual(case.lisp(string=string_kebab), 'string-case')
        self.assertEqual(
            case.lisp(
                string=string_path
            ),
            'string-case'
        )
        self.assertEqual(case.lisp(string=string_piped), 'string-case')
        self.assertEqual(case.lisp(string=string_sentence), 'string-case')
        self.assertEqual(case.lisp(string=string_title), 'string-case')
        self.assertEqual(case.lisp(string=string_raw), 'string-case')

        self.assertEqual(case.spinal(string=string_camel), 'string-case')
        self.assertEqual(case.spinal(string=string_raw), 'string-case')
        self.assertEqual(
            case.spinal(
                string=string_custom,
                replaceSeparator='!!'
            ),
            'string-case'
        )
        self.assertEqual(case.spinal(string=string_camel), 'string-case')
        self.assertEqual(case.spinal(string=string_pascal), 'string-case')
        self.assertEqual(case.spinal(string=string_kebab), 'string-case')
        self.assertEqual(
            case.spinal(
                string=string_path
            ),
            'string-case'
        )
        self.assertEqual(case.spinal(string=string_piped), 'string-case')
        self.assertEqual(case.spinal(string=string_sentence), 'string-case')
        self.assertEqual(case.spinal(string=string_title), 'string-case')
        self.assertEqual(case.spinal(string=string_raw), 'string-case')

        self.assertEqual(case.css(string=string_camel), 'string-case')
        self.assertEqual(case.css(string=string_raw), 'string-case')
        self.assertEqual(
            case.css(
                string=string_custom,
                replaceSeparator='!!'
            ),
            'string-case'
        )
        self.assertEqual(case.css(string=string_camel), 'string-case')
        self.assertEqual(case.css(string=string_pascal), 'string-case')
        self.assertEqual(case.css(string=string_kebab), 'string-case')
        self.assertEqual(
            case.css(
                string=string_path
            ),
            'string-case'
        )
        self.assertEqual(case.css(string=string_piped), 'string-case')
        self.assertEqual(case.css(string=string_sentence), 'string-case')
        self.assertEqual(case.css(string=string_title), 'string-case')
        self.assertEqual(case.css(string=string_raw), 'string-case')

    def test_flat(self):
        string_snake = "string_case"
        string_raw = "String Case"
        string_custom = "string!!case"
        string_camel = "stringCase"
        string_pascal = "StringCase"
        string_kebab = "string-case"
        string_path = "string/case"
        string_piped = "string|case"
        string_sentence = "String case"
        string_title = "stringCase"
        string_raw = "String Case"

        self.assertEqual(case.flat(string=string_camel), 'stringcase')
        self.assertEqual(case.flat(string=string_raw), 'stringcase')
        self.assertEqual(
            case.flat(
                string=string_custom,
                replaceSeparator='!!'
            ),
            'stringcase'
        )
        self.assertEqual(case.flat(string=string_camel), 'stringcase')
        self.assertEqual(case.flat(string=string_pascal), 'stringcase')
        self.assertEqual(case.flat(string=string_kebab), 'stringcase')
        self.assertEqual(
            case.flat(
                string=string_path
            ),
            'stringcase'
        )
        self.assertEqual(case.flat(string=string_piped), 'stringcase')
        self.assertEqual(case.flat(string=string_sentence), 'stringcase')
        self.assertEqual(case.flat(string=string_title), 'stringcase')
        self.assertEqual(case.flat(string=string_raw), 'stringcase')

    def test_raw(self):
        string_snake = "string_case"
        string_raw = "String Case"
        string_custom = "string!!case"
        string_camel = "stringCase"
        string_pascal = "StringCase"
        string_kebab = "string-case"
        string_path = "string/case"
        string_piped = "string|case"
        string_sentence = "String case"
        string_title = "stringCase"
        string_raw = "String Case"

        self.assertEqual(case.raw(string=string_camel), 'string case')
        self.assertEqual(case.raw(string=string_raw), 'string case')
        self.assertEqual(
            case.raw(
                string=string_custom,
                replaceSeparator='!!'
            ),
            'string case'
        )
        self.assertEqual(case.raw(string=string_camel), 'string case')
        self.assertEqual(case.raw(string=string_pascal), 'string case')
        self.assertEqual(case.raw(string=string_kebab), 'string case')
        self.assertEqual(
            case.raw(
                string=string_path
            ),
            'string case'
        )
        self.assertEqual(case.raw(string=string_piped), 'string case')
        self.assertEqual(case.raw(string=string_sentence), 'string case')
        self.assertEqual(case.raw(string=string_title), 'string case')
        self.assertEqual(case.raw(string=string_raw), 'string case')

    def test_path(self):
        string_snake = "string_case"
        string_raw = "String Case"
        string_custom = "string!!case"
        string_camel = "stringCase"
        string_pascal = "StringCase"
        string_kebab = "string-case"
        string_path = "string/case"
        string_piped = "string|case"
        string_sentence = "String case"
        string_title = "stringCase"
        string_raw = "String Case"

        self.assertEqual(case.path(string=string_camel), 'string/case')
        self.assertEqual(case.path(string=string_raw), 'string/case')
        self.assertEqual(
            case.path(
                string=string_custom,
                replaceSeparator='!!'
            ),
            'string/case'
        )
        self.assertEqual(case.path(string=string_camel), 'string/case')
        self.assertEqual(case.path(string=string_pascal), 'string/case')
        self.assertEqual(case.path(string=string_kebab), 'string/case')
        self.assertEqual(
            case.path(
                string=string_path
            ),
            'string/case'
        )
        self.assertEqual(case.path(string=string_piped), 'string/case')
        self.assertEqual(case.path(string=string_sentence), 'string/case')
        self.assertEqual(case.path(string=string_title), 'string/case')
        self.assertEqual(case.path(string=string_raw), 'string/case')

    def test_piped(self):
        string_snake = "string_case"
        string_raw = "String Case"
        string_custom = "string!!case"
        string_camel = "stringCase"
        string_pascal = "StringCase"
        string_kebab = "string-case"
        string_path = "string/case"
        string_piped = "string|case"
        string_sentence = "String case"
        string_title = "stringCase"
        string_raw = "String Case"

        self.assertEqual(case.piped(string=string_camel), 'string|case')
        self.assertEqual(case.piped(string=string_raw), 'string|case')
        self.assertEqual(
            case.piped(
                string=string_custom,
                replaceSeparator='!!'
            ),
            'string|case'
        )
        self.assertEqual(case.piped(string=string_camel), 'string|case')
        self.assertEqual(case.piped(string=string_pascal), 'string|case')
        self.assertEqual(case.piped(string=string_kebab), 'string|case')
        self.assertEqual(
            case.piped(
                string=string_path
            ),
            'string|case'
        )
        self.assertEqual(case.piped(string=string_piped), 'string|case')
        self.assertEqual(case.piped(string=string_sentence), 'string|case')
        self.assertEqual(case.piped(string=string_title), 'string|case')
        self.assertEqual(case.piped(string=string_raw), 'string|case')

    def test_custom(self):
        string_snake = "string_case"
        string_raw = "String Case"
        string_custom = "string!!case"
        string_camel = "stringCase"
        string_pascal = "StringCase"
        string_kebab = "string-case"
        string_path = "string/case"
        string_piped = "string|case"
        string_sentence = "String case"
        string_title = "stringCase"
        string_raw = "String Case"

        self.assertEqual(
            case.custom(
                string=string_camel,
                separator='<#>'
            ),
            'string<#>case'
        )
        self.assertEqual(
            case.custom(
                string=string_raw,
                separator='<#>'
            ),
            'string<#>case'
        )
        self.assertEqual(
            case.custom(
                string=string_custom,
                separator='<#>',
                replaceSeparator='!!'
            ),
            'string<#>case'
        )
        self.assertEqual(
            case.custom(
                string=string_camel,
                separator='<#>'
            ),
            'string<#>case'
        )
        self.assertEqual(
            case.custom(
                string=string_pascal,
                separator='<#>'
            ),
            'string<#>case'
        )
        self.assertEqual(
            case.custom(
                string=string_kebab,
                separator='<#>'
            ),
            'string<#>case'
        )
        self.assertEqual(
            case.custom(
                string=string_path,
                separator='<#>'
            ),
            'string<#>case'
        )
        self.assertEqual(
            case.custom(
                string=string_piped,
                separator='<#>'
            ),
            'string<#>case'
        )
        self.assertEqual(
            case.custom(
                string=string_sentence,
                separator='<#>'
            ),
            'string<#>case'
        )
        self.assertEqual(
            case.custom(
                string=string_title,
                separator='<#>'
            ),
            'string<#>case'
        )
        self.assertEqual(
            case.custom(
                string=string_raw,
                separator='<#>'
            ),
            'string<#>case'
        )

    def test_custom_between(self):
        string_snake = "string_case"
        string_raw = "String Case"
        string_custom = "string!!case"
        string_camel = "stringCase"
        string_pascal = "StringCase"
        string_kebab = "string-case"
        string_path = "string/case"
        string_piped = "string|case"
        string_sentence = "String case"
        string_title = "stringCase"
        string_raw = "String Case"

        self.assertEqual(
            case.custom_between(
                string=string_camel,
                open='<',
                close='>'
            ),
            ['<string>', '<case>']
        )
        self.assertEqual(
            case.custom_between(
                string=string_raw,
                open='<',
                close='>'
            ),
            ['<string>', '<case>']
        )
        self.assertEqual(
            case.custom_between(
                string=string_custom,
                open='<',
                close='>',
                replaceSeparator='!!'
            ),
            ['<string>', '<case>']
        )
        self.assertEqual(
            case.custom_between(
                string=string_camel,
                open='<',
                close='>'
            ),
            ['<string>', '<case>']
        )
        self.assertEqual(
            case.custom_between(
                string=string_pascal,
                open='<',
                close='>'
            ),
            ['<string>', '<case>']
        )
        self.assertEqual(
            case.custom_between(
                string=string_kebab,
                open='<',
                close='>'
            ),
            ['<string>', '<case>']
        )
        self.assertEqual(
            case.custom_between(
                string=string_path,
                open='<',
                close='>'
            ),
            ['<string>', '<case>']
        )
        self.assertEqual(
            case.custom_between(
                string=string_piped,
                open='<',
                close='>'
            ),
            ['<string>', '<case>']
        )
        self.assertEqual(
            case.custom_between(
                string=string_sentence,
                open='<',
                close='>'
            ),
            ['<string>', '<case>']
        )
        self.assertEqual(
            case.custom_between(
                string=string_title,
                open='<',
                close='>'
            ),
            ['<string>', '<case>']
        )
        self.assertEqual(
            case.custom_between(
                string=string_raw,
                open='<',
                close='>'
            ),
            ['<string>', '<case>']
        )

    def test_title(self):
        string_snake = "string_case"
        string_raw = "String Case"
        string_custom = "string!!case"
        string_camel = "stringCase"
        string_pascal = "StringCase"
        string_kebab = "string-case"
        string_path = "string/case"
        string_piped = "string|case"
        string_sentence = "String case"
        string_title = "stringCase"
        string_raw = "String Case"

        self.assertEqual(case.title(string=string_camel), 'String Case')
        self.assertEqual(case.title(string=string_raw), 'String Case')
        self.assertEqual(
            case.title(
                string=string_custom,
                replaceSeparator='!!'
            ),
            'String Case'
        )
        self.assertEqual(case.title(string=string_camel), 'String Case')
        self.assertEqual(case.title(string=string_pascal), 'String Case')
        self.assertEqual(case.title(string=string_kebab), 'String Case')
        self.assertEqual(
            case.title(
                string=string_path
            ),
            'String Case'
        )
        self.assertEqual(case.title(string=string_piped), 'String Case')
        self.assertEqual(case.title(string=string_sentence), 'String Case')
        self.assertEqual(case.title(string=string_title), 'String Case')
        self.assertEqual(case.title(string=string_raw), 'String Case')

    def test_sentence(self):
        string_snake = "string_case"
        string_raw = "String Case"
        string_custom = "string!!case"
        string_camel = "stringCase"
        string_pascal = "StringCase"
        string_kebab = "string-case"
        string_path = "string/case"
        string_piped = "string|case"
        string_sentence = "String case"
        string_title = "stringCase"
        string_raw = "String Case"

        self.assertEqual(case.sentence(string=string_camel), 'String case')
        self.assertEqual(case.sentence(string=string_raw), 'String case')
        self.assertEqual(
            case.sentence(
                string=string_custom,
                replaceSeparator='!!'
            ),
            'String case'
        )
        self.assertEqual(case.sentence(string=string_camel), 'String case')
        self.assertEqual(case.sentence(string=string_pascal), 'String case')
        self.assertEqual(case.sentence(string=string_kebab), 'String case')
        self.assertEqual(
            case.sentence(
                string=string_path
            ),
            'String case'
        )
        self.assertEqual(case.sentence(string=string_piped), 'String case')
        self.assertEqual(case.sentence(string=string_sentence), 'String case')
        self.assertEqual(case.sentence(string=string_title), 'String case')
        self.assertEqual(case.sentence(string=string_raw), 'String case')

    def test_sentence_capitalize(self):
        string_snake = "string_case"
        string_raw = "String Case"
        string_custom = "string!!case"
        string_camel = "stringCase"
        string_pascal = "StringCase"
        string_kebab = "string-case"
        string_path = "string/case"
        string_piped = "string|case"
        string_sentence = "String case"
        string_title = "stringCase"
        string_raw = "String Case"

        self.assertEqual(
            case.sentence(
                string=string_camel,
                capitalize=True
            ),
            'String Case'
        )
        self.assertEqual(
            case.sentence(
                string=string_raw,
                capitalize=True
            ),
            'String Case'
        )
        self.assertEqual(
            case.sentence(
                string=string_custom,
                capitalize=True,
                replaceSeparator='!!'
            ),
            'String Case'
        )
        self.assertEqual(
            case.sentence(
                string=string_camel,
                capitalize=True
            ),
            'String Case'
        )
        self.assertEqual(
            case.sentence(
                string=string_pascal,
                capitalize=True
            ),
            'String Case'
        )
        self.assertEqual(
            case.sentence(
                string=string_kebab,
                capitalize=True
            ),
            'String Case'
        )
        self.assertEqual(
            case.sentence(
                string=string_path,
                capitalize=True
            ),
            'String Case'
        )
        self.assertEqual(
            case.sentence(
                string=string_piped,
                capitalize=True
            ),
            'String Case'
        )
        self.assertEqual(
            case.sentence(
                string=string_sentence,
                capitalize=True
                ),
            'String Case'
        )
        self.assertEqual(
            case.sentence(
                string=string_title,
                capitalize=True
                ),
            'String Case'
        )
        self.assertEqual(
            case.sentence(
                string=string_raw,
                capitalize=True
                ),
            'String Case'
        )

    def test_sentence_upper(self):
        string_snake = "string_case"
        string_raw = "String Case"
        string_custom = "string!!case"
        string_camel = "stringCase"
        string_pascal = "StringCase"
        string_kebab = "string-case"
        string_path = "string/case"
        string_piped = "string|case"
        string_sentence = "String case"
        string_title = "stringCase"
        string_raw = "String Case"

        self.assertEqual(
            case.sentence(
                string=string_camel,
                upper=True
            ),
            'STRING CASE'
        )
        self.assertEqual(
            case.sentence(
                string=string_raw,
                upper=True
            ),
            'STRING CASE'
        )
        self.assertEqual(
            case.sentence(
                string=string_custom,
                upper=True,
                replaceSeparator='!!'
            ),
            'STRING CASE'
        )
        self.assertEqual(
            case.sentence(
                string=string_camel,
                upper=True
            ),
            'STRING CASE'
        )
        self.assertEqual(
            case.sentence(
                string=string_pascal,
                upper=True
            ),
            'STRING CASE'
        )
        self.assertEqual(
            case.sentence(
                string=string_kebab,
                upper=True
            ),
            'STRING CASE'
        )
        self.assertEqual(
            case.sentence(
                string=string_path,
                upper=True
            ),
            'STRING CASE'
        )
        self.assertEqual(
            case.sentence(
                string=string_piped,
                upper=True
            ),
            'STRING CASE'
        )
        self.assertEqual(
            case.sentence(
                string=string_sentence,
                upper=True
            ),
            'STRING CASE'
        )
        self.assertEqual(
            case.sentence(
                string=string_title,
                upper=True
            ),
            'STRING CASE'
        )
        self.assertEqual(
            case.sentence(
                string=string_raw,
                upper=True
            ),
            'STRING CASE'
        )

    def test_sentence_listmode(self):
        string_snake = "string_case"
        string_raw = "String Case"
        string_custom = "string!!case"
        string_camel = "stringCase"
        string_pascal = "StringCase"
        string_kebab = "string-case"
        string_path = "string/case"
        string_piped = "string|case"
        string_sentence = "String case"
        string_title = "stringCase"
        string_raw = "String Case"

        self.assertEqual(
            case.sentence(
                string=string_camel,
                listMode=True
            ),
            ['String', 'case']
        )
        self.assertEqual(
            case.sentence(
                string=string_raw,
                listMode=True
            ),
            ['String', 'case']
        )
        self.assertEqual(
            case.sentence(
                string=string_custom,
                listMode=True,
                replaceSeparator='!!'
            ),
            ['String', 'case']
        )
        self.assertEqual(
            case.sentence(
                string=string_camel,
                listMode=True
            ),
            ['String', 'case']
        )
        self.assertEqual(
            case.sentence(
                string=string_pascal,
                listMode=True
            ),
            ['String', 'case']
        )
        self.assertEqual(
            case.sentence(
                string=string_kebab,
                listMode=True
            ),
            ['String', 'case']
        )
        self.assertEqual(
            case.sentence(
                string=string_path,
                listMode=True
            ),
            ['String', 'case']
        )
        self.assertEqual(
            case.sentence(
                string=string_piped,
                listMode=True
            ),
            ['String', 'case']
        )
        self.assertEqual(
            case.sentence(
                string=string_sentence,
                listMode=True
            ),
            ['String', 'case']
        )
        self.assertEqual(
            case.sentence(
                string=string_title,
                listMode=True
            ),
            ['String', 'case']
        )
        self.assertEqual(
            case.sentence(
                string=string_raw,
                listMode=True
            ),
            ['String', 'case']
        )

    def test_sentence_listmode_capitalize(self):
        string_snake = "string_case"
        string_raw = "String Case"
        string_custom = "string!!case"
        string_camel = "stringCase"
        string_pascal = "StringCase"
        string_kebab = "string-case"
        string_path = "string/case"
        string_piped = "string|case"
        string_sentence = "String case"
        string_title = "stringCase"
        string_raw = "String Case"

        self.assertEqual(
            case.sentence(
                string=string_camel,
                listMode=True,
                capitalize=True
            ),
            ['String', 'Case']
        )
        self.assertEqual(
            case.sentence(
                string=string_raw,
                listMode=True,
                capitalize=True
            ),
            ['String', 'Case']
        )
        self.assertEqual(
            case.sentence(
                string=string_custom,
                listMode=True,
                capitalize=True,
                replaceSeparator='!!'
            ),
            ['String', 'Case']
        )
        self.assertEqual(
            case.sentence(
                string=string_camel,
                listMode=True,
                capitalize=True
            ),
            ['String', 'Case']
        )
        self.assertEqual(
            case.sentence(
                string=string_pascal,
                listMode=True,
                capitalize=True
            ),
            ['String', 'Case']
        )
        self.assertEqual(
            case.sentence(
                string=string_kebab,
                listMode=True,
                capitalize=True
            ),
            ['String', 'Case']
        )
        self.assertEqual(
            case.sentence(
                string=string_path,
                listMode=True,
                capitalize=True
            ),
            ['String', 'Case']
        )
        self.assertEqual(
            case.sentence(
                string=string_piped,
                listMode=True,
                capitalize=True
            ),
            ['String', 'Case']
        )
        self.assertEqual(
            case.sentence(
                string=string_sentence,
                listMode=True,
                capitalize=True
            ),
            ['String', 'Case']
        )
        self.assertEqual(
            case.sentence(
                string=string_title,
                listMode=True,
                capitalize=True
            ),
            ['String', 'Case']
        )
        self.assertEqual(
            case.sentence(
                string=string_raw,
                listMode=True,
                capitalize=True
            ),
            ['String', 'Case']
        )

    def test_sentence_listmode_upper(self):
        string_snake = "string_case"
        string_raw = "String Case"
        string_custom = "string!!case"
        string_camel = "stringCase"
        string_pascal = "StringCase"
        string_kebab = "string-case"
        string_path = "string/case"
        string_piped = "string|case"
        string_sentence = "String case"
        string_title = "stringCase"
        string_raw = "String Case"

        self.assertEqual(
            case.sentence(
                string=string_camel,
                listMode=True,
                upper=True
            ),
            ['STRING', 'CASE']
        )
        self.assertEqual(
            case.sentence(
                string=string_raw,
                listMode=True,
                upper=True
            ),
            ['STRING', 'CASE']
        )
        self.assertEqual(
            case.sentence(
                string=string_custom,
                listMode=True,
                upper=True,
                replaceSeparator='!!'
            ),
            ['STRING', 'CASE']
        )
        self.assertEqual(
            case.sentence(
                string=string_camel,
                listMode=True,
                upper=True
            ),
            ['STRING', 'CASE']
        )
        self.assertEqual(
            case.sentence(
                string=string_pascal,
                listMode=True,
                upper=True
            ),
            ['STRING', 'CASE']
        )
        self.assertEqual(
            case.sentence(
                string=string_kebab,
                listMode=True,
                upper=True
            ),
            ['STRING', 'CASE']
        )
        self.assertEqual(
            case.sentence(
                string=string_path,
                listMode=True,
                upper=True
            ),
            ['STRING', 'CASE']
        )
        self.assertEqual(
            case.sentence(
                string=string_piped,
                listMode=True,
                upper=True
            ),
            ['STRING', 'CASE']
        )
        self.assertEqual(
            case.sentence(
                string=string_sentence,
                listMode=True,
                upper=True
            ),
            ['STRING', 'CASE']
        )
        self.assertEqual(
            case.sentence(
                string=string_title,
                listMode=True,
                upper=True
            ),
            ['STRING', 'CASE']
        )
        self.assertEqual(
            case.sentence(
                string=string_raw,
                listMode=True,
                upper=True
            ),
            ['STRING', 'CASE']
        )


if __name__ == '__main__':
    unittest.main()
