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


from typing import Union, Optional
from converter.src.snake import snake
import re


class sentence(object):
    @staticmethod
    def sentence(
        string: str = "",
        listMode: bool = False,
        capitalize: bool = False,
        upper: bool = False,
        replaceSeparator: Optional[str] = None
    ) -> Union[str, list]:
        """Convert string to a list of strings or string,
         string separated by spaces.

        Parameters
        ----------
        string : str
            String to convert.
        listMode : bool
            If listMode is True return a list of strings.
        capitalize : bool
            If capitalize is True capitalize all strings.
        upper : bool
            If upper is True convert to uppercase all strings.
        replaceSeparator : Optional[str]
            If is not None peplace `replaceSeparator` with `_`

        Returns
        -------
        Union[str, list]
            String separated by space or list of strings.

        """
        listOrString = (
            snake.snake(
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
