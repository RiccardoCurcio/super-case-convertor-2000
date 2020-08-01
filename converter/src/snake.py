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
import re


class snake(object):

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

        string = string.replace('|', '_')
        string = string.replace('/', '_')
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
        string = re.sub(r'^(_{1,})', '', string)
        return str(string)

    """ Define alias for snake """
    c_case = snake
