import random
import sys
import os
from PIL import Image, ImageDraw, ImageFont
import textwrap

input_path = input("Please specify the path of your file: ")
# https://stackoverflow.com/questions/22939211/what-is-the-proper-way-to-take-a-directory-path-as-user-input

assert os.path.exists(input_path), "I did not find the file at " + str(input_path)
file = input_path
print("File found.\n")

placard = input("Type your placard or leave blank: ")
placard_standard = ["RESIST", "EMPATHY", "QUESTION", "VOTE", "REDISTRIBUTE WEALTH", "GIVE MORE", "WASTE LESS",
                    "MIGHT ≠ RIGHT"]

if placard == "":
    placard = random.choice(placard_standard)
    # https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list

# def wrap(text, font, max_width):
#     phrase = []
#     # If the width of the text is smaller than image width
#     # no need to split it, just add it to the lines array and return.
#     if font.getsize(text)[0] <= max_width:
#         phrase.append(text)
#     else:
#         # split the line by spaces to get separate words
#         words = text.split(' ')
#         i = 0
#         # append every word to a line while the total width is less than image width
#         while i < len(words):
#             line = ''  # if there's no text, line is blank
#             while i < len(words) and font.getsize(line + words[i])[0] <= max_width:
#                 line = line + words[i] + " "  # adds new words to each line and a space at the end
#                 i += 1
#             if not line:
#                 line = words[i]
#                 i += 1
#             # when the line gets longer than the max width stop appending the word,
#             # and add it to a new line in the lines array
#             phrase.append(line)
#     return phrase
#     # draw the message on the background


# initialize the drawing context with
# the image object as background

img = Image.open(input_path)
draw = ImageDraw.Draw(img)
W, H = img.size  # tuple of image dimensions; essential that width is before height for 'wrap'.

# create font object with the font file and specify
# desired size
size_font = int(H / 4)  # maintains the proportion of text relative to image size
color = 'rgb(255, 255, 255)'  # white color
placard_font = ImageFont.truetype('HelveticaNeue.ttc', size=size_font, index=1)  # index here indicates
# the style within the TrueType collection file sequence.
placard_spacing = (H - (size_font * 3)) / 2
# fit lines to image

para = textwrap.wrap(placard, width=8, max_lines=3)
print(para)

i = 0
for line in para:
    while i < len(para):
        w, h = draw.textsize(para()[i], font=placard_font, spacing=placard_spacing)

        # starting position of the message
        (x, y) = ((W - w) / 2, (H - h) / 2)  # centers the text on the image

        draw.multiline_text(xy=(x, y), text=para()[i], fill=color, font=placard_font, align="center")
        i += 1

    # save the edited image
if input_path.find('.jpg'):
    output_path = input_path.replace('.jpg', '_PLACARD.JPG')
elif input_path.find('.JPG'):
    output_path = input_path.replace('.JPG', '_PLACARD.JPG')
elif input_path.find('.JPEG'):
    output_path = input_path.replace('.JPEG', '_PLACARD.JPG')
elif input_path.find('.jpeg'):
    output_path = input_path.replace('.jpeg', '_PLACARD.JPG')

img.save(output_path)
# open(output_path)
