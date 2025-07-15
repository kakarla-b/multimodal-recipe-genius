# multimodal-recipe-genius

Turn a photo of ingredients into a complete recipe — no coding, no API keys, just open-source AI magic.

This project combines **OCR** (EasyOCR) with **text generation** (HuggingFace Transformers) to build an intelligent assistant that:
- Extracts ingredients from a kitchen image
- Generates a step-by-step recipe using a language model
- Runs with a simple **Streamlit** interface

## How It Works

1. **Upload Image**  
   Upload a photo containing a list of ingredients (handwritten, labels, packaging, etc.)

2. **OCR Processing**  
   `EasyOCR` extracts text from the image to identify the ingredients.

3. **Recipe Generation**  
   The ingredients are fed into a HuggingFace model (`GPT-2`) which generates a coherent recipe based on prompt engineering.


## Tech Stack

| Component        | Tool/Library              |
|------------------|---------------------------|
| OCR              | `easyocr`, `opencv-python` |
| NLP & Generation | `transformers`, `gpt2`, `torch` |
| Frontend         | `streamlit`, `pillow`     |
| Language Model   | `Hugging Face Transformers` |
| Runtime          | Python 3.8+               |


### 1. Clone the repo

```bash
git clone https://github.com/yourusername/multimodal-recipe-genius.git
cd multimodal-recipe-genius

