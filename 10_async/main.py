import asyncio
import httpx
import time
from tqdm import tqdm

SEM = asyncio.Semaphore(2)

async def get_data(id):
    async with SEM:
        async with httpx.AsyncClient() as client:
            response = await client.get(f'https://jsonplaceholder.typicode.com/posts/{id}')
        return response.json()

async def task(n):
    return await get_data(n)

async def main():
    results = await asyncio.gather(*(task(i) for i in tqdm(range(1, 10))))
    return results

if __name__ == "__main__":
    s = time.time()
    print(asyncio.run(main()))
    e = time.time()
    print("total_time = ", e - s )
