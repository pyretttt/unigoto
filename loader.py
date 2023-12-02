import asyncio
import argparse
import os
import logging
import sys
import json
from pathlib import Path
import csv
import traceback

import aiohttp

from parsing import parse_response

TOKEN_KEY = 'API_TOKEN'
PER_MINUT_LIMIT = 10
SLEEP = 61
RETRY_ATTEMPTS = 5

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

class LoadError(ValueError):
    def __init__(self, message: str, page, response, *args: object) -> None:
        super().__init__(*args)
        self.message = message
        self.page = page
        self.response = response

class SyncedLoader:
    def __init__(self, token, base_url, request_limit_per_min, output) -> None:
        self.token = token
        self.base_url = base_url
        self.request_limit_per_min = request_limit_per_min
        self.output = output

    def request_url(self, page):
        return f'{self.base_url}/api/{page}?token={self.token}'

    async def load(self, pages, attempt=0):
        if attempt > RETRY_ATTEMPTS:
            logging.error(f'Failed to load {pages} after fifth attempt')
            return
        assert(len(pages) > 0)

        batch_results = [None for i in range(self.request_limit_per_min)]
        current_batch_idx = 0
        n_batches = round(0.5 + len(pages) / self.request_limit_per_min)
        logging.info(f'Total Number Of Batches To Run {n_batches}')
        failed_pages = []
        async with aiohttp.ClientSession() as session:
            for batch in range(n_batches):
                pages_to_load = pages[current_batch_idx * self.request_limit_per_min : (current_batch_idx + 1) * self.request_limit_per_min]
                logging.info(f'About to start load pages: {pages_to_load}')
                tasks = (self.load_page(session, page) for page in pages_to_load)
                results = await asyncio.gather(*tasks, asyncio.sleep(SLEEP), return_exceptions=True)

                for idx, result in enumerate(results):
                    if isinstance(result, LoadError):
                        failed_pages.append(result.page)
                    else:
                        batch_results.insert(idx, result)
                batch_results = [obj for obj in batch_results if obj is not None]
                self.flush_batch(batch_results)

                current_batch_idx += 1

            if failed_pages:
                logging.info(f'Restart loading pages: {failed_pages}')
                await self.load(failed_pages, attempt=attempt+1)

    async def load_page(self, session: aiohttp.ClientSession, page: int):
        url = self.request_url(page)
        logging.info(f'Started Loading Page {url}')

        async with session.get(url) as resp:
            if resp.status == 200:
                logging.info(f'Page {page} Loaded Successfully')
                return await resp.json()
            else:
                logging.error(f'Page {page} Load Failed | Status Code {resp.status}')
                raise LoadError(
                    message=f'Page {page} pesponse contains errors',
                    page=page,
                    response=resp
                )
            
    def flush_batch(self, results):
        if not results:
            logging.info(f'Skipping Flush Of Empty Results To {self.output}')
            return
        try:
            pages_of_persons = [parse_response(page) for page in results]
            persons = [person for page in pages_of_persons for person in page]
            if not persons:
                logging.info('Skipping because no persons to process')
                return
            
            if not Path(self.output).exists():
                with open(self.output, 'a', newline='') as f:
                    writer = csv.DictWriter(f, delimiter=',',  lineterminator="\n", fieldnames=list(persons[0].keys()))
                    writer.writeheader() 
            
            with open(self.output, 'a') as f:
                for person in persons:
                    f.write(','.join(list(person.values())).strip())
                    f.write('\n')
        except BaseException as e:
            logging.error(f'Error while trying write to {e}')
            traceback.print_exc()

if __name__ == '__main__':
    if TOKEN_KEY not in os.environ:
        print(f'Please set {TOKEN_KEY} environment variable', file=sys.stderr)
        exit(1)

    parser = argparse.ArgumentParser(description='Arguments parser =)')
    parser.add_argument(
        '--start',
        action="store",
        type=int,
        required=True,
        help='starting page to load'
    )
    parser.add_argument(
        '--end',
        action="store",
        type=int,
        required=True,
        help='End page to load'
    )
    parser.add_argument(
        '--output',
        action="store",
        type=str,
        required=True,
        help='Output file path'
    )
    args = parser.parse_args()

    token = os.environ[TOKEN_KEY]
    loader = SyncedLoader(
        token, 
        base_url='http://45.91.8.110',
        request_limit_per_min=PER_MINUT_LIMIT,
        output=args.output
    )
    pages = list(range(args.start, args.end+1))
    asyncio.run(
        loader.load(pages)
    )
