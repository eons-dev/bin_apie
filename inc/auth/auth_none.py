import os
import logging
import apie

# No Auth allows all requests.
# THIS IS EXTREMELY UNSAFE!
class none(apie.Authenticator):
    def __init__(this, name="No Authentication Authenticator"):
        super().__init__(name)

    # Yep!
    def UserFunction(this):
        if (this.request.authorization is None):
            logging.debug(f"Allowing request for {this.path} without authentication")
        else:
            logging.debug(f"Allowing request for {this.path} with authentication: {this.request.authorization}")
        return True