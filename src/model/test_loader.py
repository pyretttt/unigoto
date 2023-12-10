import pytest
import json
from .loader import SyncedLoader
import os

@pytest.mark.asyncio
async def test_synced_loader():
    token = 'RHWBuMDebpkT8HNvPYw' 
    base_url = 'http://45.91.8.110'
    request_limit_per_min = 10
    output = 'output.csv'
    pages = [1, 2, 3]

    try:
        # Создание экземпляра SyncedLoader
        loader = SyncedLoader(token, base_url, request_limit_per_min, output)

        # Запуск загрузки страниц
        await loader.load(pages)

        # Проверка наличия столбцов в файле
        with open(output, 'r') as f:
            header_line = f.readline().strip()
            assert "about" in header_line
            assert "activities" in header_line
            assert "books" in header_line
            assert "games" in header_line
            assert "interests" in header_line

    finally:
        # Удаление файла после выполнения теста
        os.remove(output)