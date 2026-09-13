# AI Model

The AI subsystem classifies acoustic windows into two project classes: `Bee Activity` and `Background Noise`.

## Pipeline

```text
Audio
 ↓
Noise reduction / normalization
 ↓
Mel-spectrogram
 ↓
128 × 128 input
 ↓
CNN stage 1
 ↓
CNN stage 2
 ↓
CNN stage 3
 ↓
Dense classifier
 ↓
Softmax
 ↓
Class + confidence
```

The implementation is split into preprocessing, training and inference so each stage can be tested independently.
