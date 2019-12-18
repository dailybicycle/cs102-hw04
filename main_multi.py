import random
import os
import webbrowser
from PIL import Image, ImageDraw, ImageFont, ImageEnhance

# Run from terminal using python3, not simply python


def placard():
    # message = input("1. Type your placard text (3 WORDS MAX) or leave blank for generator: ")
    message_generator = ["RESIST", "HAVE EMPATHY", "QUESTION", "VOTE", "REDISTRIBUTE WEALTH", "GIVE MORE", "WASTE LESS",
                        "MIGHT ≠ RIGHT", "CONSUME LESS", "READ"]
    # if message == "":
    message = random.choice(message_generator)
    # elif len(message.split()) > 3:
    #     message = input("   Please choose a phrase of 3 words maximum or leave blank: ")
    #     if message == "":
    #         message = random.choice(message_generator)
    # https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list
    return message.split()  # split words into separate lines for readability


input_path = input("Please specify the file path of your image list: ")
# https://stackoverflow.com/questions/22939211/what-is-the-proper-way-to-take-a-directory-path-as-user-input

assert os.path.exists(input_path), "File not found at " + str(input_path)
file = (input_path, 'r+')
print("File found.\n")


# choose grayscale
gray = input("1. Convert image to grayscale? Y/N or leave blank: ")

if gray.upper() == 'Y':
    img = Image.open(input_path).convert('L')  # convert to grayscale. Use 'L', not 'LA', for jpg files.
    # https://stackoverflow.com/questions/12201577/how-can-i-convert-an-rgb-image-into-grayscale-in-python

else:
    img = Image.open(input_path)

# choose contrast level
contrast = input("3. Set numerical contrast factor (>1.0 is increased contrast) or leave blank: ")
if contrast == "":
    contrast = 1.0  # does not change contrast (DEFAULT)


img = ImageEnhance.Contrast(img).enhance(float(contrast))  # anything above 1.0 is added contrast.

draw = ImageDraw.Draw(img)
W, H = img.size  # tuple of image dimensions.

# choose text color
color = input("4. Choose text color, W/K, or leave blank for default (W): ")

if color.upper() == "K":  # https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/
    color = 'rgb(0,0,0)'  # black

else:
    color = 'rgb(255, 255, 255)'  # white  (DEFAULT)


# portion of image width to contain total text width (90% of each dim)
text_block = Image.new('RGB', (int(W*0.9), int(H*0.9)))

# initialize default size relative to image size
if W >= H:
    size_font = int(H / 4)
else:
    size_font = int(W / 4)

# create font object with desired font file
placard_font = ImageFont.truetype('HelveticaNeue.ttc', size=size_font, index=1)
# index here indicates the style within the TrueType collection file sequence.

# give total line height; h & g reach extents
line_height = placard_font.getsize('hg')[1]



placard = placard()
# print(placard) # for troubleshooting

# initialize starting y position at center
y = (H - (line_height * len(placard))) / 2

for line in placard:
    # If word is too long
    # or if there are too many lines to fit all of the words within the text_block at the default font size
    if placard_font.getsize(line)[0] > text_block.size[0] or (line_height * len(placard)) > text_block.size[1]:
        new_size_font = 1  # initialize small font size
        new_font = ImageFont.truetype('HelveticaNeue.ttc', size=new_size_font, index=1)  # initialize font at new size

        # make it fit the outer dimensions (width = total width, height = line height for number of lines in block)
        # longer words will have smaller text. Most action words are shorter and therefore should be bigger.
        while new_font.getsize(line)[0] < text_block.size[0] and (new_font.getsize('hg')[1] * len(placard)) < text_block.size[1]:
            new_size_font += 2  # faster incrementing
            new_font = ImageFont.truetype('HelveticaNeue.ttc', size=new_size_font, index=1)
            line_height = new_font.getsize('hg')[1]
        line_width = new_font.getsize(line)[0]
        x = (W - line_width) / 2  # centers the text on the image
        draw.text(xy=(x, y), text=line, fill=color, font=new_font, align="center")
        y = y + line_height  # this adds new line height from while loop, starts next line below current line
    else:
        # default line dims, used for centering on image
        line_width = placard_font.getsize(line)[0]
        line_height = placard_font.getsize(line)[1]
        # starting position of the message
        x = (W - line_width) / 2  # centers the text on the image
        draw.text(xy=(x, y), text=line, fill=color, font=placard_font, align="center")
        y = y + line_height  # moves next line below current line


# save the edited image. Avoid problematic characters in output file path.
illegals = ['#', '%', '&', '{', '}', '\ ', '<', '>', '*', '?', '/', ' ', '$', '!', "'", '"', ':', '@', '+', '`', '|', '=']

# re-concatenate input text for file naming
placard = ' '.join(placard)

# replace problematic characters
for line in illegals:
    placard = placard.replace(line, '_')

output_path = input_path.replace('.', '_' + placard + '.')  # add text to filename

img.save(output_path)

# open placard file in default image viewer
webbrowser.open('file://' + output_path)
# https://stackoverflow.com/questions/22004498/webbrowser-open-in-python
