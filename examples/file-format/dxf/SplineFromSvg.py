####################################################################################################
#
# Patro - A Python library to make patterns for fashion design
# Copyright (C) 2019 Fabrice Salvaire
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

####################################################################################################

def spline_from_svg(scene_importer):

    # m 74.999689,150.7821
    # c
    # 9,-10 14.500002,-5 18.916662,-0.83334 4.41667,4.16667 7.749999,7.5 11.083339,5.83334
    # 3.33333,-1.66667 6.66666,-8.33334 13.33333,-11.66667 6.66667,-3.33333 16.66667,-3.33333
    # 16.66667,-3.33333

    # Vector2D[40. 50.]
    # Vector2D[49. 60.]
    # Vector2D[54.500002 55.      ]
    # Vector2D[58.916662 50.83334 ]
    # Vector2D[63.333332 46.66667 ]
    # Vector2D[66.666661 43.33334 ]
    # Vector2D[70.000001 45.      ]
    # Vector2D[73.333331 46.66667 ]
    # Vector2D[76.666661 53.33334 ]
    # Vector2D[83.333331 56.66667 ]
    # Vector2D[90.000001 60.      ]
    # Vector2D[100.000001  60.      ]
    # Vector2D[100.000001  60.      ]

    # CubicBezier2D(Vector2D[40. 50.], Vector2D[49. 60.], Vector2D[54.5 55. ], Vector2D[58.91666667 50.83333333])
    # CubicBezier2D(Vector2D[58.91666667 50.83333333], Vector2D[63.33333333 46.66666667], Vector2D[66.66666667 43.33333333], Vector2D[70. 45.])
    # CubicBezier2D(Vector2D[70. 45.], Vector2D[73.33333333 46.66666667], Vector2D[76.66666667 53.33333333], Vector2D[83.33333333 56.66666667])
    # CubicBezier2D(Vector2D[83.33333333 56.66666667], Vector2D[90. 60.], Vector2D[100.  60.], Vector2D[100.  60.])

    x0, y0 = 40, 50
    control_points = (
        (9, -10),
        (14.500002, -5),
        (18.916662, -0.83334),

        (4.41667, 4.16667),
        (7.749999, 7.5),
        (11.083339, 5.83334),

        (3.33333, -1.66667),
        (6.66666, -8.33334),
        (13.33333, -11.66667),

        (6.66667, -3.33333),
        (16.66667, -3.33333),
        (16.66667, -3.33333),
    )

    vertices = []
    point = Vector2D(x0, y0)
    vertices.append(point)
    for i, xy in enumerate(control_points):
        xi, yi = xy
        yi = -yi
        if (i+1) % 3:
            x = xi + x0
            y = yi + y0
        else:
            x0 += xi
            y0 += yi
            x, y = x0, y0
        point = Vector2D(x, y)
        vertices.append(point)

    path_style = GraphicBezierStyle(
        line_width=3.0,
        stroke_color=Colors.blue,
        stroke_style=StrokeStyle.SolidLine,
        show_control=True,
        control_color=Colors.red,
    )

    for vertex in vertices:
        print(vertex)
    # scene_importer.scene.bezier_path(vertices, degree=3, path_style=path_style, user_data=None)
