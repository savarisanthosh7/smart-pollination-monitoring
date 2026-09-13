# Inference

`inference.py` loads a trained Keras model, creates a 128 × 128 Mel-spectrogram input from an audio file, and prints the predicted class and confidence.

Example:

```bash
python inference.py --model ../model/beewatch_cnn.keras --input sample.wav
```
