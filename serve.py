import os, sys
os.chdir("/Users/sebv/Desktop/claude code website")
sys.argv = ["serve"]
from http.server import HTTPServer, SimpleHTTPRequestHandler
HTTPServer(("", 3000), SimpleHTTPRequestHandler).serve_forever()
