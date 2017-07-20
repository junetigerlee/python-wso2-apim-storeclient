# swagger_client.ThrottlingTierCollectionApi

All URIs are relative to *https://apis.wso2.com/api/am/store/v0.11*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tiers_tier_level_get**](ThrottlingTierCollectionApi.md#tiers_tier_level_get) | **GET** /tiers/{tierLevel} | Get available tiers 


# **tiers_tier_level_get**
> list[TierList] tiers_tier_level_get(tier_level, limit=limit, offset=offset, x_wso2_tenant=x_wso2_tenant, accept=accept, if_none_match=if_none_match)

Get available tiers 

This operation can be used to retrieve all the tiers available for the provided tier level. Tier level should be specified as a path parameter and should be one of `api` and `application`.  **NOTE**: * API tiers are the ones that is available during subscription of an application to an API. Hence they are also called subscription tiers and are same as the subscription policies in Admin REST API. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ThrottlingTierCollectionApi()
tier_level = 'tier_level_example' # str | List API or Application type tiers. 
limit = 25 # int | Maximum size of resource array to return.  (optional) (default to 25)
offset = 0 # int | Starting point within the complete list of items qualified.  (optional) (default to 0)
x_wso2_tenant = 'x_wso2_tenant_example' # str | For cross-tenant invocations, this is used to specify the tenant domain, where the resource need to be   retirieved from.  (optional)
accept = 'application/json' # str | Media types acceptable for the response. Default is application/json.  (optional) (default to application/json)
if_none_match = 'if_none_match_example' # str | Validator for conditional requests; based on the ETag of the formerly retrieved variant of the resourec.  (optional)

try: 
    # Get available tiers 
    api_response = api_instance.tiers_tier_level_get(tier_level, limit=limit, offset=offset, x_wso2_tenant=x_wso2_tenant, accept=accept, if_none_match=if_none_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThrottlingTierCollectionApi->tiers_tier_level_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tier_level** | **str**| List API or Application type tiers.  | 
 **limit** | **int**| Maximum size of resource array to return.  | [optional] [default to 25]
 **offset** | **int**| Starting point within the complete list of items qualified.  | [optional] [default to 0]
 **x_wso2_tenant** | **str**| For cross-tenant invocations, this is used to specify the tenant domain, where the resource need to be   retirieved from.  | [optional] 
 **accept** | **str**| Media types acceptable for the response. Default is application/json.  | [optional] [default to application/json]
 **if_none_match** | **str**| Validator for conditional requests; based on the ETag of the formerly retrieved variant of the resourec.  | [optional] 

### Return type

[**list[TierList]**](TierList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

