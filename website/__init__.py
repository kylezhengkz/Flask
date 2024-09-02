from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ndfknslj vskjvf kfvj dsknkv kfknv jsdvks'
    
    return app