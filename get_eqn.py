'''
get_eqn.py

DESCRIPTION:
    retrieves the Latex equation and copies it to the clipboard
    to be pasted into a file.
        
    I typically use this when writing equations to Evernote.
'''
import pandas as pd

# =============================================================================
# Open the html file and extract Latex code
# =============================================================================
pandoc_output = 'tmp/equation.html'

with open(pandoc_output, 'r') as f:
    txt = ''.join(f.readlines())
    f.close()
    
out = txt.split('title="')[1].split('"')[0] # extracts the Latex code

# =============================================================================
# copy text to the clipboard
# =============================================================================
df = pd.DataFrame([out])
df.to_clipboard(index=False, header=False)