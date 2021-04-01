import tokenlib
SECRET= 'DEACTIVATE'
token= 'eyJ1c2VyaWQiOiA0MiwgImV4cGlyZXMiOiAxNjE3MjkwNDE0LjA4OTU1MzYsICJzYWx0IjogIjFjMDMzZiJ9fhvlzCxhbGVcpcVXDBx6QkGZxyiVhN9qSCYTf15bWvI='

try:
    tokenlib.parse_token(token, secret=SECRET)
except Exception as e:
    print('token expired: ',e)