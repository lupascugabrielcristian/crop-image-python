from PIL import Image, ImageDraw, ImageFont

#left    = 356 # de la bitmap position
#top     = 17 # de la bitmap position
#right   = left + 768 # width - de la "bitmap cropped"
#bottom  = top + 768  # height - de la "bitmap cropped"

MARGIN = 0.2
H_RATIO = 3.22519
statusbar_height = 48


with Image.open("orig.jpeg") as orig:
    print("==== ORIG ====")
    print("Size: %d X %d" % (orig.width, orig.height) )

    draw = ImageDraw.Draw(orig)

    # TOOLBAR margin
    ydpi = 295.563
    toolbarpx = 65 * ydpi / 160
    print(f"toolbarpx: {toolbarpx}")
    toolbar_bottom = 228
    #draw.line([(0, toolbar_bottom), (orig.width, toolbar_bottom)], fill="#008EE8", width=3)

    # TOOLBAR RATIO
    toolbar_ratio = 0.159
    toolbar_height = toolbar_ratio * orig.height
    draw.line([(0, toolbar_height), (orig.width, toolbar_height)], fill="#642697", width=3)

    # Imaginea cropped o sa fie centrata cu margini de 10%
    left = MARGIN * orig.width # 192
    ##!!! Asta este cel care trebuie reglat ##
    top = 413 #MARGIN * orig.width + (toolbar_bottom - statusbar_height) * H_RATIO
    croppedW = (1 - 2 * MARGIN) * orig.width
    croppedH = (1 - 2 * MARGIN) * orig.width
    right = left + croppedW
    bottom = top + croppedH
    print(f"Margins {left}")

    # Cropped image
    cropped = orig.crop((left, top, right, bottom))

    print("==== CROPPED ====")
    print("Size: %d X %d" % (cropped.width, cropped.height) )

    cropped.save("cropped.jpeg")
    #cropped.show()

    # Liniile verticale la fiecare 100px si label-urile
    font_coordonate = ImageFont.truetype("Montserrat-Regular.ttf", 36)
    spaces = 200
    for x in range(1, round(orig.width / 100)):
        draw.line([(200 * x, 30), (200 * x, orig.height)], "#787078", 1)
        draw.text((200*x - 10, 10), "x=" + str(200*x), font=font_coordonate)

    # Liniile orizontale la fiecare 100px si label-urile
    for y in range(1, round(orig.height / spaces)):
        draw.line([(0, spaces*y), (orig.width, spaces*y)], "#87ab63", 1)
        draw.text((10, spaces*y-10), "Y=" + str(spaces*y), "#269741", font=font_coordonate)

    # Punctul de crop dreapta-jos
    font = ImageFont.truetype("Montserrat-Regular.ttf", 18)
    crop_text = "X=" + str(right) + "\nY=" + str(bottom)
    draw.text((right, bottom), crop_text, "#6A1A0B", font)

    # Punctul de crop stanga-sus
    crop_text = "X=" + str(left) + "\nY=" + str(top)
    draw.text((left+10, top+10), crop_text, "#6A1A0B", font)

    # Crop Width
    width_text = "W=" + str(cropped.width)
    draw.text((left + cropped.width/2, top-28), width_text, "#6A1A0B", font)

    # Crop Height
    height_text = "H=" + str(cropped.height)
    draw.text((right+10, top + cropped.height/2), height_text, "#6A1A0B", font) 

    # Crop rectangle
    draw.rectangle([left, top, right, bottom], outline="#6A1A0B", width=2)

    # Orig Dimensions
    original_text = "W="+str(orig.width) + "\nH=" + str(orig.height)
    larger_font = ImageFont.truetype("Montserrat-Regular.ttf", 56)
    draw.text((orig.width - 350, orig.height - 280), original_text, "#ff9292", larger_font)

    orig.save("orig-marked.jpeg")

    marked = Image.open("orig-marked.jpeg")
    #marked.show()




