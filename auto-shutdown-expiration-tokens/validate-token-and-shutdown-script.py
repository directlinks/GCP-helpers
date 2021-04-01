from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
import tokenlib

SECRET= 'DEACTIVATE'

def validate_token(token):
    """
    Checks if the hash is valid or expired
        
        Parameters:
            token: hash value of the token
        returns:
            Bool value
    """
    
    try:
        tokenlib.parse_token(token, secret=SECRET)
        return True
    except Exception as e:
        print('TOKEN_EXCEPTION: ',e)
        return False

def decode_hash(token, name):
    """
    Checks if the hash belongs to the correct instance or not
        
        Parameters:
            token: hash value of the token
            name: name of the instance
        returns:
            Bool value
    """
    manager = tokenlib.TokenManager(secret=SECRET)
    data = manager.parse_token(token)
    if name == data['instance_name']:
        return True
    else:
        return False

def stop_instance():
    """
    Stops the instance with invalid hash or expired hash
        returns:
            Text value
    """

    credentials = GoogleCredentials.get_application_default()
    service = discovery.build('compute', 'v1', credentials=credentials)
    project = 'PROJECT' # ADD PROJECT
    zones=['asia-east1-a', 'asia-east1-b', 'asia-east1-c', 'asia-east2-a', 'asia-east2-b', 'asia-east2-c', 'asia-northeast1-a', 'asia-northeast1-b', 'asia-northeast1-c', 'asia-northeast2-a', 'asia-northeast2-b', 'asia-northeast2-c', 'asia-northeast3-a', 'asia-northeast3-b', 'asia-northeast3-c', 'asia-south1-a', 'asia-south1-b', 'asia-south1-c', 'asia-southeast1-a', 'asia-southeast1-b', 'asia-southeast1-c', 'asia-southeast2-a', 'asia-southeast2-b', 'asia-southeast2-c', 'australia-southeast1-a', 'australia-southeast1-b', 'australia-southeast1-c', 'europe-north1-a', 'europe-north1-b', 'europe-north1-c', 'urope-west1-a', 'urope-west1-b', 'urope-west1-c', 'europe-west2-a', 'europe-west2-b', 'europe-west2-c', 'europe-west3-a', 'europe-west3-b', 'europe-west3-c', 'europe-west4-a', 'europe-west4-b', 'europe-west4-c', 'europe-west6-a', 'europe-west6-b', 'europe-west6-c', 'northamerica-northeast1-a', 'northamerica-northeast1-b', 'northamerica-northeast1-c', 'southamerica-east1-a', 'southamerica-east1-b', 'southamerica-east1-c', 'us-central1-f','us-central1-a', 'us-central1-b', 'us-central1-c', 'us-east1-a', 'us-east1-b', 'us-east1-c', 'us-east4-a', 'us-east4-b', 'us-east4-c', 'us-west1-a', 'us-west1-b', 'us-west1-c', 'us-west2-a', 'us-west2-b', 'us-west2-c', 'us-west3-a', 'us-west3-b', 'us-west3-c', 'us-west4-a', 'us-west4-b', 'us-west4-c']  

    for zone in zones:
        try:
            request = service.instances().list(project=project,zone=zone)
            response = request.execute()
            # print(response)
            for each in response['items']:
                validity = False
                for i in each['metadata']['items']:
                    
                    if i['key']=='hash-value':
                        #
                        # decode hash value to verify instance name signature
                        #
                        signature = decode_hash(i['value'], each['name'])
                        if signature == True:
                            validity = validate_token(i['value'])
                    
                    if validity==False:
                        request = service.instances().stop(project=project, zone=zone, instance=each['name'])
                        response = request.execute()
                        print(response)
        except Exception as e:
            print('Exception: ',e)
    return f'stopped instance'

stop_instance()