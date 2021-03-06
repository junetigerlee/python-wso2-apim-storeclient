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


class ThrottlingTierCollectionApi(object):
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

    def tiers_tier_level_get(self, tier_level, **kwargs):
        """
        Get available tiers 
        This operation can be used to retrieve all the tiers available for the provided tier level. Tier level should be specified as a path parameter and should be one of `api` and `application`.  **NOTE**: * API tiers are the ones that is available during subscription of an application to an API. Hence they are also called subscription tiers and are same as the subscription policies in Admin REST API. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.tiers_tier_level_get(tier_level, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str tier_level: List API or Application type tiers.  (required)
        :param int limit: Maximum size of resource array to return. 
        :param int offset: Starting point within the complete list of items qualified. 
        :param str x_wso2_tenant: For cross-tenant invocations, this is used to specify the tenant domain, where the resource need to be   retirieved from. 
        :param str accept: Media types acceptable for the response. Default is application/json. 
        :param str if_none_match: Validator for conditional requests; based on the ETag of the formerly retrieved variant of the resourec. 
        :return: list[TierList]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.tiers_tier_level_get_with_http_info(tier_level, **kwargs)
        else:
            (data) = self.tiers_tier_level_get_with_http_info(tier_level, **kwargs)
            return data

    def tiers_tier_level_get_with_http_info(self, tier_level, **kwargs):
        """
        Get available tiers 
        This operation can be used to retrieve all the tiers available for the provided tier level. Tier level should be specified as a path parameter and should be one of `api` and `application`.  **NOTE**: * API tiers are the ones that is available during subscription of an application to an API. Hence they are also called subscription tiers and are same as the subscription policies in Admin REST API. 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.tiers_tier_level_get_with_http_info(tier_level, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str tier_level: List API or Application type tiers.  (required)
        :param int limit: Maximum size of resource array to return. 
        :param int offset: Starting point within the complete list of items qualified. 
        :param str x_wso2_tenant: For cross-tenant invocations, this is used to specify the tenant domain, where the resource need to be   retirieved from. 
        :param str accept: Media types acceptable for the response. Default is application/json. 
        :param str if_none_match: Validator for conditional requests; based on the ETag of the formerly retrieved variant of the resourec. 
        :return: list[TierList]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tier_level', 'limit', 'offset', 'x_wso2_tenant', 'accept', 'if_none_match']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method tiers_tier_level_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tier_level' is set
        if ('tier_level' not in params) or (params['tier_level'] is None):
            raise ValueError("Missing the required parameter `tier_level` when calling `tiers_tier_level_get`")


        collection_formats = {}

        path_params = {}
        if 'tier_level' in params:
            path_params['tierLevel'] = params['tier_level']

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))
        if 'offset' in params:
            query_params.append(('offset', params['offset']))

        header_params = {}
        if 'x_wso2_tenant' in params:
            header_params['X-WSO2-Tenant'] = params['x_wso2_tenant']
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
        auth_settings = []

        return self.api_client.call_api('/tiers/{tierLevel}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[TierList]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
