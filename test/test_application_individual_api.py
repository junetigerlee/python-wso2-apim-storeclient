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
from wso2_apim_storeclient.apis.application_individual_api import ApplicationIndividualApi


class TestApplicationIndividualApi(unittest.TestCase):
    """ ApplicationIndividualApi unit test stubs """

    def setUp(self):
        self.api = wso2_apim_storeclient.apis.application_individual_api.ApplicationIndividualApi()

    def tearDown(self):
        pass

    def test_applications_application_id_delete(self):
        """
        Test case for applications_application_id_delete

        Remove an application 
        """
        pass

    def test_applications_application_id_get(self):
        """
        Test case for applications_application_id_get

        Get details of an application 
        """
        pass

    def test_applications_application_id_put(self):
        """
        Test case for applications_application_id_put

        Update an application 
        """
        pass

    def test_applications_generate_keys_post(self):
        """
        Test case for applications_generate_keys_post

        Generate keys for application 
        """
        pass

    def test_applications_post(self):
        """
        Test case for applications_post

        Create a new application 
        """
        pass


if __name__ == '__main__':
    unittest.main()
