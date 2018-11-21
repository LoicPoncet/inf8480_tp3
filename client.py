import sys
import time
import asyncio
import aiohttp

ROUNDS = 5
REQUESTS = 30

async def make_request(session, url):
    """
    Makes a requuets to the given url.
    """
    async with session.get(url) as response:
        return response


async def batch(session):
    """
    Runs a batch of REQUESTS number of requests.
    """
    await asyncio.wait([make_request(session, 'http://' + sys.argv[1] + ':8080?nom=perfTest') for _ in range(REQUESTS)])

async def main():
    if len(sys.argv) != 2:
        print("Usage: \"python client.py IP_ADDR\"")
        sys.exit(1)
    average = 0
    async with aiohttp.ClientSession() as session:
        for i in range(ROUNDS):
            print("Running batch {} on {} with {} requests..".format(i+1, ROUNDS, REQUESTS))
            start_time = time.time()
            await batch(session)
            elapsed = time.time() - start_time
            print("Elapsed time for batch {}: {}".format(i+1, elapsed))
            average += elapsed
    average /= ROUNDS
    print("Average time for {} requests on {} batches: {}".format(
        REQUESTS,
        ROUNDS,
        average
    ))

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
