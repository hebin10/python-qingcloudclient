# -*- coding: utf-8 -*-

import sys
import json
import urllib
import base64
import hmac
import datetime
from hashlib import sha1, sha256

def dict_to_sorted_tuple(myDict):
    keys = myDict.keys()
    keys.sort()
    result = ()
    for k in keys:
        result += ((k, myDict[k]),)
    return result

def get_encoded_url(params):
    return urllib.urlencode(params)

def get_string_to_sign(string):
    return 'GET\n/iaas/\n'+string

def get_signature(string, secret_access_key, method='HmacSHA256'):
    if method == 'HmacSHA256':
        h = hmac.new(secret_access_key, digestmod=sha256)
    elif method == 'HmacSHA1':
        h = hmac.new(secret_access_key, digestmod=sha1)
    else:
        sys.exit(-1)
    h.update(string)
    sign = base64.b64encode(h.digest()).strip()
    signature = urllib.quote_plus(sign)
    return signature

def get_signed_params(params, secret_key, method):
    prams_tuple = dict_to_sorted_tuple(params)
    encoded_params = get_encoded_url(prams_tuple)
    params_to_sign = get_string_to_sign(encoded_params)
    signature = get_signature(params_to_sign, secret_key, method)
    return '/iaas/?'+encoded_params+'&signature='+signature

def get_utc_time_stamp():
    return datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

def string_to_json(string):
    try:
        decoded = json.loads(string)
        return json.dumps(decoded, sort_keys=True, indent=4)
    except (ValueError, KeyError, TypeError):
        return None

def parse_array_value(name, parsed_args, params_dict):
    if name in parsed_args:
        value = getattr(parsed_args, name, None)
        if value:
            value_dict = value.split(',')
            for i in range(0, len(value_dict)):
                params_dict[name+'.'+str(i+1)] = value_dict[i]
