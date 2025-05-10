import requests
from PIL import Image
from io import BytesIO

# URL
url = 'http://192.168.249.61/cgi-bin/returnpic.py'

# get image
response = requests.get(url)
response.raise_for_status()  # Raise error if fail

# Open image from response content
img = Image.open(BytesIO(response.content)).convert('RGB')

# Simple image processing: flip the image vertically
#img_flipped = img.transpose(Image.FLIP_TOP_BOTTOM)
img_rotated = img.rotate(180)

# Save the processed image
img_flipped.save('processed_image.png')

print('Image fetched and processed (saved as processed_image.png)')

### REQUIRMENTS OF MODULES:
### requests 
### pillow




