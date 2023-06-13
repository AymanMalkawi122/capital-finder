from http.server import BaseHTTPRequestHandler
import requests
from urllib import parse


class handler(BaseHTTPRequestHandler):
 
  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    url_components = parse.urlsplit(self.path)
    req_type = url_components.query.split("=")[0]
    if req_type == "country":
        req_type = "name"
    else: req_type = "capital"
    query_params = url_components.query.split("=")[1]
    req = requests.get(f"https://restcountries.com/v3.1/{req_type}/" + query_params)
    req = req.json()
    
    capital = req[0]["capital"][0]
    country = req[0]["name"]["common"]
    message = f"{capital} is the capital of {country}" if req_type == "capital" else f"The capital of {country} is {capital}."
    self.wfile.write(message.encode())
    return

