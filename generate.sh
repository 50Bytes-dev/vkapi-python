#!/bin/bash
source .venv/bin/activate
openapi-python-client generate --path ../vkapi/static/api/spec.yml --overwrite --meta uv --output-path generated
rm -rf ./vkapi_python
mv ./generated/vkapi_client ./vkapi_python
rm -rf ./generated
