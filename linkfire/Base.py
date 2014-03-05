import requests
import hashlib

class ApiMethod(object):
    """Basic API Class to handle API requests"""
    def __init__(self, api_version="1.0", host=None):
        super(ApiMethod, self).__init__()
        
        if not host:
            host = "http://linkfire.com/api/%s" % api_version

        self.email = ""
        self.password = ""
        
        self.token = None
        self.user_id = None

        self.host = host
        
    def call_api(endpoint, params,):
        """ Call the API """
        payload = dict()
        if self.token and self.user_id:
            payload.update({'token': self.token, 'user_id': self.user_id})
        payload.update(params)

        call_url = '{host}/{method}'.format(host=self.host, method=endpoint)

        r = requests.get(call_url, params=payload)
        data = r.json()

        self.call_response = data
        if data.has_key("errors"):
            raise Exception( "\n --- \n".join(data['errors']) ) 
   
        return data

    def authenticate(username, password, already_hashed_password=False):
        """
            This method with get from email and password the token and the 
            user_id.
        """
        if not already_hashed_password:
            hashed_password = hashlib.sha1(password).hexdigest()
        else:
            hashed_password = password

        payload = {"email": email, "password": hashed_password}
        data = self.call_api( "/auth/login", payload )

        self.token = data['token']
        self.user_id = data['user']['id']

        return data