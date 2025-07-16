from transformers import pipeline

# Load a lightweight generation model from Hugging Face
generator = pipeline("text-generation", model="gpt2")

def generate_recipe(ingredients_text):
    prompt = f"Given the following ingredients: {ingredients_text}\nWrite a step-by-step recipe:"
    result = generator(prompt, max_length=200, num_return_sequences=1)
    return result[0]['generated_text']
