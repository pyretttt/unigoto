const baseUrl = 'http://127.0.0.1:8000/';
const baselinePath = 'api/model/baseline';

const interests = document.getElementById('interests');

const resultsList = document.getElementById('results_list');
const resultsInfo = document.getElementById('results__info');
const resultsError = document.getElementById('results__error');

const modelSelection = document.getElementById('model-select');
const resLength = document.getElementById('res-length');

/** Make request with input's value to the url, set result's value to response */
function postBaseline() {
    if (interests.value?.length > 0) {
        resetForm();
        fetch(baseUrl + baselinePath, {
            method: 'POST',
            headers: {
                Accept: 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                data: { interests: interests.value },
                res_length: resLength.value
            })
        })
            .then((res) => {
                if (!res.ok) {
                    // Throw an error when network request returns error
                    console.log(res)
                    throw new Error(`${res.status}: ${res.statusText}`);
                }
                return res.json();
            })
            .then((res) => {
                console.log(res)
                addBaselineResults(res);
            })
            .catch((err) => {
                console.error(err);
                resultsError.innerText = err ? err : `Ошибка`;
            })
            .finally(() => {
                resultsInfo.innerText = '';
            });
    } else {
        resultsInfo.innerText = '';
    }
}

function clearResults() {
    if (resultsList) {
        resultsList.innerHTML = '';
    }
}

function resetForm() {
    resultsError.innerText = '';
    resultsInfo.innerText = 'Loading...';
    clearResults();
}

function addBaselineResults(results) {
    results.forEach((el) => {
        const node = document.createElement('li');
        const textNode = document.createTextNode(
            `${el.university} (${el.match_percentage}) – ${el.similar_interests}`
        );

        node.classList.add('results__item');

        node.appendChild(textNode);
        resultsList?.appendChild(node);
    });
}
