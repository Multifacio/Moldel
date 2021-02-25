from progress.bar import Bar
from typing import List
import csv
import os
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr
import timeout_decorator

BULK_SIZE = 100
TIMEOUT = 5 # The timeout for the speech recognition. After that it is recognized as an empty sentence.
SPEECH_STEP = 2/3 # The offset from which the speech is captured is increased by this step size every time in seconds.
SPEECH_LENGTH = 2 # The length of each captured speech part in seconds.
SOUND_FILE = "/home/haico/Dropbox/WIDM/Seizoen 22/Sound/Episode 3 - Amplified.wav"
TEXT_FILE = "/home/haico/Dropbox/WIDM/Seizoen 22/Speeches/Episode 3.csv"

@timeout_decorator.timeout(TIMEOUT)
def recognize_speech(audio: sr.AudioData) -> dict:
    while True:
        try:
            data = r.recognize_google(audio, language = "nl-NL", show_all = True)
            return data
        except:
            pass

def write_bulk(speeches: List[List[str]]):
    with open(TEXT_FILE, mode='a') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        for row in speeches:
            writer.writerow(row)

rate, sig = wav.read(SOUND_FILE)
duration = len(sig) / float(rate)
r = sr.Recognizer()
source = sr.AudioFile(SOUND_FILE)

if os.path.isfile(TEXT_FILE):
    with open(TEXT_FILE, newline='') as file:
        reader = csv.reader(file, delimiter=',', quotechar='"')
        skip_lines = len(list(reader))
else:
    skip_lines = 0

total_tasks = duration // SPEECH_STEP + 1 - skip_lines
progress_bar = Bar("Distributions Computed of First Model: ", max = total_tasks)
speeches = []
counter = 0
for offset in np.arange(skip_lines * SPEECH_STEP, duration, SPEECH_STEP):
    counter += 1
    with source as s:
        audio = r.record(s, offset = offset, duration = SPEECH_LENGTH)
        try:
            data = recognize_speech(audio)
        except TimeoutError:
            data = dict()

    if 'alternative' in data:
        data = data['alternative']
        speeches.append([d['transcript'] for d in data])
    else:
        speeches.append([])

    if counter % BULK_SIZE == 0:
        write_bulk(speeches)
        speeches = []
    progress_bar.next()

write_bulk(speeches)
progress_bar.finish()

