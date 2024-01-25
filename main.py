from http.server import SimpleHTTPRequestHandler, HTTPServer
import json
import os
from helpers.Checker import CheckUrl
from helpers.Exeminer import exemine_file
class SimpleHandler(SimpleHTTPRequestHandler):
    def _send_response(self, message, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(message, 'utf8'))


    def do_GET(self):
        print(self.path)
        if self.path == '/':
            self._send_response('This is just an empty endpoint', status=200)
        elif '/images/' in self.path:
            pathImg='assets/images/'+self.path.split("/images/")[1]
            print(pathImg)
            if os.path.exists(pathImg):
                self.send_response(200)
                self.send_header('Content-type', 'image/png')
                self.end_headers()
                with open(pathImg, 'rb') as file:
                    html_content = file.read()
                self.wfile.write(html_content)
            else:
                self.send_response(400)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(bytes("no file found", 'utf8'))
        elif '/docs/' in self.path:
            pathImg='assets/docs/'+self.path.split("/docs/")[1]
            print(pathImg)
            if os.path.exists(pathImg):
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                with open(pathImg, 'rb') as file:
                    html_content = file.read()
                self.wfile.write(html_content)
            else:
                self.send_response(400)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(bytes("no file found", 'utf8'))
        else:
            self.send_response(400)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes("there is no endpoint you are trying to reach", 'utf8'))
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        print(post_data)

        if self.path == '/':
            try:
                data = json.loads(post_data.decode('utf-8'))
                self._send_response(
                    json.dumps({'req': 'This is a POST request with path ' + self.path, 'data_received': data}))
            except json.JSONDecodeError:
                self._send_response('Error: Invalid JSON data received in the POST request.', status=400)

        elif self.path == '/checkURL':
            try:
                added_json = json.loads(post_data.decode('utf-8'))
                info = CheckUrl(added_json)
                self._send_response(
                    json.dumps({'url info': info}))
            except json.JSONDecodeError:
                self._send_response('Error: Invalid JSON data received in the POST request.', status=400)
        elif self.path == '/fileExeminer':
            try:
                added_json = json.loads(post_data.decode('utf-8'))
                info = exemine_file(added_json)
                self._send_response(
                    json.dumps({'file info': info}))
            except json.JSONDecodeError:
                self._send_response('Error: Invalid JSON data received in the POST request.', status=400)
        else:
            self.send_response(400)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes("there is no endpoint you are trying to reach", 'utf8'))

def run_server(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleHandler)
    print(f'Starting server on port {port}')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
