import pickle

from thefuzz import fuzz
from thefuzz import process

from .preprocessor import preprocess_text
from src.schemas.baseline_student_data import BaselineStudentData


class BaselineSolution():
    def __init__(self, correspondences):
        self.correspondences = correspondences

    def find_appropriate_variants(self, text, n=10):
        """
            Returns n most similar correspondences
        """
        text = preprocess_text(text, if_empty='')
        return process.extract(
            text,
            choices=self.correspondences,
            limit=n,
            scorer=fuzz.token_sort_ratio
        )


def run_baseline(data: BaselineStudentData, res_length: int = 10):
    """Produce a list of recommendations based on user's interests.

    Args:
        data (BaselineStudentData): The data to be processed.
        res_length (int): How many entries to produce.

    Returns:
        List: The results of the baseline model.
    """

    with open('correspondences.pickle', 'rb') as handle:
        correspondences = pickle.load(handle)
    bsl = BaselineSolution(correspondences)

    result = bsl.find_appropriate_variants(data.interests, res_length)

    return result


if __name__ == '__main__':
    with open('correspondences.pickle', 'rb') as handle:
        correspondences = pickle.load(handle)
    bsl = BaselineSolution(correspondences)

    v = bsl.find_appropriate_variants('музыка туризм пиво рыбалка', 20)
    print(v)
