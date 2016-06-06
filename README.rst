====================================================
qingcloudclient - A test CLI for some QingCloud APIs
====================================================

qingcloudclient is a python command-line client for some QingCloud APIs:
RunInstances, DescribeInstances and TerminateInstances. It is implemented base
on another CLI framework: cliff.

Setup
======

To use python virtualenv:

    $ sudo pip install virtualenv

    $ virtualenv .env
    
    $ source ./env/bin/activate
    
    (.env)$ cd python-qingcloudclient
    
    (.env)$ python setup.py install

To use the real  environment:

    $ cd python-qingcloudclient
    
    $ sudo python setup.py install

Virtualenv is recommended


Usage
=======

Note:

Qingcloudclient does not support reading arguments from file. So that you need
to present arguments required by typing it use keyboard.

1. Get help:

    $ qingcloudclient -h
    
    $ qingcloudclient command -h

    or

    $ qingcloudclient help command

command: run-instances, describe-instances, terminate-instances

2. run-instances:

    $ qingcloudclient run-instances
    
    --access_key_id YOURACCESSKEYID \
    
    --count 1 \
    
    --instance_name test05 \
    
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

This command will run a instance named test05 on zone - pek2.

3. describe-instances:

    $ qingcloudclient describe-instances \
    
    --access_key_id YOURACCESSKEYID \
    
    --signature_method HmacSHA256 \
    
    --signature_version 1 \
    
    --api_version 1 \
    
    --limit 1 \
    
    --zone pek2 \
    
    --secret_access_key YOURSECRETACCESSKEY

This command will show all of your instances information.

4. terminate-instances:

    $ ingcloudclient terminate-instances \
    
    --access_key_id YOURACCESSKEYID \
    
    --instances INSTANCE1_ID,INSTANCE2_ID,... \
    
    --signature_method HmacSHA256 \
    
    --signature_version 1 \
    
    --api_version 1 \
    
    --zone pek2 \
    
    --secret_access_key YOURSECRETACCESSKEY

This command will terminate instance(s) which id are INSTANCE1_ID,INSTANCE2_ID,...
