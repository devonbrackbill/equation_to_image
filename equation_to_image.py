'''
equation_to_image.py

DESCRIPTION:
    converts an html file with a markdown equation to an image (.png)
    and copies that image to the clipboard to be pasted into a file.
    
    I typically use this when writing equations to Evernote
    
NOTES:
    This script requires an Internet connection.
    
'''
import urllib.request
from io import BytesIO
import win32clipboard
from PIL import Image
import os

# =============================================================================
# GLOBALS
# =============================================================================

pandoc_from = 'tmp/equation.md'
pandoc_output = 'tmp/equation.html'

url = 'tmp/equation.html'
fileout = 'tmp/equation.png'

# =============================================================================
# run pandoc: converts markdown --> image
# =============================================================================

os.system('pandoc {} -f markdown -t html -o {}'.\
          format(pandoc_from,pandoc_output))

# =============================================================================
# get the image from the website and save to file
# =============================================================================
with open(url, 'r') as f:
    html = ''.join(f.readlines())
    f.close()

url_out = html.split('"')[1].split('"')[0] # URL where the image is stored.

data = urllib.request.urlretrieve(url_out, fileout) # request the image.

# =============================================================================
# copy image to clipboard
# =============================================================================

def send_to_clipboard(clip_type, data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(clip_type, data)
    win32clipboard.CloseClipboard()

filepath = fileout
image = Image.open(filepath)

output = BytesIO()
image.convert("RGB").save(output, "BMP")
data = output.getvalue()[14:]
output.close()

send_to_clipboard(win32clipboard.CF_DIB, data)