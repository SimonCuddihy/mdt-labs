#
# This is a starting point for many of the tasks in Lab 6.
# The code here is not complete and contains a deliberate
# 'bug' that you'll need to fix (pay attention to the lab
# instruction text because there is a hint there!).
#
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import time
from time import strftime, gmtime


class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-Type:', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write()

    def do_POST(self):
        length = int(self.headers.getheader('content-length'))
        postvars = cgi.parse_qs(self.rfile.read(length), keep_blank_values=1)
        global device_name
        device_name = postvars['device_name'][0]
        self._set_headers()
        if 'reboot' in postvars.keys() :
        print ("Rebooting...")
        subprocess.call("reboot", shell=True)
        self.wfile.write("<html><body>Rebooting!</body></html>")
        else :
        self.wfile.write("<html><body>Thanks! My new name is <b>")
        self.wfile.write(device_name)
        self.wfile.write("</b></body></html>")



def run(server_class=HTTPServer, handler_class=S, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...')
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()

