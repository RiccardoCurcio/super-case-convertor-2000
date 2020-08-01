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


from converter.src.snake import snake
from converter.src.camel import camel
from converter.src.pascal import pascal
from converter.src.kebab import kebab
from converter.src.flat import flat
from converter.src.raw import raw
from converter.src.path import path
from converter.src.piped import piped
from converter.src.custom import custom
from converter.src.customBetween import customBetween
from converter.src.sentence import sentence
from converter.src.title import title

class case(
    snake,
    camel,
    pascal,
    kebab,
    flat,
    raw,
    path,
    piped,
    custom,
    customBetween,
    sentence,
    title
    ):
    pass
