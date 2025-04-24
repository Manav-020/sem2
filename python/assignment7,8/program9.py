import re

def tokenize(text):
    tokens = []
    
    urls = re.findall(r'https?://\S+|www\.\S+', text)
    emails = re.findall(r'[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}', text)
    dates = re.findall(r'\b\d{1,2}[-/\.]\d{1,2}[-/\.]\d{2,4}\b', text)
    numbers = re.findall(r'\b\d+[.,]?\d*\b', text)
    punctuation = re.findall(r'[.,!?;:\\"\'()\[\]{}]', text)
    words = re.findall(r'\b\w+\b', text)
    
    for url in urls:
        tokens.append(url)
    for email in emails:
        tokens.append(email)
    for date in dates:
        tokens.append(date)
    for number in numbers:
        tokens.append(number)
    for punct in punctuation:
        tokens.append(punct)
    for word in words:
        tokens.append(word)
    
    return tokens

if __name__ == "__main__":
    text = input("Enter text to tokenize: ")
    tokens = tokenize(text)
    print("Tokens:")
    for token in tokens:
        print(token)