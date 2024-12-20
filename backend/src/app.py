from flask import Flask
from config import config
from routes import Producto, Usuario
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

def page_not_found(error):
    return "<h1>Not found page</h1>", 404

if __name__ == '__main__':

    app.config.from_object(config['development'])

    app.register_error_handler(404, page_not_found)

    app.register_blueprint(Producto.main, url_prefix='/api/productos')

    app.register_blueprint(Usuario.main, url_prefix='/api/usuario')

    app.run()