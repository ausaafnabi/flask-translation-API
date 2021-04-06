# LANGUAGE TRANSLATOR API

This is the language translation API based on transformers and MarianMT model for language translation (huggingface.co). This provides easy pretrained Language models that can be used to do machine translation in any 2 desired languages.
There is one webpage as well that works on MyMemory API to provide translation that can also store recent translations.  

## Technologies used
* **[Python3](https://www.python.org/downloads/)** - A programming language that lets you work more quickly (The universe loves speed!).
* **[Flask](flask.pocoo.org/)** - A microframework for Python based on Werkzeug, Jinja 2 and good intentions
* **[Virtualenv](https://virtualenv.pypa.io/en/stable/)** - A tool to create isolated virtual environments

## API 
There are 2 versions of the  REST API
version 0 that exposes only supported language and other as webapp
version 1 that exposes 4 endpoints to the internet.

**V0 API CONTRACTS**

```txt
GET /
GET v0/supported_langs
```
**V1 API CONTRACTS**
```txt
GET v1/health
GET v1/lang_routes
GET v1/supported_languages
POST v1/translate
```
**Inputs**

'source' : Source Language 

'target' : Target Language

'text' : Text to be transferred

**OUTPUTS**

'translation' : Translated Text

'supported languages' : Languages Supported 

'language routes' : routes to languages


## TODO:
- [ ] Add swagger Doc
- [ ] API call to download more translators

## Installation / Usage
* If you wish to run your own build, first ensure you have python3 globally installed in your computer.

* After this, ensure you have installed virtualenv globally as well. If not, run this:
    ```
        $ pip install virtualenv
    ```
* Git clone this repo to your PC
    ```
        $ git clone git@github.com:ausaafnabi/flask-translaton-API.git
    ```


* #### Dependencies
    1. Cd into your the cloned repo as such:
        ```
        $ cd flask-translation-API
        ```

    2. Create and fire up your virtual environment in python3:
        ```
        $ virtualenv -p python3 venv
        $ pip install autoenv
        ```
* #### Install your requirements
    ```
    (venv)$ pip install -r Requirements.txt
    ```
* #### Running It
    On your terminal, run the server using this one simple command:
    ```
    (venv)$ flask run
    ```
    You can now access the app on your local browser by using
    ```
    http://localhost:5000/
    ```
    Or test using  Postman


# Contributions:
Feel free to Contribute to this repository

