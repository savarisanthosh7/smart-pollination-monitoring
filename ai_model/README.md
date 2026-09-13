# AI Model

The AI subsystem classifies environmental audio into two classes:

- **Background Noise**
- **Bee Activity**

## Pipeline

```text
WAV / supported audio
        ↓
16 kHz mono loading
        ↓
Amplitude normalization
        ↓
Spectral noise reduction
        ↓
128-band Mel-spectrogram
        ↓
128 × 128 fixed representation
        ↓
3 convolutional stages
        ↓
Global average pooling
        ↓
64-unit dense layer
        ↓
2-unit softmax
```

## Source files

- `preprocessing/preprocessing.py` — converts recordings into model-ready `.npy` spectrograms.
- `training/train.py` — loads processed samples, creates the stratified split and trains the CNN.
- `inference/inference.py` — applies the same preprocessing to a new recording and predicts its class.
- `model/README.md` — describes generated model artifacts and their provenance.
- `dataset_info.md` — defines the dataset organization and recording metadata.

## Reproducibility

Use the same preprocessing settings for training and inference. Record the dataset version, class counts, recording conditions, model configuration and evaluation metrics for every experiment.

No performance metric in this directory should be treated as a measured result unless it is produced by an actual training/evaluation run.
