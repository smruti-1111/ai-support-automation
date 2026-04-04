import re

def mask_sensitive_data(text: str) -> str:
    # Mask emails
    text = re.sub(r'\S+@\S+', '[EMAIL]', text)

    # Mask phone numbers (basic pattern)
    text = re.sub(r'\b\d{10}\b', '[PHONE]', text)

    return text
