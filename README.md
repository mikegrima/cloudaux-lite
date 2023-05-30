# cloudaux-lite

[![Version](http://img.shields.io/pypi/v/cloudaux-lite.svg?style=flat)](https://pypi.python.org/pypi/cloudaux-lite/)

## Special Note: This is a slimmed-down fork of Netflix-Skunkworks/cloudaux
The original source for [CloudAux](https://github.org/Netflix-Skunkworks/cloudaux) is mostly not supported and contains a lot of code that has breaking changes with updates to boto over time.
It also contained support for non-AWS cloud providers which have breaking library changes over time as well. This fork removes all the problematic components and non-supported components to make this library
only consist of AWS support for the following very simple things:

1. Decorator for STS role assumption
2. Decorator for pagination
3. The CloudAux object

### What was removed?
This fork removed the following components:

* All things non AWS, like GCP, Azure, and OpenStack
* The orchestration logic
* The `iter_account_region` decorator
* The `rate_limited` decorator 

The primary things left are:
* The `sts_conn` decorator
* The `pagination` decorator
* The `CloudAux` class

If you use the above 3 things only, then this is a drop-in replacement. The imports and everything are exactly the same. Simply `pip install cloudaux-lite` instead of `cloudaux` and you should be good to go!

## Older support?
If you have a need to supporting the older CloudAux stuff, then continue using the Netflix cloudaux package version < 2.

## Features

 - Intelligent connection caching.
 - Handles pagination for certain client methods.
 - Multi-account sts:assumerole abstraction.

## Install

    pip install cloudaux-lite

### AWS Example

    # Using the CloudAux class
    from cloudaux import CloudAux
    CloudAux.go('kms.client.list_aliases', **conn_details)

    ca = CloudAux(**conn_details)
    ca.call('kms.client.list_aliases')

    # directly asking for a boto3 connection:
    from cloudaux.aws.sts import boto3_cached_conn
    conn = boto3_cached_conn('ec2', **conn_details)

    # Over your entire environment:
    from cloudaux.decorators import iter_account_region

    accounts = ['000000000000', '111111111111']

    conn_details = {
        'assume_role': 'MyRole',
        'session_name': 'MySession',
        'conn_type': 'boto3'
    }

    # If you want your role to be read-only, you can assume your role and add the read_only flag to connection details
    # to inherit the AWS ReadOnlyAccess policy. This flag defaults to False
    # The permissions from the role being assumed will be limited to Read and List only
    conn_details = {
        'account_number': '111111111111',
        'assume_role': 'MyRole',
        'session_name': 'MySession',
        'region': 'us-east-1',
        'read_only': True
    }

