from colorgram import colorgram

colors = colorgram.extract("./hirst.jpg", 20)
for color in colors:
    print(color.rgb)
