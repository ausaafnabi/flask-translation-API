import os
from flask import Flask,request,jsonify,render_template
from model.translator import Translator 
from config import *
SUPPORTED_LANGUAGES = [ 
        'English',
        'Hindi',
        'Japanese',
        'Chinese',
        'German',
        'French',
        'Arabic',
        'Persian',
        'Hebrew',
        'Greek',
        'Russian',
        'Spanish',
        'Italian',
        'Tamil',
        'Kannada',
]
app = Flask(__name__)

translator = Translator(MODEL_PATH)

app.config["DEBUG"] = True # turn off when in production

@app.route('/',methods=["GET","POST"])
def translateApp():
    if request.method=='GET':
        return render_template('index.html',supp_langs=SUPPORTED_LANGUAGES)

@app.route('/v1/health', methods=["GET"])
def health_check():
    '''Confirms service is running'''
    return "Machine translation Service is up and running...."

@app.route('/v1/lang_routes', methods=["GET"])
def get_lang_route():
    lang = requests.args['lang']
    all_lang = translator.get_supported_langs()
    lang_routes = [la for la in all_langs if la[0]==lang]
    return jsonify({"output":lang_routes})

@app.route('/v1/supported_languages',methods=["GET"])
def get_supported_languages():
    langs = translator.get_supported_langs()
    return jsonify({"output":langs})

@app.route('/v0/supported_langs',methods=['GET'])
def supp_langs():
    return jsonify({"output":SUPPORTED_LANGUAGES})

@app.route('/v1/translate',methods=["POST"])
def get_prediction():
    source = request.json['source']
    target = request.json['target']
    text = request.json['text']
    translation = translator.translate(source,target,text)
    return jsonify({"output":translation})

app.run(host="0.0.0.0")

