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

from argparse import ArgumentParser, FileType
from sys import argv

arg_parser = ArgumentParser(
	prog='pypads',
	description='''
Generates ethereal synth pad samples using Nasca Octavian Paul\'s PADsynth algorithm.
''',
	epilog='This software is licensed under the MIT-0 licence (https://spdx.org/licenses/MIT-0.html).')

arg_parser.add_argument('output_file', type=FileType('wb'), help='File to which to output pad sample')
arg_parser.add_argument('--stereo', action='store_true', default=False, help='Generate a stereo WAV')
arg_parser.add_argument('--sample-rate', type=int, default=44100, help='Sample rate of generated WAV')
arg_parser.add_argument('--wavetable-size', type=int, default=262144, help='Length (in samples) of generated WAV')
arg_parser.add_argument('--fundamental-hz', type=int, default=440, help='Frequency of fundamental (e.g. 440 for A4)')
arg_parser.add_argument('--bandwidth', type=int, default=50, help='Bandwidth of the first harmonic in cents')
arg_parser.add_argument('--harmonics', type=int, default=32, help='Number of harmonics')
arg_parser.add_argument('--scale', type=float, default=1.0, help='Bandwidth scale with harmonic frequency')
arg_parser.add_argument('--amplitudes', required=True, type=float, nargs='+', help='Amplitude of each harmonic (zero assumed for harmonics not given)')

args = vars(arg_parser.parse_args(argv[1:]))