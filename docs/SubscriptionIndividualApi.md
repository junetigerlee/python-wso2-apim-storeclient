# swagger_client.SubscriptionIndividualApi

All URIs are relative to *https://apis.wso2.com/api/am/store/v0.11*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subscriptions_post**](SubscriptionIndividualApi.md#subscriptions_post) | **POST** /subscriptions | Add a new subscription 
[**subscriptions_subscription_id_delete**](SubscriptionIndividualApi.md#subscriptions_subscription_id_delete) | **DELETE** /subscriptions/{subscriptionId} | Remove a subscription 
[**subscriptions_subscription_id_get**](SubscriptionIndividualApi.md#subscriptions_subscription_id_get) | **GET** /subscriptions/{subscriptionId} | Get details of a subscription 


# **subscriptions_post**
> Subscription1 subscriptions_post(body, content_type)

Add a new subscription 

This operation can be used to add a new subscription providing the id of the API and the application. 

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
api_instance = swagger_client.SubscriptionIndividualApi()
body = swagger_client.Subscription2() # Subscription2 | Subscription object that should to be added 
content_type = 'application/json' # str | Media type of the entity in the body. Default is application/json.  (default to application/json)

try: 
    # Add a new subscription 
    api_response = api_instance.subscriptions_post(body, content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionIndividualApi->subscriptions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Subscription2**](Subscription2.md)| Subscription object that should to be added  | 
 **content_type** | **str**| Media type of the entity in the body. Default is application/json.  | [default to application/json]

### Return type

[**Subscription1**](Subscription1.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscriptions_subscription_id_delete**
> subscriptions_subscription_id_delete(subscription_id, if_match=if_match, if_unmodified_since=if_unmodified_since)

Remove a subscription 

This operation can be used to remove a subscription. 

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
api_instance = swagger_client.SubscriptionIndividualApi()
subscription_id = 'subscription_id_example' # str | Subscription Id 
if_match = 'if_match_example' # str | Validator for conditional requests; based on ETag.  (optional)
if_unmodified_since = 'if_unmodified_since_example' # str | Validator for conditional requests; based on Last Modified header.  (optional)

try: 
    # Remove a subscription 
    api_instance.subscriptions_subscription_id_delete(subscription_id, if_match=if_match, if_unmodified_since=if_unmodified_since)
except ApiException as e:
    print("Exception when calling SubscriptionIndividualApi->subscriptions_subscription_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Subscription Id  | 
 **if_match** | **str**| Validator for conditional requests; based on ETag.  | [optional] 
 **if_unmodified_since** | **str**| Validator for conditional requests; based on Last Modified header.  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscriptions_subscription_id_get**
> Subscription1 subscriptions_subscription_id_get(subscription_id, accept=accept, if_none_match=if_none_match, if_modified_since=if_modified_since)

Get details of a subscription 

This operation can be used to get details of a single subscription. 

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
api_instance = swagger_client.SubscriptionIndividualApi()
subscription_id = 'subscription_id_example' # str | Subscription Id 
accept = 'application/json' # str | Media types acceptable for the response. Default is application/json.  (optional) (default to application/json)
if_none_match = 'if_none_match_example' # str | Validator for conditional requests; based on the ETag of the formerly retrieved variant of the resourec.  (optional)
if_modified_since = 'if_modified_since_example' # str | Validator for conditional requests; based on Last Modified header of the formerly retrieved variant of the resource.  (optional)

try: 
    # Get details of a subscription 
    api_response = api_instance.subscriptions_subscription_id_get(subscription_id, accept=accept, if_none_match=if_none_match, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionIndividualApi->subscriptions_subscription_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| Subscription Id  | 
 **accept** | **str**| Media types acceptable for the response. Default is application/json.  | [optional] [default to application/json]
 **if_none_match** | **str**| Validator for conditional requests; based on the ETag of the formerly retrieved variant of the resourec.  | [optional] 
 **if_modified_since** | **str**| Validator for conditional requests; based on Last Modified header of the formerly retrieved variant of the resource.  | [optional] 

### Return type

[**Subscription1**](Subscription1.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

