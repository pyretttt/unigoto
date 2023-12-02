import csv

from preprocessor import preprocess_text

def parse_response(response) -> list[str]:
    if not hasattr(response, 'get'): # If something wrong came
        return []
    
    persons: list[dict] = response.get('response', list())
    result = []
    if persons is None: # if response contains errors
        return result
    for person in persons:
        attributes = dict()
        
        if (country := person.get('country')) \
            and (country_name := country.get('title')) \
                and country_name == 'Россия':
            attributes['country'] = 'Россия'
        else:
            continue
        
        if university := person.get('university_name'):
         attributes['university_name'] = university
        else:
            continue

        attributes['city'] = person.get('city', UNK).get('title', UNK)
        attributes['about'] = preprocess_text(person.get('about', UNK))
        attributes['activities'] = preprocess_text(person.get('activities', UNK)) 
        attributes['books'] = preprocess_text(person.get('books', UNK))
        attributes['games'] = preprocess_text(person.get('games', UNK))
        attributes['interests'] = preprocess_text(person.get('interests', UNK))
        attributes['education_form'] = preprocess_text(person.get('education_form', UNK))
        attributes['education_status'] = preprocess_text(person.get('education_status', UNK))
        attributes['faculty_name'] = person.get('faculty_name', UNK)
        
        result.append(attributes)

    return result

UNK = 'unk'