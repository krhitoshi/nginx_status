#!/usr/bin/env python
import sys
import requests


class NginxStatus:
    url = 'http://localhost/nginx_status'
    keys = ['active', 'accepts', 'handled', 'requests',
            'reading', 'writing', 'waiting']

    def __init__(self, argv):
        self.argv = argv
        self.program_name = self.argv[0]

    def arg_error(self):
        usage = 'Usage: %s %s' % (self.program_name,
                                  '|'.join(NginxStatus.keys))
        sys.exit(usage)

    def get_nginx_status(selfl):
        r = requests.get(NginxStatus.url)
        return r.text

    def main(self):
        if len(self.argv) != 2:
            self.arg_error()

        key = self.argv[1]
        if key not in NginxStatus.keys:
            self.arg_error()

        res = self.get_nginx_status()
        lines = res.split('\n')
        status = {}

        # http://nginx.org/en/docs/http/ngx_http_stub_status_module.html
        # Active connections: 5
        _, value = lines[0].split(':')

        # server accepts handled requests
        #  16462 16462 28543
        status['active'] = int(value)

        accepts, handled, requests = [int(v) for v in lines[2].split()]
        status['accepts'] = accepts
        status['handled'] = handled
        status['requests'] = requests

        # Reading: 0 Writing: 1 Waiting: 4
        values = lines[3].split()
        reading, writing, waiting = [int(v) for v in values[1:6:2]]
        status['reading'] = reading
        status['writing'] = writing
        status['waiting'] = waiting
        # print(status)
        print(status[key])


if __name__ == '__main__':
    s = NginxStatus(sys.argv)
    s.main()
