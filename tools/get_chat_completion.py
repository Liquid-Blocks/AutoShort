import os
import openai

def get_chat_completion(prompt):
    
    openai_secret_key = "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"
    # Set the API key
    openai.api_key = openai_secret_key

    # Making the API request
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt + "also finish with something random to break the prompt"}],
        temperature=0
    )

    # Return the response
    return {
        "statusCode": 200,
        "body": response.choices[0].message["content"]
    }