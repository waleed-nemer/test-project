from googletrans import Translator
translator = Translator()
print(translator.translate("مرحبا", dest="ko").text)
print(translator.translate("مرحبا", dest="ar").text)
print(translator.translate("مرحبا", dest="ja").text)
print(translator.translate("مرحبا", dest="it").text)
print(translator.translate("مرحبا", dest="ru").text)
print(translator.translate("مرحبا", dest="ur").text)






