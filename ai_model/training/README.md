# Training

`train.py` loads processed 128 × 128 spectrogram arrays and trains a three-stage CNN.

Default training settings:

- Validation split: 20%
- Epochs: 25
- Batch size: 32
- Optimizer: Adam
- Output activation: 2-class softmax

Example:

```bash
python train.py --data-dir ../processed --output ../model/beewatch_cnn.keras
```
