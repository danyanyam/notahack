from vosk import Model, KaldiRecognizer, SpkModel
import numpy as np
import wave
import json
import sys
import re
import os



def find_person(array):
    database = np.array(list(users.values()))
    distances = []
    
    for i in database:
        distances.append(cosine_dist(array, i))
    min_dist = min(distances)
    
    if min_dist > 0.12:
        return 'UNKNOWN PERSON'
    
    key = distances.index(min_dist)
    return list(users.keys())[key]


def punctuation(text):
    text = re.sub(' а ', ', а ', text)
    text = re.sub(' но ', ', но ', text)
    text = re.sub(' что ', ', что ', text)
    text = re.sub(' чтобы ', ', чтобы ', text)
    text = re.sub(' например ', ', например,  ', text)
    text = re.sub(' да ', ', да  ', text)
    text = re.sub(' как ', ', как  ', text)
    text = re.sub(' зато ', ', зато  ', text)
    text = re.sub(' кроме того ', ', кроме того,  ', text)
    text = re.sub(' здравствуйте ', ' здравствуйте,  ', text)
    return text.capitalize() + '.'


persons = ['UNKNOWN_PERSON', 'timur', 'danya', 'anton']


def init_weights(persons):
    """ Функция присваивает каждому человеку вектор нулей"""
    users = {}
    for i in persons:
        users.update({i: np.zeros(128)})
    return users


def cosine_dist(x, y):
    nx = np.array(x)
    ny = np.array(y)
    return 1 - np.dot(nx, ny) / np.linalg.norm(nx) / np.linalg.norm(ny)
    
    
users = init_weights(persons)


# модель🙈, делающая разбиение речи на текст
model_path = "vosk-model-ru-0.10"
# модель 🙉, делающая разбиение текста на диалоги
spk_model_path = "vosk-model-spk-0.3"
# путь к войсу
PATH = 'ffmpeg_output.wav'


wf = wave.open(PATH, "rb")
model = Model(model_path)
spk_model = SpkModel(spk_model_path)
rec = KaldiRecognizer(model, spk_model, wf.getframerate())


with open('log.txt', 'w+') as f:
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            res = json.loads(rec.Result())
            f.write("{} : \n".format(find_person(res['spk'])) + punctuation(res['text']) + '\n\n')
