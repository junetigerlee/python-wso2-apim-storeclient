# coding: utf-8

"""
    WSO2 API Manager - Store

    This specifies a **RESTful API** for WSO2 **API Manager** - Store.  Please see [full swagger definition](https://raw.githubusercontent.com/wso2/carbon-apimgt/v6.0.4/components/apimgt/org.wso2.carbon.apimgt.rest.api.store/src/main/resources/store-api.yaml) of the API which is written using [swagger 2.0](http://swagger.io/) specification. 

    OpenAPI spec version: 0.11.0
    Contact: architecture@wso2.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ErrorObjectReturnedWith4XXHTTPStatus(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'code': 'int',
        'message': 'str',
        'description': 'str',
        'more_info': 'str',
        'error': 'list[DescriptionOfIndividualErrorsThatMayHaveOccurredDuringARequest_]'
    }

    attribute_map = {
        'code': 'code',
        'message': 'message',
        'description': 'description',
        'more_info': 'moreInfo',
        'error': 'error'
    }

    def __init__(self, code=None, message=None, description=None, more_info=None, error=None):
        """
        ErrorObjectReturnedWith4XXHTTPStatus - a model defined in Swagger
        """

        self._code = None
        self._message = None
        self._description = None
        self._more_info = None
        self._error = None

        self.code = code
        self.message = message
        if description is not None:
          self.description = description
        if more_info is not None:
          self.more_info = more_info
        if error is not None:
          self.error = error

    @property
    def code(self):
        """
        Gets the code of this ErrorObjectReturnedWith4XXHTTPStatus.

        :return: The code of this ErrorObjectReturnedWith4XXHTTPStatus.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this ErrorObjectReturnedWith4XXHTTPStatus.

        :param code: The code of this ErrorObjectReturnedWith4XXHTTPStatus.
        :type: int
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")

        self._code = code

    @property
    def message(self):
        """
        Gets the message of this ErrorObjectReturnedWith4XXHTTPStatus.
        Error message.

        :return: The message of this ErrorObjectReturnedWith4XXHTTPStatus.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this ErrorObjectReturnedWith4XXHTTPStatus.
        Error message.

        :param message: The message of this ErrorObjectReturnedWith4XXHTTPStatus.
        :type: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")

        self._message = message

    @property
    def description(self):
        """
        Gets the description of this ErrorObjectReturnedWith4XXHTTPStatus.
        A detail description about the error message. 

        :return: The description of this ErrorObjectReturnedWith4XXHTTPStatus.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ErrorObjectReturnedWith4XXHTTPStatus.
        A detail description about the error message. 

        :param description: The description of this ErrorObjectReturnedWith4XXHTTPStatus.
        :type: str
        """

        self._description = description

    @property
    def more_info(self):
        """
        Gets the more_info of this ErrorObjectReturnedWith4XXHTTPStatus.
        Preferably an url with more details about the error. 

        :return: The more_info of this ErrorObjectReturnedWith4XXHTTPStatus.
        :rtype: str
        """
        return self._more_info

    @more_info.setter
    def more_info(self, more_info):
        """
        Sets the more_info of this ErrorObjectReturnedWith4XXHTTPStatus.
        Preferably an url with more details about the error. 

        :param more_info: The more_info of this ErrorObjectReturnedWith4XXHTTPStatus.
        :type: str
        """

        self._more_info = more_info

    @property
    def error(self):
        """
        Gets the error of this ErrorObjectReturnedWith4XXHTTPStatus.
        If there are more than one error list them out. For example, list out validation errors by each field. 

        :return: The error of this ErrorObjectReturnedWith4XXHTTPStatus.
        :rtype: list[DescriptionOfIndividualErrorsThatMayHaveOccurredDuringARequest_]
        """
        return self._error

    @error.setter
    def error(self, error):
        """
        Sets the error of this ErrorObjectReturnedWith4XXHTTPStatus.
        If there are more than one error list them out. For example, list out validation errors by each field. 

        :param error: The error of this ErrorObjectReturnedWith4XXHTTPStatus.
        :type: list[DescriptionOfIndividualErrorsThatMayHaveOccurredDuringARequest_]
        """

        self._error = error

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ErrorObjectReturnedWith4XXHTTPStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
