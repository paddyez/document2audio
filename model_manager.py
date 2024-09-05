from TTS.api import TTS

def info_from_model_manager():
    """
    Function to print the list of all engines
    """
    model_manager = TTS().list_models()
    print(dir(model_manager))
    print("### tts_model")
    for tts_model in model_manager.list_tts_models():
        print(f"{tts_model}")
    print("### vc_model")
    for vc_model in model_manager.list_vc_models():
        print(f"{vc_model}")
    print("### vocoder_model")
    for vocoder_model in model_manager.list_vocoder_models():
        print(f"{vocoder_model}")
    print("### lang")
    langs = model_manager.list_langs()
    #help(langs)
    print(f"{langs}")
