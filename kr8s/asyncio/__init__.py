# SPDX-FileCopyrightText: Copyright (c) 2023-2025, Kr8s Developers (See LICENSE for list)
# SPDX-License-Identifier: BSD 3-Clause License
"""The `kr8s` asynchronous API.

This module provides an asynchronous API for interacting with a Kubernetes cluster.
"""
from kr8s._api import Api

from . import objects, portforward
from ._api import api
from ._helpers import api_resources, create, get, version, watch, whoami

__all__ = [
    "api",
    "api_resources",
    "create",
    "get",
    "objects",
    "portforward",
    "version",
    "watch",
    "whoami",
    "Api",
]
