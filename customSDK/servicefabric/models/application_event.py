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

from .fabric_event import FabricEvent


class ApplicationEvent(FabricEvent):
    """Represents the base for all Application Events.

    :param event_instance_id: The identifier for the FabricEvent instance.
    :type event_instance_id: str
    :param time_stamp: The time event was logged.
    :type time_stamp: datetime
    :param has_correlated_events: Shows that there is existing related events
     available.
    :type has_correlated_events: bool
    :param kind: Constant filled by server.
    :type kind: str
    :param application_id: The identity of the application. This is an encoded
     representation of the application name. This is used in the REST APIs to
     identify the application resource.
     Starting in version 6.0, hierarchical names are delimited with the "\\~"
     character. For example, if the application name is "fabric:/myapp/app1",
     the application identity would be "myapp\\~app1" in 6.0+ and "myapp/app1"
     in previous versions.
    :type application_id: str
    """

    _validation = {
        'event_instance_id': {'required': True},
        'time_stamp': {'required': True},
        'kind': {'required': True},
        'application_id': {'required': True},
    }

    _attribute_map = {
        'event_instance_id': {'key': 'EventInstanceId', 'type': 'str'},
        'time_stamp': {'key': 'TimeStamp', 'type': 'iso-8601'},
        'has_correlated_events': {'key': 'HasCorrelatedEvents', 'type': 'bool'},
        'kind': {'key': 'Kind', 'type': 'str'},
        'application_id': {'key': 'ApplicationId', 'type': 'str'},
    }

    def __init__(self, event_instance_id, time_stamp, application_id, has_correlated_events=None):
        super(ApplicationEvent, self).__init__(event_instance_id=event_instance_id, time_stamp=time_stamp, has_correlated_events=has_correlated_events)
        self.application_id = application_id
        self.kind = 'ApplicationEvent'
