#!/bin/env python
# -*- coding: utf-8 -*-

import time
import json
import tornado.gen
import tornado.tcpserver
import tornado.ioloop
import tornado.options
from tornado.log import app_log
from concurrent.futures import ThreadPoolExecutor


class BoServer(tornado.tcpserver.TCPServer):
    executor = ThreadPoolExecutor(max_workers=4)

    def __init__(self, io_loop=None, ssl_options=None, max_buffer_size=None, read_chunk_size=None):
        super(BoServer, self).__init__(io_loop, ssl_options, max_buffer_size, read_chunk_size)

    def busy_work(self):
        time.sleep(3)
        print "work now"
        return {"a": "b"}

    @tornado.gen.coroutine
    def handle_stream(self, stream, address):
        print "get request {}".format(address)
        try:
            r = self.busy_work()
            stream.write(json.dumps(r))
        finally:
            stream.close()


def main():
    server = BoServer()
    server.listen(9999)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
