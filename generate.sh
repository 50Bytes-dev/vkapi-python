#!/bin/bash
source .venv/bin/activate
openapi-python-client generate --custom-template-path=./templates --path ../vkapi/static/api/spec.yml --overwrite --meta uv --output-path generated
rm -rf ./vkapi_python
mv ./generated/vkapi_client ./vkapi_python
rm -rf ./generated
