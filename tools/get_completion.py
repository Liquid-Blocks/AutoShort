import os
import openai

def get_completion(prompt):
    openai_secret_key = "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"
    # Set the API key
    openai.api_key = openai_secret_key

    # Making the API request
    response = openai.Completion.create(
        model= "text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Return the response
    return {
        "statusCode": 200,
        "body": response.choices[0].text.strip()
    }