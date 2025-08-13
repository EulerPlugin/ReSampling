# argument as an audio file, sampling rate

# a. check command-line arguments for validility

# b. perform the desired resampling

# c. store the result in a separate audio file next to the original file


import scipy
import scipy.signal

import argparse
import pathlib
import soundfile as sf

parser = argparse.ArgumentParser()

parser.add_argument("input", type = pathlib.Path)
parser.add_argument("SampleRate", type = int)

args = parser.parse_args()

if not args.input.exists():
    raise   FileNotFoundError(f"Input file Not found: {args.input}")

data, fs = sf.read(args.input)
resampled = scipy.signal.resample_poly(data, args.SampleRate, fs)

sf.write(
    args.input.with_name(args.input.stem + f"_{args.SampleRate}Hz" + args.input.suffix),
    resampled,
    args.SampleRate
)