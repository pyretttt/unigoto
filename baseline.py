import pickle

from thefuzz import fuzz
from thefuzz import process

from preprocessor import preprocess_text

class BaselineSolution():
    def __init__(self, correspondences):
        self.correspondences = correspondences

    def find_appropriate_variants(self, text, n=10):
        """
            Returns n most simillar correspondences
        """
        text = preprocess_text(text, if_empty='')
        return process.extract(
            text, 
            choices=self.correspondences,
            limit=n, 
            scorer=fuzz.token_sort_ratio
        )
    
if __name__ == '__main__':
    with open('correspondences.pickle', 'rb') as handle:
        correspondences = pickle.load(handle)
    bsl = BaselineSolution(correspondences)

    v = bsl.find_appropriate_variants('музыка туризм пиво рыбалка', 20)
    print(v)