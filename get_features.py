import numpy as np
import scipy.io.wavfile
import pywt
from scipy.fftpack import dct

import data
from utils.feature_utils import *

NFFT = 512

path_whole_data = "data/validator.csv"

def get_frames(sample_rate, signal):
	alpha = 0.97
	emphasized_signal = np.append(signal[0], signal[1:] - alpha * signal[:-1])

	frame_size = 0.025
	frame_stride = 0.01

	frame_length, frame_step = frame_size * sample_rate, frame_stride * sample_rate  # Convert from seconds to samples
	signal_length = len(emphasized_signal)
	frame_length = int(round(frame_length))
	frame_step = int(round(frame_step))
	num_frames = int(np.ceil(float(np.abs(signal_length - frame_length)) / frame_step))  # Make sure that we have at least 1 frame

	pad_signal_length = num_frames * frame_step + frame_length
	z = np.zeros((pad_signal_length - signal_length))
	pad_signal = np.append(emphasized_signal, z) # Pad Signal to make sure that all frames have equal number of samples without truncating any samples from the original signal

	indices = np.tile(np.arange(0, frame_length), (num_frames, 1)) + np.tile(np.arange(0, num_frames * frame_step, frame_step), (frame_length, 1)).T
	frames = pad_signal[indices.astype(np.int32, copy=False)]
	frames *= np.hamming(frame_length)

	return frames

def power_spectrum_fft(sample_rate, signal): #gives fft power spectrum
	frames = get_frames(sample_rate, signal)
	mag_frames = np.absolute(np.fft.rfft(frames, NFFT))  # Magnitude of the FFT
	pow_frames = ((1.0 / NFFT) * ((mag_frames) ** 2)) #power spectrum
	return pow_frames

def power_spectrum_wavelet(sample_rate, signal): #gives wavelet power spectrum (I hope!)
	frames = get_frames(sample_rate, signal)
	(x, y) = pywt.dwt(frames, 'haar')
	return np.append(x, y)

def get_spectrums(file): #give both spectrums given a file
	sample_rate, signal = scipy.io.wavfile.read(file)
	return (power_spectrum_fft(sample_rate, signal), power_spectrum_wavelet(sample_rate, signal))

#MAX_FFT_SIZE
#MAX_WAVELET_SIZE

def get_sizes():
	_, df = data.combine_all_wavs_and_trans_from_csvs(path_whole_data)

	indices = [ i for i in range(len(df)) ]
	path_audio, transcript = load_audio(df, indices)

	max_len_fft = 0
	max_len_wavelet = 0

	for path in path_audio:
		print('Calculating spectrums of', path)
		fft, wavelet = get_spectrums(path)

		print('Done with', path)

		max_len_fft = max(max_len_fft, len(fft))
		max_len_wavelet = max(max_len_wavelet, len(wavelet))

	# return (max_len_fft, max_len_wavelet)

if __name__ == '__main__':
	x, y = get_sizes()
	print('fft max size', x, 'wavelet max size', y)