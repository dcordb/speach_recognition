import argparse

def main(args):
	print(args.feature_type)

if __name__ == '__main__':
	parser = argparse.ArgumentParser()

	parser.add_argument('--feature_type', type=str, default='mfcc',
						help='Feature extraction method: mfcc, spectrogram, fft (fourier power spectrum) or wavelet (wavelet power spectrum).')

	args = parser.parse_args()
	main(args)