""" API handlers for dealing with pokemon """
import webapp2

from app.constants import API_USER_KEY_ASSOCIATIONS
from app.domain.pokemon import get_pokemon


class GetPokemonByNumberHandler(webapp2.RequestHandler):
    """ Get a specific pokemon's info by number """
    def get(self):
        """ get """
        self.check_credentials()
        number = self.request.get('number')
        if not number:
            self.abort(400, 'number is required')
        response = get_pokemon(number)
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(response)

    def check_credentials(self):
        """ Check that valid credentials were provided on the request """
        api_user = self.request.get('apiUser')
        if not api_user:
            self.abort(400, 'apiUser is required.')
        api_key = self.request.get('apiKey')
        if not api_key:
            self.abort(400, 'apiKey is required.')

        expected_key = API_USER_KEY_ASSOCIATIONS.get(api_user)
        if not expected_key or not expected_key == api_key:
            self.abort(401, 'Invalid apiUser/apiKey combination.')
