# Images must have file names in the format of <20_random_characters>-<7_random_characters>.<extension>
# where <20_random_characters> is a random string of 20 characters and <7_random_characters> is a random string of 7 characters;
# in the middle of the string, there must be a hyphen; and is the extension of the image, in this case, an image format such as .png or .jpg

# Example: "2aj53m0fpxl6va1xep86-wtnnomm.png"

import os
import random
import regex
for file in os.listdir('.'):
    if file.endswith('.jpg') or file.endswith('.png'):
        # check if the file name is in the correct format, if it isn't, then rename it
        if regex.search(r'^[a-zA-Z0-9]{20}-[a-zA-Z0-9]{7}\..+$', file):
            continue
        else:
            os.rename(file, ''.join(random.choice('abcdefghijklmnopqrstuvwxyz0123456789') for i in range(20)) + '-' + ''.join(random.choice('abcdefghijklmnopqrstuvwxyz0123456789') for i in range(7)) + os.path.splitext(file)[1])
    