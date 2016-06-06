#!/bin/bash
qingcloudclient terminate-instances \
--access_key_id YOURACCESSKEYID \
--instances i-7ulvz0st \
--signature_method HmacSHA256 \
--signature_version 1 \
--api_version 1 \
--zone pek2 \
--secret_access_key YOURSECRETACCESSKEY
