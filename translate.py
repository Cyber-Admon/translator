from googletrans import Translator

translator = Translator()

def translate_text(text, source_lang, target_lang):
    translated_text = translator.translate(text, src=source_lang, dest=target_lang)
    return translated_text.text

source_text = input("Enter the text to translate: ")
source_lang = input("Enter the source language (en, fr, es): ")
target_lang = input("Enter the target language (en, fr, ar, es, ja, ko): ")

translated_text = translate_text(source_text, source_lang, target_lang)

print("Translated text:", translated_text)
