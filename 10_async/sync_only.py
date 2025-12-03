import httpx
import time
from tqdm import tqdm

def get_data(id):
    url = "https://jsonplaceholder.typicode.com/posts"
    r = httpx.get(url + f"/{id}")
    return r.json()

def main():
    result = []
    for i in range(1, 10):
        res = get_data(i)
        result.append(res)
    return result

if __name__ == "__main__":
    s = time.time()
    print(main())
    e = time.time()
    print("total_time = ", e - s )

