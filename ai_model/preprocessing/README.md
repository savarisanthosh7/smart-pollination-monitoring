# Audio Preprocessing

`preprocessing.py` converts raw audio recordings into fixed-size model inputs.

## Implemented operations

1. Load supported audio as mono.
2. Resample to **16 kHz**.
3. Normalize amplitude.
4. Calculate an STFT magnitude/phase representation.
5. Estimate a stationary noise profile from the lower-percentile magnitude values.
6. Subtract the estimated noise profile while retaining the phase.
7. Generate a **128-band Mel-spectrogram**.
8. Convert power to decibel scale.
9. Normalize the resulting spectrogram to the 0–1 range.
10. Fix the time dimension to 128 frames and return a **128 × 128** float32 array.

## Command

```bash
python ai_model/preprocessing/preprocessing.py --input-dir data/dataset --output-dir data/processed
```

The input directory must contain one subdirectory per class. The output preserves the same class names and stores one NumPy array per audio file.

## Supported formats

- `.wav`
- `.mp3`
- `.flac`
- `.ogg`

WAV is recommended for original field recordings because it is straightforward to archive and process consistently.
