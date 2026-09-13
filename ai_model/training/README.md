# CNN Training

The training script builds and trains the project's three-stage convolutional neural network for binary bee-acoustic classification.

## Dataset input

The script expects processed NumPy spectrograms arranged as:

```text
processed/
├── Background Noise/
│   └── *.npy
└── Bee Activity/
    └── *.npy
```

Every sample must have shape `128 × 128`.

## Model

```text
Input: 128 × 128 × 1
    ↓
Conv2D 16 + ReLU
    ↓
MaxPool
    ↓
Conv2D 32 + ReLU
    ↓
MaxPool
    ↓
Conv2D 64 + ReLU
    ↓
MaxPool
    ↓
GlobalAveragePooling
    ↓
Dense 64 + ReLU
    ↓
Dropout 0.30
    ↓
Dense 2 + Softmax
```

## Default experiment settings

- Validation split: 20%
- Stratification: enabled
- Random seed: 42
- Optimizer: Adam
- Loss: sparse categorical cross-entropy
- Epochs: 25
- Batch size: 32

## Training command

```bash
python ai_model/training/train.py --data-dir data/processed --output ai_model/model/beewatch_cnn.keras
```

The run produces the requested model plus a best-checkpoint model, training history, class list, classification report and confusion matrix.

Those outputs are generated from the actual dataset at runtime; the repository does not contain fabricated metrics.
