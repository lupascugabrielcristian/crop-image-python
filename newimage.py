from PIL import Image, ImageDraw, ImageFont

size_W = 1280
size_H = 960

normal_font = ImageFont.truetype("Montserrat-Regular.ttf", 18)
new_image = Image.new("RGB", (size_W,size_H), "#6B6652")
draw = ImageDraw.Draw(new_image)

# Liniile verticale la fiecare 100px
for x in range(0, round(size_W / 100)):
    draw.line([(100 * x, 30), (100 * x, size_H)], "#ccc", 1)
    draw.line([(100 * x + 50, 30), (100 * x + 50, size_H)], "#ccc", 1)
    draw.text((100*x - 10, 10), "x=" + str(100*x), "#999", normal_font)


for y in range(0, round(size_H / 100)):
    draw.line([(0, 100*y), (size_W, 100*y)], "#ccc", 1)
    draw.line([(0, 100*y + 50), (size_W, 100*y + 50)], "#ccc", 1)
    draw.text((10, 100*y-10), "Y=" + str(100*y), "#ce7e00", normal_font)

# Orig Dimensions
original_text = "W="+str(size_W) + "\nH=" + str(size_H)
larger_font = ImageFont.truetype("Montserrat-Regular.ttf", 22)
draw.text((size_W - 140, size_H - 80), original_text, "#ff9292", larger_font)


# Punctele de referinta
top_left_center = (120, 170)
top_right_center = (580, 630)
draw.ellipse([top_left_center[0] - 10, top_left_center[1] - 10,top_left_center[0] + 10, top_left_center[1]+10], fill="#6a1a0b") 
draw.ellipse([top_right_center[0] - 10, top_right_center[1] - 10,top_right_center[0] + 10, top_right_center[1]+10], fill="#008EE8") 


new_image.save("grid-image.jpeg")
