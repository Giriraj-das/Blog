#!/bin/bash

set -e
alembic upgrade head || alembic upgrade head
exec "$@"