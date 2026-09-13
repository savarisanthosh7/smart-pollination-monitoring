# Dataset Information

## Classes

The project uses two acoustic classes:

1. **Bee Activity**
2. **Background Noise**

## Expected local structure

```text
ai_model/dataset/
├── Bee Activity/
│   ├── sample_001.wav
│   └── ...
└── Background Noise/
    ├── sample_001.wav
    └── ...
```

The actual dataset is not committed because its original contents and redistribution rights are not available in the reconstructed repository.

## Dataset preparation

Use consistent sample rates and audio formats where possible. Keep the validation set separated from training data to avoid leakage between recordings from the same source.
