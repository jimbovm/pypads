# SPDX-License-Identifier: MIT-0

# Copyright 2025 James Brierley.

# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the “Software”), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to do
# so.

# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from math import tau
from random import random

import numpy as np
import scipy as sp

from utils import profile

def padsynth(
		harmonics: int,
		amplitudes: list,
		wavetable_size: int,
		bandwidth: int,
		fundamental_hz: int,
		sample_rate: int
):
	'''Implement the PADsynth algorithm by Nasca Octavian Paul (https://zynaddsubfx.sourceforge.io/doc/PADsynth/PADsynth.htm).

	See args.py for defaults passed in this program.

	Arguments:
	harmonics -- the number of harmonics (overtones) in the generated sound
	amplitudes -- amplitude of each harmonic (length <= harmonics, 0.0 assumed for harmonics not given)
	wavetable_size -- the length (in samples) of the generated sound
	bandwidth -- the bandwidth of a harmonic (overtone) in cents
	fundamental_hz -- the fundamental frequency, e.g. 440 for A4
	sample_rate -- the number of samples per second in the generated sound
	'''
	freq_amplitude = sp.zeros(wavetable_size // 2 - 1)
	freq_phase = sp.array([random() * tau for i in range(wavetable_size // 2 - 1)])

	for harmonic in range(1, harmonics):
		if amplitudes[harmonic] != 0:
			bandwidth_hz = (pow(2, bandwidth / 1200) - 1.0) * fundamental_hz * harmonic
			this_bandwidth = bandwidth_hz / (2.0 * sample_rate)
			this_frequency = (fundamental_hz * harmonic) / sample_rate

			for i in range(0, (wavetable_size // 2 - 1)):
				harmonic_profile = profile((i / wavetable_size) - this_frequency, this_bandwidth)
				freq_amplitude[i] = freq_amplitude[i] + harmonic_profile * amplitudes[harmonic]

	wavetable = sp.empty(len(freq_amplitude), dtype=complex)
	wavetable.real = sp.array(freq_amplitude) * sp.cos(freq_phase)
	wavetable.imag = sp.array(freq_amplitude) * sp.sin(freq_phase)

	sample = sp.fft.irfft(wavetable)
	pcm = sp.int16(sample / np.max(np.abs(sample)) * 32767)
	return pcm