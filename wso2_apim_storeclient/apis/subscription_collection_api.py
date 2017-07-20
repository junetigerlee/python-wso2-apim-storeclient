# coding: utf-8

"""
    WSO2 API Manager - Store

    This specifies a **RESTful API** for WSO2 **API Manager** - Store.  Please see [full swagger definition](https://raw.githubusercontent.com/wso2/carbon-apimgt/v6.0.4/components/apimgt/org.wso2.carbon.apimgt.rest.api.store/src/main/resources/store-api.yaml) of the API which is written using [swagger 2.0](http://swagger.io/) specification. 

    OpenAPI spec version: 0.11.0
    Contact: architecture@wso2.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class SubscriptionCollectionApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def subscriptions_get(self, api_id, application_id, **kwargs):
        """
        Get all subscriptions 
        This operation can be used to retrieve a list of subscriptions of the user associated with the provided access token. This operation is capable of  1. Retrieving applications which are subscibed to a specific API. `GET https://127.0.0.1:9443/api/am/store/v0.11/subscriptions?apiId=c43a325c-260b-4302-81cb-768eafaa3aed`  2. Retrieving APIs which are subscribed by a specific application. `GET https://127.0.0.1:9443/api/am/store/v0.11/subscriptions?applicationId=c43a325c-260b-4302-81cb-768eafaa3aed`  **IMPORTANT:** * It is mandatory to provide either **apiId** or **applicationId**. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.subscriptions_get(api_id, application_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_id: **API ID** consisting of the **UUID** of the API. The combination of the provider of the API, name of the API and the version is also accepted as a valid API I. Should be formatted as **provider-name-version**.  (required)
        :param str application_id: Application Identifier consisting of the UUID of the Application.  (required)
        :param str group_id: Application Group Id 
        :param int offset: Starting point within the complete list of items qualified. 
        :param int limit: Maximum size of resource array to return. 
        :param str accept: Media types acceptable for the response. Default is application/json. 
        :param str if_none_match: Validator for conditional requests; based on the ETag of the formerly retrieved variant of the resourec. 
        :return: SubscriptionList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.subscriptions_get_with_http_info(api_id, application_id, **kwargs)
        else:
            (data) = self.subscriptions_get_with_http_info(api_id, application_id, **kwargs)
            return data

    def subscriptions_get_with_http_info(self, api_id, application_id, **kwargs):
        """
        Get all subscriptions 
        This operation can be used to retrieve a list of subscriptions of the user associated with the provided access token. This operation is capable of  1. Retrieving applications which are subscibed to a specific API. `GET https://127.0.0.1:9443/api/am/store/v0.11/subscriptions?apiId=c43a325c-260b-4302-81cb-768eafaa3aed`  2. Retrieving APIs which are subscribed by a specific application. `GET https://127.0.0.1:9443/api/am/store/v0.11/subscriptions?applicationId=c43a325c-260b-4302-81cb-768eafaa3aed`  **IMPORTANT:** * It is mandatory to provide either **apiId** or **applicationId**. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.subscriptions_get_with_http_info(api_id, application_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_id: **API ID** consisting of the **UUID** of the API. The combination of the provider of the API, name of the API and the version is also accepted as a valid API I. Should be formatted as **provider-name-version**.  (required)
        :param str application_id: Application Identifier consisting of the UUID of the Application.  (required)
        :param str group_id: Application Group Id 
        :param int offset: Starting point within the complete list of items qualified. 
        :param int limit: Maximum size of resource array to return. 
        :param str accept: Media types acceptable for the response. Default is application/json. 
        :param str if_none_match: Validator for conditional requests; based on the ETag of the formerly retrieved variant of the resourec. 
        :return: SubscriptionList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_id', 'application_id', 'group_id', 'offset', 'limit', 'accept', 'if_none_match']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method subscriptions_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_id' is set
        if ('api_id' not in params) or (params['api_id'] is None):
            raise ValueError("Missing the required parameter `api_id` when calling `subscriptions_get`")
        # verify the required parameter 'application_id' is set
        if ('application_id' not in params) or (params['application_id'] is None):
            raise ValueError("Missing the required parameter `application_id` when calling `subscriptions_get`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'api_id' in params:
            query_params.append(('apiId', params['api_id']))
        if 'application_id' in params:
            query_params.append(('applicationId', params['application_id']))
        if 'group_id' in params:
            query_params.append(('groupId', params['group_id']))
        if 'offset' in params:
            query_params.append(('offset', params['offset']))
        if 'limit' in params:
            query_params.append(('limit', params['limit']))

        header_params = {}
        if 'accept' in params:
            header_params['Accept'] = params['accept']
        if 'if_none_match' in params:
            header_params['If-None-Match'] = params['if_none_match']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['OAuth2']

        return self.api_client.call_api('/subscriptions', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='SubscriptionList',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
