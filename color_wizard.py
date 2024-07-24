import colorgram as cor

colors = cor.extract("img.png", 4)
for color in range(len(colors)):
    colors[color] = (colors[color].rgb.r, colors[color].rgb.g, colors[color].rgb.b)
print(colors)

color_rgb_list = [(2, 241, 235),
                  (223, 104, 174),
                  (134, 52, 129),
                  (39, 39, 76),
                  ]

# color_rgb_list = [(243, 220, 203),
#                   (128, 86, 61),
#                   (185, 160, 137),
#                   (28, 30, 37),
#                   (66, 41, 24),
#                   (66, 97, 125),
#                   (45, 31, 48),
#                   (181, 139, 56),
#                   (59, 93, 81),
#                   (103, 44, 27),
#                   (111, 96, 104),
#                   (165, 150, 154),
#                   (226, 210, 214),
#                   (141, 121, 118),
#                   (39, 42, 41),
#                   (208, 185, 179),
#                   (80, 64, 44),
#                   (147, 156, 164),
#                   (137, 122, 126),
#                   (216, 192, 159),
#                   (207, 211, 216),
#                   (57, 62, 73),
#                   (202, 185, 189),
#                   (154, 162, 153),
#                   (72, 59, 63),
#                   (213, 218, 214),
#                   (120, 126, 140),
#                   (52, 72, 60),
#                   (119, 133, 119),
#                   (190, 189, 198)]

print(len(color_rgb_list))

'''colors_generated = [ < colorgram.py
Color: Rgb(r=243, g=220, b=203), 60.71601970872585 % >, < colorgram.py
Color: Rgb(r=128, g=86, b=61), 11.186123402912003 % >, < colorgram.py
Color: Rgb(r=185, g=160, b=137), 8.708317872432335 % >, < colorgram.py
Color: Rgb(r=28, g=30, b=37), 4.6024563910288006 % >, < colorgram.py
Color: Rgb(r=66, g=41, b=24), 4.418956264572476 % >, < colorgram.py
Color: Rgb(r=66, g=97, b=125), 3.384598911921785 % >, < colorgram.py
Color: Rgb(r=45, g=31, b=48), 1.230595415450563 % >, < colorgram.py
Color: Rgb(r=181, g=139, b=56), 1.1117080095774512 % >, < colorgram.py
Color: Rgb(r=59, g=93, b=81), 1.0278960805923694 % >, < colorgram.py
Color: Rgb(r=103, g=44, b=27), 0.9363306251373019 % >, < colorgram.py
Color: Rgb(r=111, g=96, b=104), 0.931161607490645 % >, < colorgram.py
Color: Rgb(r=165, g=150, b=154), 0.7184934528853272 % >, < colorgram.py
Color: Rgb(r=226, g=210, b=214), 0.3047874333796699 % >, < colorgram.py
Color: Rgb(r=141, g=121, b=118), 0.1491630806606743 % >, < colorgram.py
Color: Rgb(r=39, g=42, b=41), 0.10005741301743251 % >, < colorgram.py
Color: Rgb(r=208, g=185, b=179), 0.09285770986673166 % >, < colorgram.py
Color: Rgb(r=80, g=64, b=44), 0.07808908801914013 % >, < colorgram.py
Color: Rgb(r=147, g=156, b=164), 0.07679683360747588 % >, < colorgram.py
Color: Rgb(r=137, g=122, b=126), 0.06184360398678947 % >, < colorgram.py
Color: Rgb(r=216, g=192, b=159), 0.0516901764665703 % >, < colorgram.py
Color: Rgb(r=207, g=211, b=216), 0.031937144745416646 % >, < colorgram.py
Color: Rgb(r=57, g=62, b=73), 0.029168028148993243 % >, < colorgram.py
Color: Rgb(r=202, g=185, b=189), 0.022337540544482167 % >, < colorgram.py
Color: Rgb(r=154, g=162, b=153), 0.010707250839503848 % >, < colorgram.py
Color: Rgb(r=72, g=59, b=63), 0.005722840965941712 % >, < colorgram.py
Color: Rgb(r=213, g=218, b=214), 0.005353625419751924 % >, < colorgram.py
Color: Rgb(r=120, g=126, b=140), 0.0031383321426131966 % >, < colorgram.py
Color: Rgb(r=52, g=72, b=60), 0.0018460777309489394 % >, < colorgram.py
Color: Rgb(r=119, g=133, b=119), 0.0011076466385693635 % >, < colorgram.py
Color: Rgb(r=190, g=189, b=198), 0.0007384310923795758 % >]
'''
