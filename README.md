# Smart Pollination Monitoring

## AI + IoT + LoRaWAN based Bee Pollination Monitoring System

> Reconstructed implementation repository based on the project specification available in this conversation. Missing original experimental assets, trained weights, and credentials are intentionally not fabricated.

## 1. Project Overview

Smart Pollination Monitoring is an AI + IoT system for monitoring bee activity and supporting pollination assessment. The system combines an INMP441 digital microphone, ESP32, SX1278 LoRa radio, edge/cloud processing, a CNN-based audio classifier, and a Blynk dashboard.

The central idea is to distinguish **Bee Activity** from **Background Noise** using acoustic sensing. A transmitter captures audio, performs lightweight feature preparation/classification as configured, and sends a compact classification packet through LoRa. A receiver forwards the packet to the monitoring application/dashboard.

## 2. Objectives

- Monitor bee activity continuously.
- Detect acoustic patterns associated with bee activity.
- Reduce false detections caused by background noise.
- Send classification results over a low-power LoRa link.
- Present remote monitoring information through Blynk.
- Keep the system modular so the AI model, radio firmware, and dashboard can be updated independently.

## 3. System Architecture

```text
Bee activity / ambient sound
          |
          v
     INMP441 Mic
          |
          v
        ESP32
          |
          +---- Audio preprocessing / feature extraction
          |
          v
       CNN model
          |
          v
 Bee Activity / Background Noise
          |
          v
     SX1278 LoRa TX
          |
       LoRa link
          |
          v
     SX1278 LoRa RX
          |
          v
 ESP32 receiver / gateway
          |
          v
 Blynk dashboard / monitoring
```

## 4. AI Pipeline

1. Capture an audio segment.
2. Apply noise-reduction/preprocessing operations.
3. Convert the audio representation to a Mel-spectrogram.
4. Resize the spectrogram representation to **128 × 128**.
5. Pass the representation through a 3-stage CNN.
6. Use softmax output for the two classes:
   - `Bee Activity`
   - `Background Noise`
7. Return the predicted class and confidence.

### Training configuration

The reconstructed training script supports:

- 80/20 train-validation split
- Adam optimizer
- 25 epochs
- Batch size 32
- Configurable two-class dataset
- Saved model output

The repository does **not** claim a particular accuracy, precision, recall, F1 score, or trained model file because those original artifacts were not available.

## 5. Dataset

Expected directory structure:

```text
ai_model/dataset/
├── Bee Activity/
└── Background Noise/
```

The project specification describes a dataset containing these two classes. Place the actual audio dataset locally; dataset files are ignored by Git.

## 6. Hardware

| Component | Purpose |
|---|---|
| ESP32 | Sensor acquisition and control |
| INMP441 | Digital audio sensing |
| SX1278 LoRa | Long-range wireless communication |
| Power supply | Portable node power |
| Optional receiver/gateway ESP32 | LoRa packet reception |

Exact GPIO assignments should be verified against the physical prototype before flashing firmware.

## 7. Firmware

The `firmware/` directory contains separate transmitter and receiver sketches. The packet format is intentionally simple and readable:

```text
BEEWATCH,<class>,<confidence>
```

Example:

```text
BEEWATCH,Bee Activity,0.94
```

Do not treat this example as a measured result; it is only a packet-format example.

## 8. Blynk

The `blynk/` directory documents the dashboard architecture and configuration approach. Credentials and authentication tokens are deliberately excluded from the repository.

Recommended dashboard information:

- Current classification
- Confidence
- Last received packet
- Device/node status
- Historical activity trend
- Alert state

## 9. Repository Structure

```text
smart-pollination-monitoring/
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── hardware/
│   ├── README.md
│   ├── circuit/
│   │   └── README.md
│   └── components/
│       └── components_list.md
├── firmware/
│   ├── README.md
│   ├── esp32_transmitter/
│   │   ├── README.md
│   │   └── transmitter.ino
│   └── esp32_receiver/
│       ├── README.md
│       └── receiver.ino
├── ai_model/
│   ├── README.md
│   ├── dataset_info.md
│   ├── preprocessing/
│   │   ├── README.md
│   │   └── preprocessing.py
│   ├── training/
│   │   ├── README.md
│   │   └── train.py
│   ├── inference/
│   │   ├── README.md
│   │   └── inference.py
│   └── model/
│       └── README.md
├── blynk/
│   ├── README.md
│   ├── configuration/
│   │   └── blynk_setup.md
│   └── dashboard/
│       └── README.md
├── documentation/
│   ├── README.md
│   └── references.md
└── images/
    └── README.md
```

## 10. Quick Start

### Python environment

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### Preprocess audio

```bash
python ai_model/preprocessing/preprocessing.py --input-dir "ai_model/dataset" --output-dir "ai_model/processed"
```

### Train

```bash
python ai_model/training/train.py --data-dir "ai_model/processed" --output "ai_model/model/beewatch_cnn.keras"
```

### Inference

```bash
python ai_model/inference/inference.py --model "ai_model/model/beewatch_cnn.keras" --input "sample.wav"
```

## 11. Important Notes

- Replace the placeholder GPIO values in the Arduino sketches after confirming the actual board wiring.
- Keep Wi-Fi passwords, Blynk tokens, API keys, and other secrets outside source control.
- Do not commit raw datasets or large model files unless project licensing permits it.
- Hardware and radio performance must be validated on the actual prototype.
- The repository is a clean reconstruction, not a claim that unavailable original files have been recovered.

## 12. License

MIT License. See `LICENSE`.
