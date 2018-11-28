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


async def batch(session, synchronous, batchNumber):
    """
    Runs a batch of REQUESTS number of requests. It can be launched synchronously if
    there is only one server to send response.
    """
    if(synchronous):
        for i in range(REQUESTS):
            await make_request(session, 'http://' + sys.argv[1] + ':8080?nom={}:{}'.format(
                batchNumber, i)
            )
    else:
        await asyncio.wait([make_request(session, 'http://' + sys.argv[1] + ':8080?nom={}:{}'.format(
            batchNumber, i 
        )) for i in range(REQUESTS)])

async def main():
    if len(sys.argv) != 3:
        print("Usage: \"python client.py <IP_ADDR:String> <SYNCHRONOUS:boolean>\"")
        sys.exit(1)
    if(sys.argv[2] not in ["true", "false"]):
        print("<SYNCHRONOUS> parameter should be \"true\" or \"false\"")
        sys.exit(1)

    average = 0
    synchronous = sys.argv[2] == "true"
    async with aiohttp.ClientSession() as session:
        for batchNumber in range(ROUNDS):
            print("Running batch {} on {} with {} requests..".format(batchNumber+1, ROUNDS, REQUESTS))
            start_time = time.time()
            await batch(session, synchronous, batchNumber)
            elapsed = time.time() - start_time
            print("Elapsed time for batch {}: {}".format(batchNumber+1, elapsed))
            average += elapsed
    average /= ROUNDS
    print("Average time for {} requests on {} batches: {}".format(
        REQUESTS,
        ROUNDS,
        average
    ))

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
