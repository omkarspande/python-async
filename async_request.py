import aiohttp
import asyncio
import os
import time

from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("ALPHAVANTAGE_API_KEY")
url = "https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}"
symbols = ["AAPL", "GOOG", "TSLA", "MSFT", "PEP"]
results = []


async def run_tasks():
    async with aiohttp.ClientSession() as session:
        for symbol in symbols:
            print("Fetching data for:", symbol)
            response = await session.get(url.format(symbol, api_key), ssl=False)
            results.append(await response.json())


start = time.time()
asyncio.run(run_tasks())
end = time.time()
total_time = end - start
print("It took {} seconds to make {} API calls".format(total_time, len(symbols)))
