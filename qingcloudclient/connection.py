# -*- coding: utf-8 -*-

try:
    import httplib
except Exception:
    import http.client as httplib

HOST = 'api.qingcloud.com'
PORT = 443
METHOD = 'GET'


def get_response(url):
    conn = httplib.HTTPSConnection(HOST, port=PORT)
    conn.request(METHOD, url)
    res = conn.getresponse()
    return res
