import utils

body = {
    "access_key_id": "QYACCESSKEYIDEXAMPLE",
    "action": "RunInstances",
    "count": 1,
    "image_id": "centos64x86a",
    "instance_name": "demo",
    "instance_type": "small_b",
    "login_mode": "passwd",
    "login_passwd": "QingCloud20130712",
    "signature_method": "HmacSHA256",
    "signature_version": 1,
    "time_stamp": "2013-08-27T14:30:10Z",
    "version": 1,
    "vxnets.1": "vxnet-0",
    "zone": "pek1"
}

secret_access_key = 'SECRETACCESSKEY'

body = utils.dict_to_sorted_tuple(body)

encoded_body = utils.get_encoded_url(body)

string_to_sign = utils.get_string_to_sign(encoded_body)

signature = utils.get_signature(
    string_to_sign,
    secret_access_key,
    method='HmacSHA256'
)

print signature

import time
import datetime

print time.time()

print datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

string = 'abc_def'
print string.replace('_', '-')
print str('access_key_id'.split('_'))

string = '{"abc":123, "cde":456}'
print utils.string_to_json(string)

string = 'abc'
params = {'abc': '123,456,789'}
utils.parse_array_value(string, params)
print getattr(params, string, None)
