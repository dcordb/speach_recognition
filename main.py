import tensorflow as tf
import numpy as np


def get_wavelets(waves):
    return []


def get_t_fourier(speech):
    return []


def recognize(slices):
    return []


def get_waves(file=None):
    return []


def compare_solutions(fourier, wavelets, expected):
    return []


def implementation(speech, expected):
    waves = get_waves(speech)

    wavelets = recognize(get_wavelets(waves))
    fourier = recognize(get_t_fourier(waves))

    return compare_solutions(fourier, wavelets, expected)


examples = {
    'path_to_sound': ['expected', 'response'],
}


def test_cases():
    for key in examples.keys():
        implementation(key, examples.get(key))


def main():
    test_cases()


if __name__ == '__main__':
    main()
