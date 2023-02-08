from dotenv import load_dotenv
import os, openai

load_dotenv()

openai.api_key = os.environ['OPENAI_API_KEY']

def get_response(text):
    text = f'{text}'

    # logger.info(f"OpenAI prompt: {text}")
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=text,
        temperature=0.7,
        max_tokens=200,
    )
    response_text = response['choices'][0]['text']

    return response_text