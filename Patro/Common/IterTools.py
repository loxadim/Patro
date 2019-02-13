####################################################################################################
#
# Patro - A Python library to make patterns for fashion design
# Copyright (C) 2017 Fabrice Salvaire
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
####################################################################################################

# Note: useless code was removed

####################################################################################################

__all__ = [
    'pairwise', # used in Patro/GeometryEngine/Line.py
]

####################################################################################################

from itertools import tee

####################################################################################################

def pairwise(iterable):

    """Return a generator which generate a pair wise list from an iterable.

    s -> (s[0],s[1]), (s[1],s[2]), ... (s[N-1],s[N])

    """

    prev = iterable[0]
    for x in iterable[1:]:
        yield prev, x
        prev = x

####################################################################################################

def closed_pairwise(iterable):

    """Return a generator which generate a closed pair wise list from an iterable.

    s -> (s[0],s[1]), (s[1],s[2]), ... (s[N], s[0])

    """

    return pairwise(list(iterable) + [iterable[0]])

####################################################################################################

def multiwise(iterable, n=2):

    """Return a generator which generate a multi wise list from an iterable.

    s -> (s[0],s[1],s[2],...), (s[1],s[2],s[3],...), ... (...,s[N-2],s[N-1],s[N])

    Examples::

      a = (1,2,3,4,5)

      list(multiwise(a, n=1))
      # [(1,), (2,), (3,), (4,), (5,)]

      list(multiwise(a, n=2))
      # [(1, 2), (2, 3), (3, 4), (4, 5)]

      list(multiwise(a, n=3))
      # [(1, 2, 3), (2, 3, 4), (3, 4, 5)]

      # list(multiwise(a, n=4))
      # [(1, 2, 3, 4), (2, 3, 4, 5)]

      list(multiwise(a, n=5))
      # [(1, 2, 3, 4, 5)]

      list(multiwise(a, n=6))
      # []

      list(multiwise(a, n=0))
      # []

    """

    # Create n iterators on iterable
    iterators = tee(iterable, n)
    # Increment the iterators according to their positions
    for i, iterator in enumerate(iterators):
        for j in range(i):
            next(iterator, None) # Fixme: does None prevent StopIteration to be raised ?

    # Return the aggregate
    #   zip stops when the shortest iterator is exhausted
    return zip(*iterators)
