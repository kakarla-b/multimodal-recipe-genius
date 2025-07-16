import easyocr
import numpy as np
from PIL import Image

reader = easyocr.Reader(['en'], gpu=False)

def extract_ingredients_from_image(pil_image):
    image_np = np.array(pil_image)
    results = reader.readtext(image_np)
    text = " ".join([res[1] for res in results])
    return text
