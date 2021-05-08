import re

def text_match(text):
    patterns = '^[a-z]+_[a-z]+$'
    if re.search(patterns,text):
        return 'Found Match'
    
    else:
        return 'Match Not found'

print(text_match('cab_cjsgfj'))
print(text_match('cag_Ahsjsfhyd'))
print(text_match('Abdf_dfdfd'))