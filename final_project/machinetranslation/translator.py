from deep_translator import MyMemoryTranslator

"""
Creates a Language Translator Service between French and English.
"""

def english_to_french(english_text):
    """
        Receives a text in English and returns its French translation.
    """
    french_translation = MyMemoryTranslator(source='en', target='french').translate(english_text)
    return french_translation

def french_to_english(french_text):
    """
        Receives a text in French and returns its English translation.
    """
    english_translation = MyMemoryTranslator(source='french', target='en').translate(french_text)
    return english_translation
