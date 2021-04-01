from translate import Translator

def HTTPTranslate(textToTranslate,toLang,fromLang="English"):
    translator = Translator(from_lang=fromLang,to_lang=toLang)
    try:
        translation=translator.translate(textToTranslate)
        return translation
    except ConnectionError as conn_error:
        print("Could'nt connect to the server at the moment!")
        return 500
    except Exception as ex:
        print("Undefined Error")
        return 504


