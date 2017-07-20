# python-wso2-apim-storeclient
This specifies a **RESTful API** for WSO2 **API Manager** - Store.  Please see [full swagger definition](https://raw.githubusercontent.com/wso2/carbon-apimgt/v6.0.4/components/apimgt/org.wso2.carbon.apimgt.rest.api.store/src/main/resources/store-api.yaml) of the API which is written using [swagger 2.0](http://swagger.io/) specification. 

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.11.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen
For more information, please visit [http://wso2.com/products/api-manager/](http://wso2.com/products/api-manager/)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import wso2_apim_storeclient 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import wso2_apim_storeclient
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import wso2_apim_storeclient
from wso2_apim_storeclient.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = wso2_apim_storeclient.APICollectionApi()
limit = 25 # int | Maximum size of resource array to return.  (optional) (default to 25)
offset = 0 # int | Starting point within the complete list of items qualified.  (optional) (default to 0)
x_wso2_tenant = 'x_wso2_tenant_example' # str | For cross-tenant invocations, this is used to specify the tenant domain, where the resource need to be   retirieved from.  (optional)
query = 'query_example' # str | **Search condition**.  You can search in attributes by using an **\"<attribute>:\"** modifier.  Eg. \"provider:wso2\" will match an API if the provider of the API is exactly \"wso2\".  Additionally you can use wildcards.  Eg. \"provider:wso2*\" will match an API if the provider of the API starts with \"wso2\".  Supported attribute modifiers are [**version, context, status, description, subcontext, doc, provider, tag**]  If no advanced attribute modifier has been specified, search will match the given query string against API Name.  (optional)
accept = 'application/json' # str | Media types acceptable for the response. Default is application/json.  (optional) (default to application/json)
if_none_match = 'if_none_match_example' # str | Validator for conditional requests; based on the ETag of the formerly retrieved variant of the resourec.  (optional)

try:
    # Retrieve/Search APIs 
    api_response = api_instance.apis_get(limit=limit, offset=offset, x_wso2_tenant=x_wso2_tenant, query=query, accept=accept, if_none_match=if_none_match)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APICollectionApi->apis_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://apis.wso2.com/api/am/store/v0.11*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*APICollectionApi* | [**apis_get**](docs/APICollectionApi.md#apis_get) | **GET** /apis | Retrieve/Search APIs 
*APIIndividualApi* | [**apis_api_id_get**](docs/APIIndividualApi.md#apis_api_id_get) | **GET** /apis/{apiId} | Get details of an API 
*APIIndividualApi* | [**apis_api_id_swagger_get**](docs/APIIndividualApi.md#apis_api_id_swagger_get) | **GET** /apis/{apiId}/swagger | Get swagger definition 
*APIIndividualApi* | [**apis_api_id_thumbnail_get**](docs/APIIndividualApi.md#apis_api_id_thumbnail_get) | **GET** /apis/{apiId}/thumbnail | Get thumbnail image
*APIIndividualApi* | [**apis_generate_sdk_post**](docs/APIIndividualApi.md#apis_generate_sdk_post) | **POST** /apis/generate-sdk/ | Generate SDK for an API 
*ApplicationCollectionApi* | [**applications_get**](docs/ApplicationCollectionApi.md#applications_get) | **GET** /applications | Retrieve/Search applications 
*ApplicationIndividualApi* | [**applications_application_id_delete**](docs/ApplicationIndividualApi.md#applications_application_id_delete) | **DELETE** /applications/{applicationId} | Remove an application 
*ApplicationIndividualApi* | [**applications_application_id_get**](docs/ApplicationIndividualApi.md#applications_application_id_get) | **GET** /applications/{applicationId} | Get details of an application 
*ApplicationIndividualApi* | [**applications_application_id_put**](docs/ApplicationIndividualApi.md#applications_application_id_put) | **PUT** /applications/{applicationId} | Update an application 
*ApplicationIndividualApi* | [**applications_generate_keys_post**](docs/ApplicationIndividualApi.md#applications_generate_keys_post) | **POST** /applications/generate-keys | Generate keys for application 
*ApplicationIndividualApi* | [**applications_post**](docs/ApplicationIndividualApi.md#applications_post) | **POST** /applications | Create a new application 
*DocumentCollectionApi* | [**apis_api_id_documents_get**](docs/DocumentCollectionApi.md#apis_api_id_documents_get) | **GET** /apis/{apiId}/documents | Get a list of documents of an API 
*DocumentIndividualApi* | [**apis_api_id_documents_document_id_content_get**](docs/DocumentIndividualApi.md#apis_api_id_documents_document_id_content_get) | **GET** /apis/{apiId}/documents/{documentId}/content | Get the content of an API document 
*DocumentIndividualApi* | [**apis_api_id_documents_document_id_get**](docs/DocumentIndividualApi.md#apis_api_id_documents_document_id_get) | **GET** /apis/{apiId}/documents/{documentId} | Get a document of an API 
*SubscriptionCollectionApi* | [**subscriptions_get**](docs/SubscriptionCollectionApi.md#subscriptions_get) | **GET** /subscriptions | Get all subscriptions 
*SubscriptionIndividualApi* | [**subscriptions_post**](docs/SubscriptionIndividualApi.md#subscriptions_post) | **POST** /subscriptions | Add a new subscription 
*SubscriptionIndividualApi* | [**subscriptions_subscription_id_delete**](docs/SubscriptionIndividualApi.md#subscriptions_subscription_id_delete) | **DELETE** /subscriptions/{subscriptionId} | Remove a subscription 
*SubscriptionIndividualApi* | [**subscriptions_subscription_id_get**](docs/SubscriptionIndividualApi.md#subscriptions_subscription_id_get) | **GET** /subscriptions/{subscriptionId} | Get details of a subscription 
*TagCollectionApi* | [**tags_get**](docs/TagCollectionApi.md#tags_get) | **GET** /tags | Get all tags 
*ThrottlingTierCollectionApi* | [**tiers_tier_level_get**](docs/ThrottlingTierCollectionApi.md#tiers_tier_level_get) | **GET** /tiers/{tierLevel} | Get available tiers 
*ThrottlingTierIndividualApi* | [**tiers_tier_level_tier_name_get**](docs/ThrottlingTierIndividualApi.md#tiers_tier_level_tier_name_get) | **GET** /tiers/{tierLevel}/{tierName} | Get details of a tier 


## Documentation For Models

 - [API](docs/API.md)
 - [APIInfo](docs/APIInfo.md)
 - [APIInfoObjectWithBasicAPIDetails_](docs/APIInfoObjectWithBasicAPIDetails_.md)
 - [APIList](docs/APIList.md)
 - [APIObject](docs/APIObject.md)
 - [APIObjectBusinessInformation](docs/APIObjectBusinessInformation.md)
 - [APIObjectEndpointURLs](docs/APIObjectEndpointURLs.md)
 - [APIObjectEnvironmentURLs](docs/APIObjectEnvironmentURLs.md)
 - [Application](docs/Application.md)
 - [Application1](docs/Application1.md)
 - [Application2](docs/Application2.md)
 - [Application3](docs/Application3.md)
 - [ApplicationInfo](docs/ApplicationInfo.md)
 - [ApplicationInfoObjectWithBasicApplicationDetails](docs/ApplicationInfoObjectWithBasicApplicationDetails.md)
 - [ApplicationKey](docs/ApplicationKey.md)
 - [ApplicationKeyDetails](docs/ApplicationKeyDetails.md)
 - [ApplicationKeyGenerateRequest](docs/ApplicationKeyGenerateRequest.md)
 - [ApplicationKeyGenerationRequestObject](docs/ApplicationKeyGenerationRequestObject.md)
 - [ApplicationList](docs/ApplicationList.md)
 - [DescriptionOfIndividualErrorsThatMayHaveOccurredDuringARequest_](docs/DescriptionOfIndividualErrorsThatMayHaveOccurredDuringARequest_.md)
 - [Document](docs/Document.md)
 - [Document1](docs/Document1.md)
 - [DocumentList](docs/DocumentList.md)
 - [Error](docs/Error.md)
 - [ErrorListItem](docs/ErrorListItem.md)
 - [ErrorObjectReturnedWith4XXHTTPStatus](docs/ErrorObjectReturnedWith4XXHTTPStatus.md)
 - [Subscription](docs/Subscription.md)
 - [Subscription1](docs/Subscription1.md)
 - [Subscription2](docs/Subscription2.md)
 - [SubscriptionList](docs/SubscriptionList.md)
 - [Tag](docs/Tag.md)
 - [Tag1](docs/Tag1.md)
 - [TagList](docs/TagList.md)
 - [Tier](docs/Tier.md)
 - [Tier1](docs/Tier1.md)
 - [TierList](docs/TierList.md)
 - [Token](docs/Token.md)
 - [TokenDetailsForInvokingAPIs](docs/TokenDetailsForInvokingAPIs.md)


## Documentation For Authorization


## OAuth2

- **Type**: OAuth
- **Flow**: password
- **Token URL**: https://apis.wso2.com/oauth2/token
- **Scopes**: 
 - **apim:subscribe**: apim:subscribe


## Author

architecture@wso2.com

