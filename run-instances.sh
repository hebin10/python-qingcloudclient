#!/bin/bash
qingcloudclient run-instances \
--access_key_id YOURACCESSKEYID \
--count 1 \
--instance_name test06 \
--cpu 1 \
--memory 1024 \
--login_mode passwd \
--login_passwd cecgw1QAZ \
--signature_method HmacSHA256 \
--signature_version 1 \
--api_version 1 \
--vxnets vxnet-0 \
--zone pek2 \
--image_id centos63x64a \
--secret_access_key YOURSECRETACCESSKEY
