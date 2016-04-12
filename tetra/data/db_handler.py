"""
Copyright 2016 Rackspace

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import logging

from tetra.data.postgres_client import PostgresClient

LOG = logging.getLogger(__name__)

_db_handler = PostgresClient()

try:
    _db_handler.connect()
except Exception as e:
    LOG.error("Problem connecting to database: {0}".format(e))


def get_handler():
    return _db_handler