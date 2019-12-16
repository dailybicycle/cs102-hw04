from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


def text_wrap(text, font, max_width):
    lines = []
    # If the width of the text is smaller than image width
    # we don't need to split it, just add it to the lines array
    # and return
    if font.getsize(text)[0] <= max_width:
        lines.append(text)
    else:
        # split the line by spaces to get words
        words = text.split(' ')
        i = 0
        # append every word to a line while its width is shorter than image width
        while i < len(words):
            line = ''
            while i < len(words) and font.getsize(line + words[i])[0] <= max_width:
                line = line + words[i] + " "
                i += 1
            if not line:
                line = words[i]
                i += 1
            # when the line gets longer than the max width do not append the word,
            # add the line to the lines array
            lines.append(line)
    return lines


def draw_text(text):
    # open the background file
    img = Image.open('background.png')

    # size() returns a tuple of (width, height)
    image_size = img.size

    # create the ImageFont instance
    font_file_path = 'fonts/Avenir-Medium.ttf'
    font = ImageFont.truetype(font_file_path, size=50, encoding="unic")

    # get shorter lines
    lines = text_wrap(text, font)

    for line in lines:
        font.getsize(line)[1]


text = "This could be a single line text but it can't fit in one line."
lines = text_wrap(lines, font)

for line in lines:
    font.getsize(line)[1]

# Output
# 62
# 51

text = "This could be a single line text but it can't fit in one line."
lines = text_wrap(lines, font)

line_height = font.get_size('hg')[1]

# Output
# 62

text = "This could be a single line text but its too long to fit in one."
lines = text_wrap(text, font, image_size[0])
line_height = font.getsize('hg')[1]

x = 10
y = 20
for line in lines:
    # draw the line on the image
    draw.text((x, y), line, fill=color, font=font)

    # update the y position so that we can use it for next line
    y = y + line_height
# save the image
img.save('word2.png', optimize=True)

if __name__ == __main__:
    draw_text("This could be a single line text but its too long to fit in one.")