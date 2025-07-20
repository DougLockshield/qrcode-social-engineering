# coleta.py
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class Handler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_POST(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        try:
            data = json.loads(post_data.decode())
            print("\n[+] Dados recebidos:")
            print(json.dumps(data, indent=2))
        except Exception as e:
            print("Erro ao processar JSON:", e)

httpd = HTTPServer(('0.0.0.0', 9090), Handler)
print("Servidor de coleta iniciado na porta 9090...")
httpd.serve_forever()
