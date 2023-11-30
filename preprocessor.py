from string import punctuation

import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")

russian_stopwords = stopwords.words("russian")
punctuations_translation = str.maketrans('', '', punctuation) 


def preprocess_text(text):
    string = text.translate(punctuations_translation) \
        .strip() \
        .lower()
    tokens = [token for token in string.split() if token not in russian_stopwords]
    
    return ' '.join(tokens)


if __name__ == '__main__':
    # Test
    print(preprocess_text('Привет Всем, что вы как бы ну \-^-^-/ тут делаете?'))