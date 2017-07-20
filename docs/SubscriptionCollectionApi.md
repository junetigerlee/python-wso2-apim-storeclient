# swagger_client.SubscriptionCollectionApi

All URIs are relative to *https://apis.wso2.com/api/am/store/v0.11*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subscriptions_get**](SubscriptionCollectionApi.md#subscriptions_get) | **GET** /subscriptions | Get all subscriptions 


# **subscriptions_get**
> SubscriptionList subscriptions_get(api_id, application_id, group_id=group_id, offset=offset, limit=limit, accept=accept, if_none_match=if_none_match)

Get all subscriptions 

This operation can be used to retrieve a list of subscriptions of the user associated with the provided access token. This operation is capable of  1. Retrieving applications which are subscibed to a specific API. `GET https://127.0.0.1:9443/api/am/store/v0.11/subscriptions?apiId=c43a325c-260b-4302-81cb-768eafaa3aed`  2. Retrieving APIs which are subscribed by a specific application. `GET https://127.0.0.1:9443/api/am/store/v0.11/subscriptions?applicationId=c43a325c-260b-4302-81cb-768eafaa3aed`  **IMPORTANT:** * It is mandatory to provide either **apiId** or **applicationId**. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.SubscriptionCollectionApi()
api_id = 'api_id_example' # str | **API ID** consisting of the **UUID** of the API. The combination of the provider of the API, name of the API and the version is also accepted as a valid API I. Should be formatted as **provider-name-version**. 
application_id = 'application_id_example' # str | Application Identifier consisting of the UUID of the Application. 
group_id = 'group_id_example' # str | Application Group Id  (optional)
offset = 0 # int | Starting point within the complete list of items qualified.  (optional) (default to 0)
limit = 25 # int | Maximum size of resource array to return.  (optional) (default to 25)
accept = 'application/json' # str | Media types acceptable for the response. Default is application/json.  (optional) (default to application/json)
if_none_match = 'if_none_match_example' # str | Validator for conditional requests; based on the ETag of the formerly retrieved variant of the resourec.  (optional)

try: 
    # Get all subscriptions 
    api_response = api_instance.subscriptions_get(api_id, application_id, group_id=group_id, offset=offset, limit=limit, accept=accept, if_none_match=if_none_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionCollectionApi->subscriptions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_id** | **str**| **API ID** consisting of the **UUID** of the API. The combination of the provider of the API, name of the API and the version is also accepted as a valid API I. Should be formatted as **provider-name-version**.  | 
 **application_id** | **str**| Application Identifier consisting of the UUID of the Application.  | 
 **group_id** | **str**| Application Group Id  | [optional] 
 **offset** | **int**| Starting point within the complete list of items qualified.  | [optional] [default to 0]
 **limit** | **int**| Maximum size of resource array to return.  | [optional] [default to 25]
 **accept** | **str**| Media types acceptable for the response. Default is application/json.  | [optional] [default to application/json]
 **if_none_match** | **str**| Validator for conditional requests; based on the ETag of the formerly retrieved variant of the resourec.  | [optional] 

### Return type

[**SubscriptionList**](SubscriptionList.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

