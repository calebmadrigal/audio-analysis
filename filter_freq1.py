import sys
import numpy
import scikits.audiolab as audio
import matplotlib.pyplot as plt
import random

def frequencyFilter(signal):
   starting_freq = 6000
   for i in range(starting_freq, len(signal)-starting_freq):
      signal[i] = 0

def processWithNumpy(signal):
   transformedSignal = numpy.fft.fft(signal)
   frequencyFilter(transformedSignal)

   cleanedSignal = numpy.fft.ifft(transformedSignal)
   return numpy.array(cleanedSignal, dtype=numpy.float64)

# Must be wav files.
infile = sys.argv[1]
outfile = sys.argv[2]

(inputSignal, samplingRate, bits) = audio.wavread(infile)
outputSignal = processWithNumpy(inputSignal)

outputFile = audio.Sndfile(outfile, 'w', audio.Format('wav'), 1, samplingRate)
outputFile.write_frames(outputSignal)
outputFile.close()
