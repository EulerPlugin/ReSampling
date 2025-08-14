# Python Audio Resampling CLI

This is a command line utility that resamples a given audio file to a target samplerate and saves the result as a new file alongside the original

Core Libraries : `argparse`, `pathlib`, `soundfile`, `scipy.signal`

**Quick Usage**
```
python Resampling.py input.wav 48000
```

<br>

-----

**Code**
```python
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

```

<br>

-----

### Design Requirements

**a) Argument Validation**

- Argument parsing with `argparse`, and file existence check with `pathlib.Path.exists()`

**b) Resampling Implement**

- Using `scipy.resample_poly`

**c) Saving Result**

- Creating a new file alongside the original using `soundfile.write`


<br>


-----

### Library Explanation

**1) `argparse` - Command line argument parsing**

`parser = argparse.ArgumentParser()` : Creates a parset object that defines descriptions, options, etc.

`parser.add_argument("input", type = pathlib.Path)` : Takes the firts positional argument as a file path. By specifying `type = Path`, it can be used directly as a Path object after parsing (prevents string-handling mistakes)

`parser.add_argument("SampleRate", type=int)` : Takes the second positional argument as the target sample rate (integer)

`args = parser.parse_args()` : Actually parses the CLI arguments and binds them to the `args` namespace

Validation Logic :

`if not args.input.excists():`



Raised a `FileNotFoundError` if the path does not exist

-> Satifies a minimum level of validity check


<br>

**2) `pathlib` - Handiling Paths and Filenames**

- `args.input.stem` -> filename without extension

- `args.input.suffix` -> extension (e.g., `.wav`)

- `with_name(newname)` -> creates a new Path in the same directory but with a different filename

In this script, the output filename is created in the format

`"{stem}_{SampleRate}Hz{suffix}"`, and saved in the same folder as the original


<br>

**3) soundfile (pysoundfile) - Reading/Writind I/O**

- `data, fs = sf.read(args.input)`

Return values:

1) `data` (Numpy array)

2) `fs` (interger sample rate)

<br>


- `sf.write(path, data, samplerate)`

: saves the audio data to file.

Why specify the sample rate again? Even though `fs` was obtained when reading the file, the new file's header metadata need to specify the sample rate of this file. In other words, even if `resample_poly` has already changed the array, you must explicitly set the sample rate so it is written correctly in the file format.


<br>


**4) scipy.signal.resample_poly - Polyphase Resampling**

- `resmaple_poly(x, up, down, axis = 0, window = ('kaiser', 5.0))`

: `up` (upsampling factor) and `down` (downsamppling factor) must be integers.

In this code : `up = args.SampleRate`, `down = fs` directly (e.g., `48000/44100`)



