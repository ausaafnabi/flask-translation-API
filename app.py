import os
from flask import Flask,requests,jsonify
from models.translate import Translator
from config import *

app = Flask(__name__)

translator = Translator(MODEL_PATH)

app.config["DEBUG"] = True # turn off when in production

@app.route('/health', method=["GET"])
def health_check():
    '''Confirms service is running'''
    return "Machine translation Service is up and running...."

@app.route('/lang_routes', methods=["GET"])
def get_lang_route():
    lang = requests.args['lang']
    all_lang = translator.get_supported_langs()
    lang_routes = [la for la in all_langs if la[0]=lang]
    return jsonify({"output":lang_routes})

@app.route('/supported_languages',method=["GET"])
def get_supported_languages():
    langs = translator.get_supported_langs()
    return jsonify({"output":langs})

@app.route('/translate',method=["POST"])
def get_prediction():
    source = requests.json['source']
    target = requests.json['target']
    translation = translator.translate(source,target,text)
    return jsonify({"output":translation})

app.run(host="0.0.0.0")

