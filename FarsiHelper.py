import arabic_reshaper
from bidi.algorithm import get_display
def CorrectFarsi(txt):
 reshaped_text = arabic_reshaper.reshape(u'%s' %str(txt))
 bidi_text = get_display(reshaped_text)
 return bidi_text