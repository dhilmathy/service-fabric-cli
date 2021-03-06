# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .retention_policy_description_py3 import RetentionPolicyDescription


class BasicRetentionPolicyDescription(RetentionPolicyDescription):
    """Describes basic retention policy.

    All required parameters must be populated in order to send to Azure.

    :param retention_policy_type: Required. Constant filled by server.
    :type retention_policy_type: str
    :param retention_duration: Required. It is the minimum duration for which
     a backup created, will remain stored in the storage and might get deleted
     after that span of time. It should be specified in ISO8601 format.
    :type retention_duration: timedelta
    :param minimum_number_of_backups: It is the minimum number of backups to
     be retained at any point of time. If specified with a non zero value,
     backups will not be deleted even if the backups have gone past retention
     duration and have number of backups less than or equal to it.
    :type minimum_number_of_backups: int
    """

    _validation = {
        'retention_policy_type': {'required': True},
        'retention_duration': {'required': True},
        'minimum_number_of_backups': {'minimum': 0},
    }

    _attribute_map = {
        'retention_policy_type': {'key': 'RetentionPolicyType', 'type': 'str'},
        'retention_duration': {'key': 'RetentionDuration', 'type': 'duration'},
        'minimum_number_of_backups': {'key': 'MinimumNumberOfBackups', 'type': 'int'},
    }

    def __init__(self, *, retention_duration, minimum_number_of_backups: int=None, **kwargs) -> None:
        super(BasicRetentionPolicyDescription, self).__init__(**kwargs)
        self.retention_duration = retention_duration
        self.minimum_number_of_backups = minimum_number_of_backups
        self.retention_policy_type = 'Basic'
