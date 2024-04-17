import os
import re

def text_extraction(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        match = re.search(r'([A-Za-z0-9,;"\'\s\-()]+[.!?])', content)
        if match:
            return match.group(1)
        else:
            return 'no text'
        
def main():
    directory = 'texts'
    for filename in os.listdir(directory):
        if filename.endswith('txt'):
            # construct full path to file
            file_path = os.path.join(directory, filename)
            # extract and print first sentence
            first_sentence = text_extraction(file_path)
            print(first_sentence)

if __name__ == '__main__':
    main()