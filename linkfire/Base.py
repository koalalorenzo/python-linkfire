import requests
import hashlib

class ApiMethod(object):
    """Basic API Class to handle API requests"""

    email = ""
    password = ""
    host = None
    
    token = None
    user_id = None
    domain_id = ""
    team_id = ""
    
    def __init__(self, api_version="1.0", host=None):
        super(ApiMethod, self).__init__()        
        if not host:
            host = "http://linkfire.com/api/%s" % api_version
        self.host = host
        
    def call_api(self, endpoint, params):
        """ Call an API endpoint with auth credentials """
        payload = dict()

        # Credentials:
        if self.token:
            payload.update({'token': self.token})

        if self.user_id:
            payload.update({'user_id': self.user_id})

        if self.domain_id:
            payload.update({'domain_id': self.domain_id})

        if self.team_id:
            payload.update({'team_id': self.team_id})

        payload.update(params)

        call_url = '{host}/{method}'.format(host=self.host, method=endpoint)

        r = requests.get(call_url, params=payload)
        data = r.json()

        self.call_response = data
        if data.has_key("errors"):
            raise Exception( "\n --- \n".join(data['errors']) ) 
   
        return data

    def authenticate(self, email, password, already_hashed_password=False):
        """
            This method with get from email and password the token and the 
            user_id.
        """
        if not already_hashed_password:
            hashed_password = hashlib.sha1(password).hexdigest()
        else:
            hashed_password = password

        payload = {"email": email, "password": hashed_password}
        data = self.call_api( "auth/login", payload )

        self.token = data['token']
        self.user_id = data['user']['id']

        return data