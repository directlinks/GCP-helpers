# Script to validate a token and stop the instance

Script `validate-token-and-shutdown-script.py` validates the expiration of the token present in the metadata and if the token is invalid it simply turn off the instance.

## Generate Token

>Location- ./utils/generate-token.py

## Useful links
1. [Client-Library Guide](https://cloud.google.com/compute/docs/tutorials/python-guide)
2. [Compute Engine API Docs](https://cloud.google.com/compute/docs/reference/rest/v1)
3. [API client Github](https://github.com/googleapis/google-api-python-client)