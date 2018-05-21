#!/usr/bin/env python3

import logging
import signal
import threading
import zmq

from queue import Queue

from katatennis.services.workers.simulate import run as simulate_game

logger = logging.getLogger(__name__)

def receive_signal(signum, stack):
    logger.info('Received signal %s', signum)
    raise SystemExit('Exiting')


if __name__ == '__main__':

    signal.signal(signal.SIGINT, receive_signal)
    signal.signal(signal.SIGTERM, receive_signal)
    signal.signal(signal.SIGHUP, receive_signal)

    print("[katabackend.services.server] Starting KataTennis server process")

    qGames = Queue()
    threads = []

    nb_threads = 1
    for y in range(nb_threads):
        t = threading.Thread(target=simulate_game, args=(qGames,))
        t.daemon = True
        threads.append(t)
        t.start()

    try:
        context = zmq.Context()
        sock = context.socket(zmq.REP)
        sock.bind('tcp://0.0.0.0:6002')

        while True:
            message = sock.recv_json()
            print("got the message = {}".format(message))
            qGames.put(message)
            print("processing game")
            sock.send_json({"status": "processing"})

        print("out of the loop")
    except SystemExit:
        # clean up
        sock.close()
        context.term()
