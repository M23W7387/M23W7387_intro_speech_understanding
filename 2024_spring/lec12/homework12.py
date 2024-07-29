import gtts

def synthesize(text, lang, filename):
    tts = gtts.gTTS(text, lang=lang)  # 変数名を正しいものに修正
    tts.save(filename)