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


class DocumentIndividualApi(object):
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

    def apis_api_id_documents_document_id_content_get(self, api_id, document_id, **kwargs):
        """
        Get the content of an API document 
        This operation can be used to retrive the content of an API's document.  The document can be of 3 types. In each cases responses are different.  1. **Inline type**:    The content of the document will be retrieved in `text/plain` content type 2. **FILE type**:     The file will be downloaded with the related content type (eg. `application/pdf`) 3. **URL type**:     The client will recieve the URL of the document as the Location header with the response with - `303 See Other`  `X-WSO2-Tenant` header can be used to retrive the content of a document of an API that belongs to a different tenant domain. If not specified super tenant will be used. If Authorization header is present in the request, the user's tenant associated with the access token will be used.  **NOTE:** * This operation does not require an Authorization header by default. But in order to see a restricted API's document content, you need to provide Authorization header.         
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.apis_api_id_documents_document_id_content_get(api_id, document_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_id: **API ID** consisting of the **UUID** of the API. The combination of the provider of the API, name of the API and the version is also accepted as a valid API ID. Should be formatted as **provider-name-version**.  (required)
        :param str document_id: Document Identifier  (required)
        :param str x_wso2_tenant: For cross-tenant invocations, this is used to specify the tenant domain, where the resource need to be   retirieved from. 
        :param str accept: Media types acceptable for the response. Default is application/json. 
        :param str if_none_match: Validator for conditional requests; based on the ETag of the formerly retrieved variant of the resourec. 
        :param str if_modified_since: Validator for conditional requests; based on Last Modified header of the formerly retrieved variant of the resource. 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.apis_api_id_documents_document_id_content_get_with_http_info(api_id, document_id, **kwargs)
        else:
            (data) = self.apis_api_id_documents_document_id_content_get_with_http_info(api_id, document_id, **kwargs)
            return data

    def apis_api_id_documents_document_id_content_get_with_http_info(self, api_id, document_id, **kwargs):
        """
        Get the content of an API document 
        This operation can be used to retrive the content of an API's document.  The document can be of 3 types. In each cases responses are different.  1. **Inline type**:    The content of the document will be retrieved in `text/plain` content type 2. **FILE type**:     The file will be downloaded with the related content type (eg. `application/pdf`) 3. **URL type**:     The client will recieve the URL of the document as the Location header with the response with - `303 See Other`  `X-WSO2-Tenant` header can be used to retrive the content of a document of an API that belongs to a different tenant domain. If not specified super tenant will be used. If Authorization header is present in the request, the user's tenant associated with the access token will be used.  **NOTE:** * This operation does not require an Authorization header by default. But in order to see a restricted API's document content, you need to provide Authorization header.         
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.apis_api_id_documents_document_id_content_get_with_http_info(api_id, document_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_id: **API ID** consisting of the **UUID** of the API. The combination of the provider of the API, name of the API and the version is also accepted as a valid API ID. Should be formatted as **provider-name-version**.  (required)
        :param str document_id: Document Identifier  (required)
        :param str x_wso2_tenant: For cross-tenant invocations, this is used to specify the tenant domain, where the resource need to be   retirieved from. 
        :param str accept: Media types acceptable for the response. Default is application/json. 
        :param str if_none_match: Validator for conditional requests; based on the ETag of the formerly retrieved variant of the resourec. 
        :param str if_modified_since: Validator for conditional requests; based on Last Modified header of the formerly retrieved variant of the resource. 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_id', 'document_id', 'x_wso2_tenant', 'accept', 'if_none_match', 'if_modified_since']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method apis_api_id_documents_document_id_content_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_id' is set
        if ('api_id' not in params) or (params['api_id'] is None):
            raise ValueError("Missing the required parameter `api_id` when calling `apis_api_id_documents_document_id_content_get`")
        # verify the required parameter 'document_id' is set
        if ('document_id' not in params) or (params['document_id'] is None):
            raise ValueError("Missing the required parameter `document_id` when calling `apis_api_id_documents_document_id_content_get`")


        collection_formats = {}

        path_params = {}
        if 'api_id' in params:
            path_params['apiId'] = params['api_id']
        if 'document_id' in params:
            path_params['documentId'] = params['document_id']

        query_params = []

        header_params = {}
        if 'x_wso2_tenant' in params:
            header_params['X-WSO2-Tenant'] = params['x_wso2_tenant']
        if 'accept' in params:
            header_params['Accept'] = params['accept']
        if 'if_none_match' in params:
            header_params['If-None-Match'] = params['if_none_match']
        if 'if_modified_since' in params:
            header_params['If-Modified-Since'] = params['if_modified_since']

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

        return self.api_client.call_api('/apis/{apiId}/documents/{documentId}/content', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def apis_api_id_documents_document_id_get(self, api_id, document_id, **kwargs):
        """
        Get a document of an API 
        This operation can be used to retrieve a particular document's metadata associated with an API.  `X-WSO2-Tenant` header can be used to retrive a document of an API that belongs to a different tenant domain. If not specified super tenant will be used. If Authorization header is present in the request, the user's tenant associated with the access token will be used.  **NOTE:** * This operation does not require an Authorization header by default. But in order to see a restricted API's document, you need to provide Authorization header.         
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.apis_api_id_documents_document_id_get(api_id, document_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_id: **API ID** consisting of the **UUID** of the API. The combination of the provider of the API, name of the API and the version is also accepted as a valid API ID. Should be formatted as **provider-name-version**.  (required)
        :param str document_id: Document Identifier  (required)
        :param str x_wso2_tenant: For cross-tenant invocations, this is used to specify the tenant domain, where the resource need to be   retirieved from. 
        :param str accept: Media types acceptable for the response. Default is application/json. 
        :param str if_none_match: Validator for conditional requests; based on the ETag of the formerly retrieved variant of the resourec. 
        :param str if_modified_since: Validator for conditional requests; based on Last Modified header of the formerly retrieved variant of the resource. 
        :return: Document1
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.apis_api_id_documents_document_id_get_with_http_info(api_id, document_id, **kwargs)
        else:
            (data) = self.apis_api_id_documents_document_id_get_with_http_info(api_id, document_id, **kwargs)
            return data

    def apis_api_id_documents_document_id_get_with_http_info(self, api_id, document_id, **kwargs):
        """
        Get a document of an API 
        This operation can be used to retrieve a particular document's metadata associated with an API.  `X-WSO2-Tenant` header can be used to retrive a document of an API that belongs to a different tenant domain. If not specified super tenant will be used. If Authorization header is present in the request, the user's tenant associated with the access token will be used.  **NOTE:** * This operation does not require an Authorization header by default. But in order to see a restricted API's document, you need to provide Authorization header.         
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.apis_api_id_documents_document_id_get_with_http_info(api_id, document_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_id: **API ID** consisting of the **UUID** of the API. The combination of the provider of the API, name of the API and the version is also accepted as a valid API ID. Should be formatted as **provider-name-version**.  (required)
        :param str document_id: Document Identifier  (required)
        :param str x_wso2_tenant: For cross-tenant invocations, this is used to specify the tenant domain, where the resource need to be   retirieved from. 
        :param str accept: Media types acceptable for the response. Default is application/json. 
        :param str if_none_match: Validator for conditional requests; based on the ETag of the formerly retrieved variant of the resourec. 
        :param str if_modified_since: Validator for conditional requests; based on Last Modified header of the formerly retrieved variant of the resource. 
        :return: Document1
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_id', 'document_id', 'x_wso2_tenant', 'accept', 'if_none_match', 'if_modified_since']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method apis_api_id_documents_document_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_id' is set
        if ('api_id' not in params) or (params['api_id'] is None):
            raise ValueError("Missing the required parameter `api_id` when calling `apis_api_id_documents_document_id_get`")
        # verify the required parameter 'document_id' is set
        if ('document_id' not in params) or (params['document_id'] is None):
            raise ValueError("Missing the required parameter `document_id` when calling `apis_api_id_documents_document_id_get`")


        collection_formats = {}

        path_params = {}
        if 'api_id' in params:
            path_params['apiId'] = params['api_id']
        if 'document_id' in params:
            path_params['documentId'] = params['document_id']

        query_params = []

        header_params = {}
        if 'x_wso2_tenant' in params:
            header_params['X-WSO2-Tenant'] = params['x_wso2_tenant']
        if 'accept' in params:
            header_params['Accept'] = params['accept']
        if 'if_none_match' in params:
            header_params['If-None-Match'] = params['if_none_match']
        if 'if_modified_since' in params:
            header_params['If-Modified-Since'] = params['if_modified_since']

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

        return self.api_client.call_api('/apis/{apiId}/documents/{documentId}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Document1',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)