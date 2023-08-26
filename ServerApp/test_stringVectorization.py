import requests
import json


with open("./env.json") as f:
    CONFIG = json.load(f)

SERVER_IP = "http://{0}:{1}".format(CONFIG['server_ip'],CONFIG['port'])
auth_url = SERVER_IP+"/token"
vectorization_url = SERVER_IP+"/vectorize"


class TestClass:
    """
        test cases for testing the various possible scenarios
    """
 
    def test_server_status(self):
        """
           first and foremost thing is to check whether the required backed server is up or not ?
           status : 200 -> indicates server is up and running 
        """
        response = requests.get(SERVER_IP)
        assert response.status_code == 200



    def test_unauthorized_access(self):
        """
            Invalid or Unauthorized user trying to get Oath2 Authentication Token
            Status : 400 indicates either user is not a valid user / username or password is not correct
        """
        response = requests.post(
            auth_url,
            data={'username':'dummy','password':'fraud'},
        )
        assert response.status_code == 400



    def test_authorized_access(self):
        """
            Authorized user trying to get Oath2 Authentication Token
            status : 200 indicates a valid customer trying to establish a session
        """
        response = requests.post(
            auth_url,
            data={'username': CONFIG['username'], 'password': CONFIG['password']},
        )
        assert response.status_code == 200



    def test_unauthorized_api_access(self):
        """
            An unauthorized user trying to access vectorization API
            status : 401 -> if any unauthenticated user tries to access the /vectorization API (unsecured access to APIs)
        """
        response = requests.get(
            vectorization_url ,
            params = {
                'user_input' : 'String in this input does not matter, because user in not authorized to access'
            }
        )
        assert response.status_code == 401



    def test_input_validation(self):
        """
        Test whether input string is a valid string for vectorization.
        A valid string is one with minimum 25 characters.
        status : 422 -> unprocessable input, which means input is not a valid input and doesn't satisfies the required validations
        """
        response = requests.get(
            vectorization_url ,
            params = {
                'user_input' : '422 error should come'
            },
            headers = {"Authorization": "Bearer {0}".format(TestClass.get_access_token())}
        )
        assert response.status_code == 422



    def get_access_token():
        """
            Get Access token to be appended for valid request
        """
        response = requests.post(
            auth_url,
            data={'username': CONFIG['username'],'password': CONFIG['password']},
        )
        return json.loads(response.text)['access_token']
    
    

    def test_authorized_api_access(self):
        """
            An authorized user trying to access vectorization API
            status : 200 -> A valid authenticated user trying to access the vectorization api to get 500 vector representation of input string > 25 characters.
        """
        access_token = TestClass.get_access_token()

        response = requests.get(
            vectorization_url,
            params = {
                'user_input': "Generate 500 dimensional vector representation of input string."
            },
            headers = {"Authorization": "Bearer {0}".format(access_token)}
        )

        data = json.loads(response.text)
        
        assert response.status_code == 200
        assert len(data['vector_representation']) == 500