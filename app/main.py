from flask import Flask

from app.api.handler import dummy_handler

def create_app():
    app = Flask("test_app")
    app.add_url_rule('/success', view_func=dummy_handler)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='127.0.0.1', port=5000)
