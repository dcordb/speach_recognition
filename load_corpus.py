from scipy.io import wavfile
from nltk.corpus import PlaintextCorpusReader as pcr
import csv
from random import shuffle

corpus_dir = '/media/daniel/31B9D577341E99F0/Programming/VCTK-Corpus/' #add correct dir address here!
wav_files = corpus_dir + '/wav48'


def gen_cvs():
    my_corpus = pcr(corpus_dir, r'.*\.txt')
    data = [[]]

    for f_name in my_corpus.fileids():
        if 'txt/p' not in f_name:
            continue
        wav = wav_files + f_name[3:len(f_name)-4] + '.wav'
        data.append([wav, my_corpus.raw(f_name)[0:len(my_corpus.raw(f_name)) - 1]])

    print('Processed', len(data), 'files')
    print('Shuffling data')

    shuffle(data) #suffle first the data
    data.insert(0, ['filename', 'transcript']) #add the headers

    print('Saving train.csv...')

    with open(corpus_dir + 'data/train.csv', 'w') as csv_train:
        writer = csv.writer(csv_train)
        writer.writerows([data[0]]+data[220:])

    csv_train.close()

    print('Done')
    print('Saving test.csv...')

    with open(corpus_dir + 'data/test.csv', 'w') as csv_test:
        writer = csv.writer(csv_test)
        writer.writerows(data[:220])

    csv_test.close()

    print('Done')


gen_cvs()