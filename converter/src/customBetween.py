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
from converter.src.sentence import sentence
import re


class customBetween(object):
    @staticmethod
    def custom_between(
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
        replaceSeparator : Optional[str]
            If is not None peplace `replaceSeparator` with `_`

        Returns
        -------
        list
            List of strings.

        """

        listOf = sentence.sentence(
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
