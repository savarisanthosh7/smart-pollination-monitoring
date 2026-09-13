# Model Inference

`inference.py` loads a trained Keras model and classifies a real audio recording using the same preprocessing assumptions as the training pipeline.

## Usage

```bash
python ai_model/inference/inference.py --model ai_model/model/best_model.keras --input path/to/recording.wav
```

## Output

The program reports:

- Predicted class
- Confidence of the selected class

The confidence is the softmax probability returned by the trained model. It should not be interpreted as a calibrated probability of real-world bee presence without additional calibration and field validation.

## Deployment integration

For LoRa transmission, the resulting label and confidence can be supplied to the ESP32 transmitter using the documented serial input format:

```text
Bee Activity,0.9500
```

or

```text
Background Noise,0.9500
```

The number shown is only the required input format, not a measured project result.
