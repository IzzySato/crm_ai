# AI-Powered Image-to-Text Description Service

This project is a Python Flask microservice designed to generate descriptive text from images using the HuggingFace API. It processes images stored on S3 and returns a detailed, contextually relevant description, making it ideal for use in e-commerce, content creation, and other applications requiring automated image descriptions.

## Features

- **AI Integration**: Uses state-of-the-art HuggingFace models to generate high-quality descriptions from images.
- **Secure Access**: Ensures that only authorized users can access the service through the use of an Authorization header.
- **Scalable**: Built with Flask, making the service lightweight and easy to scale.
- **Flexible API**: Can be easily integrated into larger applications as a microservice.

## Installation

### Prerequisites

- Python 3.x
- Flask
- Requests library
- HuggingFace API key

### Setup

1. **Clone the repository:**

```bash
git clone https://github.com/IzzySato/crm_ai.git
cd ai-image-to-text
```

2. **Create and activate a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Set environment variables:**
```bash
API_KEY=your_huggingface_api_key
JWT_SECRET_KEY=your_jwt_secret_key
```

5. **Run the application:**
```bash
python -m flask run
```

### POST /description Usage
#### This endpoint generates a description for an image provided via an S3 URL.

Request

	Headers:
	•	Authorization: Bearer <your_token> - Required for accessing the endpoint.
	Body:
	•	image_url: The URL of the image stored in S3.
	•	product_name: The product name or any additional context to generate a better description.

Example:
```bash
curl --location 'http://127.0.0.1:5000/description' \
--header 'Authorization: Bearer <your_token>' \
--header 'Content-Type: application/json' \
--data '{
    "image_url": <image_url>,
    "product_name": <product_name>
}'
```

Response:
```json
{
    "description": [
        {
            "generated_text": "a large white building with a lot of white chairs"
        }
    ]
}
```