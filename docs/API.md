# API

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | UUID of the api registry artifact  | [optional] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**context** | **str** |  | 
**version** | **str** |  | 
**provider** | **str** | If the provider value is not given user invoking the api will be used as the provider.  | 
**api_definition** | **str** | Swagger definition of the API which contains details about URI templates and scopes  | 
**wsdl_uri** | **str** | WSDL URL if the API is based on a WSDL endpoint  | [optional] 
**status** | **str** |  | 
**is_default_version** | **bool** |  | [optional] 
**transport** | **list[str]** |  | [optional] 
**tags** | **list[str]** |  | [optional] 
**tiers** | **list[str]** |  | [optional] 
**thumbnail_url** | **str** |  | [optional] 
**endpoint_ur_ls** | [**list[APIObjectEndpointURLs]**](APIObjectEndpointURLs.md) |  | [optional] 
**business_information** | [**APIObjectBusinessInformation**](APIObjectBusinessInformation.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


