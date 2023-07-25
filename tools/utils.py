def convert_text(text):
    words = text.split()[:7]  # Extract the first 7 words
    lowercased_words = [word.lower() for word in words]  # Convert words to lowercase
    result = '-'.join(lowercased_words)  # Join the lowercased words with hyphens
    return result