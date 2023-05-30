"""
.. module: cloudaux.tests.aws.conftest
    :platform: Unix
    :copyright: (c) 2018 by Netflix Inc., see AUTHORS for more
    :license: Apache, see LICENSE for more details.
.. moduleauthor:: Mike Grima <mgrima@netflix.com>
"""
import os

import pytest

from moto import mock_sts
import boto3


@pytest.fixture(scope="function")
def conn_dict():
    return {
        "region": "us-east-1"
    }


@pytest.fixture(scope='function')
def aws_credentials():
    os.environ['AWS_ACCESS_KEY_ID'] = 'testing'
    os.environ['AWS_SECRET_ACCESS_KEY'] = 'testing'
    os.environ['AWS_SECURITY_TOKEN'] = 'testing'
    os.environ['AWS_SESSION_TOKEN'] = 'testing'


@pytest.fixture(scope="function")
def sts(aws_credentials, conn_dict):
    with mock_sts():
        yield boto3.client("sts", region_name="us-east-1")
