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

import numpy as np
import scipy as sp
from sys import exit, stderr

from args import arg_parser, args
from padsynth import padsynth

if len(args['amplitudes']) > args['harmonics']:
	print(f'More amplitude values ({len(args['amplitudes'])}) given than harmonics ({args['harmonics']})', file=stderr)
	arg_parser.print_help()
	exit(1)

amplitudes = np.zeros(args['harmonics'], dtype=float)
amplitudes[0:len(args['amplitudes'])] = args['amplitudes']

sample = padsynth(
	args['harmonics'],
	amplitudes, # zero-padded up to args['harmonics']
	args['wavetable_size'],
	args['bandwidth'],
	args['fundamental_hz'],
	args['sample_rate']
)

sp.io.wavfile.write(args['output_file'], args['sample_rate'], sample)

exit(0)