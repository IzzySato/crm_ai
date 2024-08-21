import os
import requests

def generate_description(image_url, product_name):
  API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-base"
  headers = {"Authorization": f"Bearer {os.getenv('API_KEY')}"}
  prompt = f"Product name: {product_name}. Generate a detailed description of the product in the image"
  response = requests.post(API_URL, headers=headers, json={"inputs": {
    "image": image_url,
    "text": prompt
    }})
  return response.json()