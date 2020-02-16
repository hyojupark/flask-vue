import os

from flask import url_for, request

from src import app
from src.controller import base_controller

class Server(object):
    def __init__(self, host, port, debug, use_reloader, threaded):
        self.host = host
        self.port = int(os.environ.get("PORT", port))
        self.debug = debug
        self.use_reloader = use_reloader
        self.threaded = threaded

    @staticmethod
    def register_views() -> None:
      # Business logic
      base_controller.BaseView.register(app, route_base='/')

      # Resources
      pass

    @staticmethod
    def url_for_other_page(page):
        args = request.view_args.copy()
        args['page'] = page
        return url_for(request.endpoint, **args)

    def run(self) -> bool:
        self.register_views()

        app.jinja_env.globals['url_for_other_page'] = self.url_for_other_page
        app.run(host=self.host, port=self.port, debug=self.debug,
                use_reloader=self.use_reloader, threaded=self.threaded)

        return True

if __name__ == '__main__':
    server = Server(host='0.0.0.0', port=5010, debug=True, use_reloader=False, threaded=True)
    server.run()
