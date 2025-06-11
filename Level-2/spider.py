import asyncio
import aiohttp
from urllib.parse import urljoin
from bs4 import BeautifulSoup

BASE_URL = "https://www.example.com"
CONCURRENCY = 10
VISITED = set()

class Spider:
    def __init__(self):
        pass

    async def fetch(self, session, url):
        try:
            async with session.get(url) as response:
                return await response.text()
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return None
    
    async def parse_and_crawl(self, session, url, semaphore):
        async with semaphore:
            if url in VISITED:
                return
            VISITED.add(url)

            print(f"Crawling {url}")
            html = await self.fetch(session, url)
            if not html:
                return
            
            soup = BeautifulSoup(html, 'html.parser')
            links = [
                urljoin(BASE_URL, a['href'])
                for a in soup.find_all('a', href=True)
                if urljoin(BASE_URL, a['href']).startswith(BASE_URL)
            ]

            tasks = []
            for link in links:
                if link not in VISITED:
                    task = asyncio.create_task(self.parse_and_crawl(session, link, semaphore))
                    tasks.append(task)
            
            await asyncio.gather(*tasks)


async def main():
    semaphore = asyncio.Semaphore(CONCURRENCY)

    async with aiohttp.ClientSession() as session:
        await Spider().parse_and_crawl(session, BASE_URL, semaphore)

