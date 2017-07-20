# coding: utf-8

"""
    WSO2 API Manager - Store

    This specifies a **RESTful API** for WSO2 **API Manager** - Store.  Please see [full swagger definition](https://raw.githubusercontent.com/wso2/carbon-apimgt/v6.0.4/components/apimgt/org.wso2.carbon.apimgt.rest.api.store/src/main/resources/store-api.yaml) of the API which is written using [swagger 2.0](http://swagger.io/) specification. 

    OpenAPI spec version: 0.11.0
    Contact: architecture@wso2.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import wso2_apim_storeclient
from wso2_apim_storeclient.rest import ApiException
from wso2_apim_storeclient.apis.subscription_individual_api import SubscriptionIndividualApi


class TestSubscriptionIndividualApi(unittest.TestCase):
    """ SubscriptionIndividualApi unit test stubs """

    def setUp(self):
        self.api = wso2_apim_storeclient.apis.subscription_individual_api.SubscriptionIndividualApi()

    def tearDown(self):
        pass

    def test_subscriptions_post(self):
        """
        Test case for subscriptions_post

        Add a new subscription 
        """
        pass

    def test_subscriptions_subscription_id_delete(self):
        """
        Test case for subscriptions_subscription_id_delete

        Remove a subscription 
        """
        pass

    def test_subscriptions_subscription_id_get(self):
        """
        Test case for subscriptions_subscription_id_get

        Get details of a subscription 
        """
        pass


if __name__ == '__main__':
    unittest.main()
