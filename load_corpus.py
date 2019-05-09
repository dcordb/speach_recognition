from scipy.io import wavfile
# import nltk
from nltk.corpus import PlaintextCorpusReader as pcr

corpus_dir = 'data'
wav_files = corpus_dir + '/wav48'

def read_corpus():
    my_corpus = pcr(corpus_dir, r'.*\.txt')

    for f_name in my_corpus.fileids():
        if 'txt/p' not in f_name:
            continue
        text = corpus_dir + '/' + f_name
        wav = wav_files + f_name[3:len(f_name)-4] + '.wav'
        yield text, wav


fs, data = wavfile.read('./output/audio.wav')
