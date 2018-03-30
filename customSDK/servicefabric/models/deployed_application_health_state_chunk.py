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

from .entity_health_state_chunk import EntityHealthStateChunk


class DeployedApplicationHealthStateChunk(EntityHealthStateChunk):
    """Represents the health state chunk of a deployed application, which contains
    the node where the application is deployed, the aggregated health state and
    any deployed service packages that respect the chunk query description
    filters.
    .

    :param health_state: The health state of a Service Fabric entity such as
     Cluster, Node, Application, Service, Partition, Replica etc. Possible
     values include: 'Invalid', 'Ok', 'Warning', 'Error', 'Unknown'
    :type health_state: str or ~azure.servicefabric.models.HealthState
    :param node_name: The name of node where the application is deployed.
    :type node_name: str
    :param deployed_service_package_health_state_chunks: The list of deployed
     service package health state chunks belonging to the deployed application
     that respect the filters in the cluster health chunk query description.
    :type deployed_service_package_health_state_chunks:
     ~azure.servicefabric.models.DeployedServicePackageHealthStateChunkList
    """

    _attribute_map = {
        'health_state': {'key': 'HealthState', 'type': 'str'},
        'node_name': {'key': 'NodeName', 'type': 'str'},
        'deployed_service_package_health_state_chunks': {'key': 'DeployedServicePackageHealthStateChunks', 'type': 'DeployedServicePackageHealthStateChunkList'},
    }

    def __init__(self, health_state=None, node_name=None, deployed_service_package_health_state_chunks=None):
        super(DeployedApplicationHealthStateChunk, self).__init__(health_state=health_state)
        self.node_name = node_name
        self.deployed_service_package_health_state_chunks = deployed_service_package_health_state_chunks
