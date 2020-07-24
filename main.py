# Copyright (c) 2020 <Riccardo Curcio>
#
# GNU GENERAL PUBLIC LICENSE
#    Version 3, 29 June 2007
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.



"""
flatcase
kebab-case. Also called caterpillar-case, dash-case, hyphen-case, lisp-case, spinal-case and css-case
camelCase
PascalCase or CapitalCamelCase
snake_case or c_case
# MACRO_CASE or UPPER_CASE
# COBOL-CASE or TRAIN-CASE
pathcase
sentencecase
"""
from typing import Union, Optional
import re


class case(object):

    @staticmethod
    def snake(string: str = "", replaceSeparator: Optional[str] = None) -> str:
        """Convert string to snake case.

        Parameters
        ----------
        string : str
            String to convert.
        replaceSeparator : Optional[str]
            If is not None peplace `replaceSeparator` with `_`

        Returns
        -------
        str
            String converted to snake case.

        """
        if replaceSeparator is not None:
            string = string.replace(replaceSeparator, '_')

        string = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', string)
        string = str(re.sub('([a-z0-9])([A-Z])', r'\1_\2', string).lower())
        string = re.sub(
            r'([0-9]{1,})+',
            lambda m: "_{}_".format(m.group(1)),
            string
        )
        string = re.sub(r'( {1,})+', '_', string)
        string = re.sub(r'(-{1,})+', '_', string)
        string = re.sub(r'(_{1,})+', '_', string)
        string = re.sub(r'(_{1,})$', '', string)
        string = re.sub(r'^(_{1,})', '', string)
        return str(string)

    """ Define alias for snake """
    cCase = snake

    @staticmethod
    def camel(string: str = "", replaceSeparator: Optional[str] = None) -> str:
        """Convert string to camel case.

        Parameters
        ----------
        string : str
            String to convert.

        Returns
        -------
        str
            String converted to camel case.

        """
        string = case.snake(string=string, replaceSeparator=replaceSeparator)
        string = re.sub('_([a-zA-Z0-9])', lambda m: m.group(1).upper(), string)
        return string

    @staticmethod
    def pascal(string: str = "", replaceSeparator: Optional[str] = None) -> str:
        """Convert string to pascal case.

        Parameters
        ----------
        string : str
            String to convert.

        Returns
        -------
        str
            String converted to pascal case.

        """
        string = case.snake(string=string, replaceSeparator=replaceSeparator)
        string = case.camel(string)
        string = "{}{}".format(string[0].upper(), string[1:])
        return string

    """Define alias for capitalCamel"""
    capitalCamel = pascal

    @staticmethod
    def kebab(string: str = "", replaceSeparator: Optional[str] = None) -> str:
        """Convert string to kebab case.

        Parameters
        ----------
        string : str
            String to convert.

        Returns
        -------
        str
            String converted to kebab case.

        """
        string = case.snake(string=string, replaceSeparator=replaceSeparator)
        string = string.replace('_', '-')
        return string

    """Define alias for kebab"""

    caterpillar = kebab
    dash = kebab
    hyphen = kebab
    lisp = kebab
    spinal = kebab
    css = kebab

    @staticmethod
    def flat(string: str = "", replaceSeparator: Optional[str] = None) -> str:
        """Convert string to flat case.

        Parameters
        ----------
        string : str
            String to convert.

        Returns
        -------
        str
            String converted to flat case.

        """
        string = case.snake(string=string, replaceSeparator=replaceSeparator)
        string = string.replace('_', '')
        return string

    @staticmethod
    def path(string: str = "", replaceSeparator: Optional[str] = None) -> str:
        """Convert string to path.

        Parameters
        ----------
        string : str
            String to convert.

        Returns
        -------
        str
            String converted to path.

        """
        string = case.snake(string=string, replaceSeparator=replaceSeparator)
        string = string.replace('_', '/')
        return string

    @staticmethod
    def piped(string: str = "", replaceSeparator: Optional[str] = None) -> str:
        """Convert string to piped string.

        Parameters
        ----------
        string : str
            String to convert.

        Returns
        -------
        str
            String converted to piped string.

        """
        string = case.snake(string=string, replaceSeparator=replaceSeparator)
        string = string.replace('_', '|')

        return string

    @staticmethod
    def custom(
        string: str = "",
        separator: str = "",
        replaceSeparator: Optional[str] = None
    ) -> str:
        """Convert string from snake case to custom separator.

        Parameters
        ----------
        string : str
            String to convert.
        separator : str
            Separator.

        Returns
        -------
        str
            String converted to separator.

        """
        string = case.snake(string=string, replaceSeparator=replaceSeparator)
        string = string.replace('_', separator)

        return string

    @staticmethod
    def customBetween(
        string: str = "",
        open: str = "",
        close: Optional[str] = None,
        replaceSeparator: Optional[str] = None
    ) -> list:
        """Convert string to a list of strings
        Each element of the list between open and close value.

        Parameters
        ----------
        string : str
            String to convert.
        open : str
            Opening character.
        close : Optional[str]
            Closing character if `close` is None will become equal to `open`.

        Returns
        -------
        list
            List of strings.

        """

        listOf = case.sentence(
            string=string,
            listMode=True,
            replaceSeparator=replaceSeparator
        )
        close = close if close else open
        listOf = list(
            map(
                lambda x: str("{}{}{}".format(open, x.lower(), close)),
                listOf
            )
        )
        return listOf

    @staticmethod
    def sentence(
        string: str = "",
        listMode: bool = False,
        capitalize: bool = False,
        upper: bool = False,
        replaceSeparator: Optional[str] = None
    ) -> Union[str, list]:
        """Convert string to a list of strings or string string separated by spaces.

        Parameters
        ----------
        string : str
            String to convert.
        listMode : bool
            If listMode is True return a list of strings.
        capitalize : bool
            If capitalize is True capitalize all strings.
        upper : bool
            If upper is True convert to uppercase all strings..

        Returns
        -------
        Union[str, list]
            String separated by space or list of strings.

        """
        listOrString = (
            case.snake(
                string=string,
                replaceSeparator=replaceSeparator
            )
        ).capitalize()
        listOrString = listOrString.replace('_', ' ')

        if capitalize is True:
            listOrString = listOrString.capitalize()
            listOrString = re.sub(
                ' ([a-zA-Z0-9])',
                lambda m: " {}".format(m.group(1).capitalize()),
                listOrString
            )

        if upper is True:
            listOrString = listOrString.upper()
            listOrString = re.sub(
                ' ([a-zA-Z0-9])',
                lambda m: " {}".format(m.group(1).upper()),
                listOrString
            )

        if listMode is True:
            listOrString = listOrString.split(' ')

        return listOrString

    @staticmethod
    def title(string: str = "", replaceSeparator: Optional[str] = None) -> str:
        """Convert string to title case.

        Parameters
        ----------
        string : str
            String to convert..

        Returns
        -------
        str
            String converted to title case.

        """
        return case.sentence(
            string=string,
            capitalize=True,
            replaceSeparator=replaceSeparator
        )


strings = [
    "Ciao mi chiamo riccardo-Curcio? ho 35? anni!",
    "-- ciao-mi___chiamo  riccardo-  Curcio ___ ho 35  __ anni",
    "ciao*|*mi*|*chiamo*|*riccardo*|*curcio?*|*ho*|*35*|*?*|*anni!"
]

# print("\n *** kebab *** ")
# for string in strings:
#     print("{} -> {}".format(string, case.caterpillar(string)))

print("\n *** Snake *** ")
for string in strings:
    print("{} -> {}".format(string, case.snake(string=string, replaceSeparator="*|*")))

print("\n *** camel *** ")
for string in strings:
    print("{} -> {}".format(string, case.camel(string)))

print("\n *** pascal *** ")
for string in strings:
    print("{} -> {}".format(string, case.pascal(string)))

print("\n *** kebab *** ")
for string in strings:
    print("{} -> {}".format(string, case.kebab(string)))

print("\n *** flat *** ")
for string in strings:
    print("{} -> {}".format(string, case.flat(string)))

print("\n *** path *** ")
for string in strings:
    print("{} -> {}".format(string, case.path(string)))

print("\n *** sentence *** ")
for string in strings:
    print("{} -> {}".format(string, case.sentence(string)))

print("\n *** sentence capitalize*** ")
for string in strings:
    print("{} -> {}".format(string, case.sentence(string, False, True)))

print("\n *** sentence listMode*** ")
for string in strings:
    print("{} -> {}".format(string, case.sentence(string, True)))

print("\n *** sentence listMode capitalize*** ")
for string in strings:
    print("{} -> {}".format(string, case.sentence(string, True, True)))

print("\n *** sentence listMode upper*** ")
for string in strings:
    print("{} -> {}".format(string, case.sentence(string, True, False, True)))

print("\n *** custom *** ")
for string in strings:
    print("{} -> {}".format(string, case.custom(string, "*|*")))

print("\n *** custom between*** ")
for string in strings:
    print("{} -> {}".format(string, case.customBetween(string=string, open="{:", close="}", replaceSeparator="*|*")))

print("\n *** piped *** ")
for string in strings:
    print("{} -> {}".format(string, case.piped(string)))

print("\n *** title *** ")
for string in strings:
    print("{} -> {}".format(string, case.title(string=string, replaceSeparator="*|*")))
