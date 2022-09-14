#md_techgeek

import easyocr

reader = easyocr.Reader(['en','hi','mr'])

results = reader.readtext('HINDI2.jpg')

text = ''

for result in results:
    text += result[1] + ' '

print(text)