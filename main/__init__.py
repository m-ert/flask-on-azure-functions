import logging

from flask import Flask, redirect

import azure.functions as func

app = Flask(__name__)

#code for azure functions
def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    return func.WsgiMiddleware(app.wsgi_app).handle(req, context)

#code for flask app
@app.route("/")
def index():
    return "Hello World"

if __name__ == '__main__':
    app.run()
