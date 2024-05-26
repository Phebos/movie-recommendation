from modeltranslation.translator import translator, TranslationOptions
from .models import Film

class FilmTranslationOptions(TranslationOptions):
    fields = ('plot',)

translator.register(Film, FilmTranslationOptions)