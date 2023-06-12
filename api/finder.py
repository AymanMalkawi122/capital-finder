from http.server import BaseHTTPRequestHandler
import requests
from urllib import parse


class handler(BaseHTTPRequestHandler):
 
  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    url_components = parse.urlsplit(self.path)
    req_type = url_components.query.split()[0]
    if req_type == "country":
        req_type = "name"
    else: req_type = "capital"
    query_params = url_components.query.split()[1]
    req = requests.get(f"https://restcountries.com/v3.1/{req_type}/" + query_params)
    message = str(req.capital if req_type == "capital" else req.name.comon)
    self.wfile.write(message.encode())
    return

