####################################################################################################
#
# Patro - A Python library to make patterns for fashion design
# Copyright (C) 2019 Fabrice Salvaire
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
#
####################################################################################################

####################################################################################################

from pathlib import Path

from Patro.Common.Logging import Logging
Logging.setup_logging()

from Patro.FileFormat.Svg.SvgFile import SvgFile
from PatroExample import find_data_path

####################################################################################################

# svg_path = find_data_path('patterns-svg', 'veravenus-little-bias-dress.pattern-a0.svg')
svg_path = find_data_path('svg', 'demo.svg')

svg_file = SvgFile(svg_path)
