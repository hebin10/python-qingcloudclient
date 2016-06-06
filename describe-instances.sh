#!/bin/bash
qingcloudclient describe-instances \
--access_key_id YOURACCESSKEYID \
--signature_method HmacSHA256 \
--signature_version 1 \
--api_version 1 \
--zone pek2 \
--instances i-7ulvz0st \
--secret_access_key YOURSECRETACCESSKEY
