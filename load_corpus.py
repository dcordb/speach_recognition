from scipy.io import wavfile
# import nltk
from nltk.corpus import PlaintextCorpusReader as pcr
import csv

corpus_dir = 'data'
wav_files = corpus_dir + '/wav48'


def gen_cvs():
    my_corpus = pcr(corpus_dir, r'.*\.txt')
    data = [['filename', 'transcript']]
    for f_name in my_corpus.fileids():
        if 'txt/p' not in f_name:
            continue
        wav = wav_files + f_name[3:len(f_name)-4] + '.wav'
        data.append([wav, my_corpus.raw(f_name)[0:len(my_corpus.raw(f_name)) - 1]])

    with open('data/train.csv', 'w') as csv_train:
        writer = csv.writer(csv_train)
        writer.writerows(data[:220])

    csv_train.close()

    with open('data/test.csv', 'w') as csv_test:
        writer = csv.writer(csv_test)
        writer.writerows([data[0]]+data[220:])

    csv_test.close()


gen_cvs()

# fs, data = wavfile.read('./output/audio.wav')
