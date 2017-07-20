# swagger_client.ThrottlingTierIndividualApi

All URIs are relative to *https://apis.wso2.com/api/am/store/v0.11*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tiers_tier_level_tier_name_get**](ThrottlingTierIndividualApi.md#tiers_tier_level_tier_name_get) | **GET** /tiers/{tierLevel}/{tierName} | Get details of a tier 


# **tiers_tier_level_tier_name_get**
> Tier1 tiers_tier_level_tier_name_get(tier_name, tier_level, x_wso2_tenant=x_wso2_tenant, accept=accept, if_none_match=if_none_match, if_modified_since=if_modified_since)

Get details of a tier 

This operation can be used to retrieve details of a single tier by specifying the tier level and tier name. 

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ThrottlingTierIndividualApi()
tier_name = 'tier_name_example' # str | Tier name 
tier_level = 'tier_level_example' # str | List API or Application type tiers. 
x_wso2_tenant = 'x_wso2_tenant_example' # str | For cross-tenant invocations, this is used to specify the tenant domain, where the resource need to be   retirieved from.  (optional)
accept = 'application/json' # str | Media types acceptable for the response. Default is application/json.  (optional) (default to application/json)
if_none_match = 'if_none_match_example' # str | Validator for conditional requests; based on the ETag of the formerly retrieved variant of the resourec.  (optional)
if_modified_since = 'if_modified_since_example' # str | Validator for conditional requests; based on Last Modified header of the formerly retrieved variant of the resource.  (optional)

try: 
    # Get details of a tier 
    api_response = api_instance.tiers_tier_level_tier_name_get(tier_name, tier_level, x_wso2_tenant=x_wso2_tenant, accept=accept, if_none_match=if_none_match, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ThrottlingTierIndividualApi->tiers_tier_level_tier_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tier_name** | **str**| Tier name  | 
 **tier_level** | **str**| List API or Application type tiers.  | 
 **x_wso2_tenant** | **str**| For cross-tenant invocations, this is used to specify the tenant domain, where the resource need to be   retirieved from.  | [optional] 
 **accept** | **str**| Media types acceptable for the response. Default is application/json.  | [optional] [default to application/json]
 **if_none_match** | **str**| Validator for conditional requests; based on the ETag of the formerly retrieved variant of the resourec.  | [optional] 
 **if_modified_since** | **str**| Validator for conditional requests; based on Last Modified header of the formerly retrieved variant of the resource.  | [optional] 

### Return type

[**Tier1**](Tier1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

