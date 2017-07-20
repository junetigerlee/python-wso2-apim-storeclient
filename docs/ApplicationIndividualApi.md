# swagger_client.ApplicationIndividualApi

All URIs are relative to *https://apis.wso2.com/api/am/store/v0.11*

Method | HTTP request | Description
------------- | ------------- | -------------
[**applications_application_id_delete**](ApplicationIndividualApi.md#applications_application_id_delete) | **DELETE** /applications/{applicationId} | Remove an application 
[**applications_application_id_get**](ApplicationIndividualApi.md#applications_application_id_get) | **GET** /applications/{applicationId} | Get details of an application 
[**applications_application_id_put**](ApplicationIndividualApi.md#applications_application_id_put) | **PUT** /applications/{applicationId} | Update an application 
[**applications_generate_keys_post**](ApplicationIndividualApi.md#applications_generate_keys_post) | **POST** /applications/generate-keys | Generate keys for application 
[**applications_post**](ApplicationIndividualApi.md#applications_post) | **POST** /applications | Create a new application 


# **applications_application_id_delete**
> applications_application_id_delete(application_id, if_match=if_match, if_unmodified_since=if_unmodified_since)

Remove an application 

This operation can be used to remove an application specifying its id. 

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
api_instance = swagger_client.ApplicationIndividualApi()
application_id = 'application_id_example' # str | Application Identifier consisting of the UUID of the Application. 
if_match = 'if_match_example' # str | Validator for conditional requests; based on ETag.  (optional)
if_unmodified_since = 'if_unmodified_since_example' # str | Validator for conditional requests; based on Last Modified header.  (optional)

try: 
    # Remove an application 
    api_instance.applications_application_id_delete(application_id, if_match=if_match, if_unmodified_since=if_unmodified_since)
except ApiException as e:
    print("Exception when calling ApplicationIndividualApi->applications_application_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application Identifier consisting of the UUID of the Application.  | 
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

# **applications_application_id_get**
> Application2 applications_application_id_get(application_id, accept=accept, if_none_match=if_none_match, if_modified_since=if_modified_since)

Get details of an application 

This operation can be used to retrieve details of an individual application specifying the application id in the URI. 

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
api_instance = swagger_client.ApplicationIndividualApi()
application_id = 'application_id_example' # str | Application Identifier consisting of the UUID of the Application. 
accept = 'application/json' # str | Media types acceptable for the response. Default is application/json.  (optional) (default to application/json)
if_none_match = 'if_none_match_example' # str | Validator for conditional requests; based on the ETag of the formerly retrieved variant of the resourec.  (optional)
if_modified_since = 'if_modified_since_example' # str | Validator for conditional requests; based on Last Modified header of the formerly retrieved variant of the resource.  (optional)

try: 
    # Get details of an application 
    api_response = api_instance.applications_application_id_get(application_id, accept=accept, if_none_match=if_none_match, if_modified_since=if_modified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationIndividualApi->applications_application_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application Identifier consisting of the UUID of the Application.  | 
 **accept** | **str**| Media types acceptable for the response. Default is application/json.  | [optional] [default to application/json]
 **if_none_match** | **str**| Validator for conditional requests; based on the ETag of the formerly retrieved variant of the resourec.  | [optional] 
 **if_modified_since** | **str**| Validator for conditional requests; based on Last Modified header of the formerly retrieved variant of the resource.  | [optional] 

### Return type

[**Application2**](Application2.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_application_id_put**
> Application2 applications_application_id_put(application_id, body, content_type, if_match=if_match, if_unmodified_since=if_unmodified_since)

Update an application 

This operation can be used to update an application. Upon succesfull you will retrieve the updated application as the response. 

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
api_instance = swagger_client.ApplicationIndividualApi()
application_id = 'application_id_example' # str | Application Identifier consisting of the UUID of the Application. 
body = swagger_client.Application3() # Application3 | Application object that needs to be updated 
content_type = 'application/json' # str | Media type of the entity in the body. Default is application/json.  (default to application/json)
if_match = 'if_match_example' # str | Validator for conditional requests; based on ETag.  (optional)
if_unmodified_since = 'if_unmodified_since_example' # str | Validator for conditional requests; based on Last Modified header.  (optional)

try: 
    # Update an application 
    api_response = api_instance.applications_application_id_put(application_id, body, content_type, if_match=if_match, if_unmodified_since=if_unmodified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationIndividualApi->applications_application_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application Identifier consisting of the UUID of the Application.  | 
 **body** | [**Application3**](Application3.md)| Application object that needs to be updated  | 
 **content_type** | **str**| Media type of the entity in the body. Default is application/json.  | [default to application/json]
 **if_match** | **str**| Validator for conditional requests; based on ETag.  | [optional] 
 **if_unmodified_since** | **str**| Validator for conditional requests; based on Last Modified header.  | [optional] 

### Return type

[**Application2**](Application2.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_generate_keys_post**
> ApplicationKeyDetails applications_generate_keys_post(application_id, body, content_type, if_match=if_match, if_unmodified_since=if_unmodified_since)

Generate keys for application 

This operation can be used to generate client Id and client secret for an application 

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
api_instance = swagger_client.ApplicationIndividualApi()
application_id = 'application_id_example' # str | Application Identifier consisting of the UUID of the Application. 
body = swagger_client.ApplicationKeyGenerationRequestObject() # ApplicationKeyGenerationRequestObject | Application object the keys of which are to be generated 
content_type = 'application/json' # str | Media type of the entity in the body. Default is application/json.  (default to application/json)
if_match = 'if_match_example' # str | Validator for conditional requests; based on ETag.  (optional)
if_unmodified_since = 'if_unmodified_since_example' # str | Validator for conditional requests; based on Last Modified header.  (optional)

try: 
    # Generate keys for application 
    api_response = api_instance.applications_generate_keys_post(application_id, body, content_type, if_match=if_match, if_unmodified_since=if_unmodified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationIndividualApi->applications_generate_keys_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application Identifier consisting of the UUID of the Application.  | 
 **body** | [**ApplicationKeyGenerationRequestObject**](ApplicationKeyGenerationRequestObject.md)| Application object the keys of which are to be generated  | 
 **content_type** | **str**| Media type of the entity in the body. Default is application/json.  | [default to application/json]
 **if_match** | **str**| Validator for conditional requests; based on ETag.  | [optional] 
 **if_unmodified_since** | **str**| Validator for conditional requests; based on Last Modified header.  | [optional] 

### Return type

[**ApplicationKeyDetails**](ApplicationKeyDetails.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **applications_post**
> Application2 applications_post(body, content_type)

Create a new application 

This operation can be used to create a new application specifying the details of the application in the payload. 

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
api_instance = swagger_client.ApplicationIndividualApi()
body = swagger_client.Application1() # Application1 | Application object that is to be created. 
content_type = 'application/json' # str | Media type of the entity in the body. Default is application/json.  (default to application/json)

try: 
    # Create a new application 
    api_response = api_instance.applications_post(body, content_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApplicationIndividualApi->applications_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Application1**](Application1.md)| Application object that is to be created.  | 
 **content_type** | **str**| Media type of the entity in the body. Default is application/json.  | [default to application/json]

### Return type

[**Application2**](Application2.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

