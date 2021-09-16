import speech_recognition as sr
import ffmpy, urllib, pydub

def solve_recaptcha():


    frame_select('recaptcha-audio-button')
    frame_select('PLAY')

    audio_path_mp3 = os.path.join('sample.mp3')
    audio_path_wav = os.path.join('sample.wav')

    frame_select('audio-source','attrib','src')
    print('[INFO] Audio src:',src)
    urllib.request.urlretrieve(src,audio_path_mp3)

    sound = pydub.AudioSegment.from_mp3(audio_path_mp3)
    sound.export(audio_path_wav,format='wav')
    sample_audio = sr.AudioFile(audio_path_wav)
    print('[+] Audio Saved')

    r = sr.Recognizer()
    with sample_audio as source:
        audio = r.record(source)
    key = r.recognize_google(audio)
    print('[INFO] Recaptcha Passcode:',key)

    frame_select('audio-response','key',key)
    frame_select('recaptcha-verify-button')
    print('[+] Passcode Sent')
