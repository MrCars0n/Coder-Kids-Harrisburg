import random

common = ["red", "blue", "green", "yellow", "purple", "orange"]

all = ["white", "white smoke", "gainsboro", "light gray", "silver", "dark gray", "gray", "dim gray", "black", "light slate gray", "slate gray", "alice blue", "light steel blue", "cornflower blue", "royal blue", "blue", "medium blue", "navy", "dark blue", "midnight blue", "light blue", "deep sky blue", "dodger blue", "powder blue", "sky blue", "light sky blue", "steel blue", "azure", "light cyan", "cyan", "pale turquoise", "dark turquoise", "turquoise", "medium turquoise", "light sea green", "cadet blue", "dark cyan", "teal", "dark slate gray", "mint cream", "aquamarine", "medium aquamarine", "dark sea green", "medium sea green", "sea green", "honeydew", "pale green", "light green", "medium spring green", "spring green", "lime green", "green", "forest green", "dark green", "green yellow", "chartreuse", "lawn green", "lime", "yellow green", "olive drab", "beige", "dark khaki", "olive", "dark olive green", "pale goldenrod", "khaki", "ivory", "light yellow", "light goldenrod yellow", "cornsilk", "lemon chiffon", "yellow", "gold", "goldenrod", "dark goldenrod", "wheat", "tan", "burlywood", "peru", "sienna", "saddle brown", "floral white", "old lace", "navajo white", "moccasin", "sandy brown", "orange", "dark orange", "chocolate", "firebrick", "brown", "dark red", "maroon", "antique white", "papaya whip", "blanched almond", "bisque", "peach puff", "light salmon", "coral", "tomato", "orange red", "red", "crimson", "dark salmon", "salmon", "light coral", "indian red", "rosy brown", "linen", "seashell", "misty rose", "pink", "light pink", "hot pink", "deep pink", "snow", "lavender blush", "pale violet red", "violet red", "medium violet red", "purple", "dark magenta", "violet", "magenta", "thistle", "plum", "orchid", "medium orchid", "dark orchid", "dark violet", "blue violet", "medium purple", "rebecca purple", "indigo", "ghost white", "lavender", "light slate blue", "medium slate blue", "slate blue", "dark slate blue"]

def randomCommon():
  return common[random.randint(0, len(common) - 1)]

def randomColor():
  return all[random.randint(0,140)]
  
def randomRGBColor():
  rgb = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
  return rgb
  
  