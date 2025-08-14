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


<br>


**Validation Logic**

`if not args.input.excists():`



Raised a `FileNotFoundError` if the path does not exist

-> Satifies a minimum level of validity check


<br>

**2) `pathlib` - Handiling Paths and Filenames**

- `args.input.stem` -> filename without extension



