# Preprocessing

`preprocessing.py` converts source audio into normalized Mel-spectrogram arrays suitable for CNN training.

## Command

```bash
python preprocessing.py --input-dir ../dataset --output-dir ../processed
```

The script uses a 16 kHz mono audio representation, noise reduction, Mel-spectrogram conversion and a 128 × 128 output representation.
