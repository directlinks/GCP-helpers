import tokenlib
from time import time

SECRET= 'DEACTIVATE'
TOKEN_EXPIRATION = time() + 86400 # valid for next 24 hours

DATA = {'instance_name': 'test', 'expires': TOKEN_EXPIRATION}

#
# Create Token
#
token = tokenlib.make_token(DATA, secret=SECRET)
print (token)

#
# Decode Data
#
manager = tokenlib.TokenManager(secret=SECRET)
data = manager.parse_token(token)

print(data)




