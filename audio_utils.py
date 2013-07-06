import numpy as np
import scipy

def stft(input_data, sample_rate, window_size, hop_size):
    window = scipy.hamming(window_size)
    output = scipy.array([scipy.fft(window*input_data[i:i+window_size]) 
                         for i in range(0, len(input_data)-window_size, hop_size)])
    return output

def istft(input_data, sample_rate, window_size, hop_size, total_time):
    output = scipy.zeros(total_time*sample_rate)
    for n,i in enumerate(range(0, len(output)-window_size, hop_size)):
        output[i:i+window_size] += scipy.real(scipy.ifft(input_data[n]))
    return output

def low_pass_filter(max_freq, window_size, fft_bin_size):
    max_freq_bin = max_freq / fft_bin_size
    filter_block = np.ones(window_size)
    filter_block[max_freq_bin:(window_size-max_freq_bin)] = 0
    return filter_block

def high_pass_filter(min_freq, window_size, fft_bin_size):
    return np.ones(window_size) - low_pass_filter(min_freq, window_size, fft_bin_size)

