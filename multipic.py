import time
import sys
import requests
from PIL import Image
from io import BytesIO

# URL of the image
url = 'http://192.168.249.61/cgi-bin/returnpic.py'

def fetch_and_process_image(filename):
    response = requests.get(url)
    response.raise_for_status()
    img = Image.open(BytesIO(response.content)).convert('RGB')
    img_rotated = img.rotate(180)
    img_rotated.save(filename)
    print(f'Image saved as {filename}')

if __name__ == '__main__':
    num_images = 10
    if len(sys.argv) > 1:
        try:
            num_images = int(sys.argv[1])
        except ValueError:
            print('Invalid number specified, using default 10')
    for i in range(1, num_images + 1):
        filename = f'processed_image[secondbatch]_{i}.png'
        fetch_and_process_image(filename)
        if i != num_images:
            time.sleep(3)
