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


class raw(object):
    @staticmethod
    def raw(string: str = "", replaceSeparator: Optional[str] = None) -> str:
        """Convert string to raw case.

        Parameters
        ----------
        string : str
            String to convert.
        replaceSeparator : Optional[str]
            If is not None peplace `replaceSeparator` with `_`

        Returns
        -------
        str
            String converted to raw case.

        """
        string = snake.snake(string=string, replaceSeparator=replaceSeparator)
        string = string.replace('_', ' ')
        return string
