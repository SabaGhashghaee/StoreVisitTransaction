class Service:
    def __init__(self, app):
        # Validate
        self.initial_services(app)
        # register services

    def initial_services(self, app):
        pass

    def request_validation(self):
        # validate request base on sender and ...
        pass


class GeneralService(Service):

    def initial_services(self, app):
        @app.route("/")
        def about():
            return "this is an exercise by Saba Ghashghaee. Enjoy it :) "
