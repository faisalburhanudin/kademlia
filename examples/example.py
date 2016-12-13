import logging
import asyncio

from kademlia.network import Server


logging.basicConfig(level=logging.DEBUG)
loop = asyncio.get_event_loop()
loop.set_debug(True)

server = Server()
server.listen(8468)


def done(result):
    print("Key result:", result)


def set_done(result, server):
    server.get("a key").addCallback(done)


def bootstrap_done(found, server):
    server.set("a key", "a value").addCallback(set_done, server)

# server.bootstrap([("1.2.3.4", 8468)]).addCallback(bootstrapDone, server)

try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

loop.close()
