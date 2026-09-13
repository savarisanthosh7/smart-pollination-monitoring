<div align="center">

<img src="images/banner.svg" alt="Smart Pollination Monitoring System" width="900"/>

### AI + IoT + LoRa + Bioacoustic Sensing

**An end-to-end prototype for monitoring acoustic bee activity and reporting observations remotely.**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![ESP32](https://img.shields.io/badge/ESP32-IoT-E7352C?style=for-the-badge&logo=espressif&logoColor=white)
![LoRa](https://img.shields.io/badge/LoRa-SX1278-0B7285?style=for-the-badge)
![AI](https://img.shields.io/badge/AI-CNN-F4C95D?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-2F855A?style=for-the-badge)

</div>

---

## 🐝 Project at a glance

Pollinating insects are important to crop production, but continuous manual observation of bee activity is difficult. This project explores **acoustic sensing + machine learning + long-range IoT communication** as a practical monitoring pipeline.

An **INMP441 MEMS microphone** captures environmental sound, an **ESP32** handles embedded acquisition/control, an **SX1278 LoRa** link transports compact classification data, and a **CNN** separates **Bee Activity** from **Background Noise**. The result is surfaced through a remote **Blynk** monitoring layer.

> **Core idea:** turn an acoustic event into a useful remote field observation.

### 🔎 Pipeline

```text
Acoustic sensing
      ↓
Audio preprocessing
      ↓
Mel-spectrogram
      ↓
CNN classification
      ↓
LoRa transmission
      ↓
ESP32 receiver / gateway
      ↓
Blynk monitoring
```

---

## ✨ What makes this project interesting

<table>
<tr>
<td width="50%">

### 🎙️ Bioacoustic sensing
Digital audio from an INMP441 microphone is used as the sensing signal for bee-activity analysis.

</td>
<td width="50%">

### 🧠 AI classification
A three-stage CNN processes fixed-size Mel-spectrogram representations and classifies two acoustic classes.

</td>
</tr>
<tr>
<td>

### 📡 Long-range communication
SX1278 LoRa is used to move compact classification information between the field node and receiver.

</td>
<td>

### 📱 Remote monitoring
Blynk provides a simple IoT layer for observing the latest classification information remotely.

</td>
</tr>
</table>

---

## 🧩 End-to-end architecture

```text
                  FIELD / APIARY
                       │
                       ▼
              ┌─────────────────┐
              │ INMP441         │
              │ MEMS microphone │
              └────────┬────────┘
                       │ I2S audio
                       ▼
              ┌─────────────────┐
              │ ESP32 node      │
              │ acquisition     │
              └────────┬────────┘
                       │ audio data
                       ▼
              ┌─────────────────┐
              │ Preprocessing   │
              │ noise reduction │
              └────────┬────────┘
                       ▼
              ┌─────────────────┐
              │ Mel-spectrogram │
              │ 128 × 128       │
              └────────┬────────┘
                       ▼
              ┌─────────────────┐
              │ 3-stage CNN     │
              └────────┬────────┘
                       ▼
          ┌──────────────────────────┐
          │ Bee Activity /           │
          │ Background Noise         │
          └────────────┬─────────────┘
                       │ class + confidence
                       ▼
              ┌─────────────────┐
              │ SX1278 LoRa TX  │
              └────────┬────────┘
                       │ LoRa
                       ▼
              ┌─────────────────┐
              │ SX1278 LoRa RX  │
              │ ESP32 receiver  │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │ Blynk monitoring│
              └─────────────────┘
```

### Processing responsibilities

| Layer | Responsibility |
|---|---|
| INMP441 | Capture digital acoustic signal |
| ESP32 | Embedded acquisition/control and LoRa node operation |
| Python preprocessing | Noise reduction and Mel-spectrogram generation |
| CNN | Classify bee activity versus background noise |
| SX1278 | Long-range wireless packet transport |
| Receiver/gateway | Receive and parse LoRa packets |
| Blynk | Remote visualization and monitoring |

The repository does not claim that the CNN runs natively on the ESP32 unless an embedded deployment of the trained model is separately added and validated. The supplied Python pipeline is the reference training/inference implementation.

---

## 🧠 AI model

### Input representation

The documented preprocessing pipeline uses:

- Mono audio
- Target sample rate: **16 kHz**
- Mel bands: **128**
- Frequency range: **50 Hz to Nyquist frequency**
- Log-power conversion using decibels
- Fixed representation: **128 × 128**

The preprocessing stage performs amplitude normalization and deterministic spectral noise-profile subtraction before Mel-spectrogram generation.

### CNN architecture

1. `Conv2D(16, 3×3)` + ReLU + max pooling
2. `Conv2D(32, 3×3)` + ReLU + max pooling
3. `Conv2D(64, 3×3)` + ReLU + max pooling
4. Global average pooling
5. Dense layer with 64 units and ReLU
6. Dropout of 0.30
7. Two-unit softmax output

```text
0 = Background Noise
1 = Bee Activity
```

### Training configuration

- Stratified 80/20 train-validation split
- Random seed: 42
- Optimizer: Adam
- Loss: sparse categorical cross-entropy
- Default epochs: 25
- Default batch size: 32
- Shuffling during training

Accuracy and evaluation figures should be treated as **experiment artifacts from the supplied project material**, not as independently reproduced benchmarks.

---

## 📊 Project results

The repository includes the project's **actual supplied ML result figures** as visual artifacts when they are added to the `images/ml/` directory:

- Training / validation accuracy curve
- Bee Mel-spectrogram
- Audio waveform
- Confusion matrix
- Classification report

These figures are kept separately from the hardware and IoT screenshots so the README remains clean and easy to scan.

---

## 🔩 Hardware

The documented prototype uses:

- ESP32 development board
- INMP441 digital MEMS microphone
- SX1278 LoRa transceiver module
- Regulated power supply appropriate for the selected boards
- Interconnects and an enclosure suitable for field deployment

### Hardware principle

The INMP441 supplies digital audio to the ESP32 through I2S. The ESP32 node handles acquisition and communication. Classification data is transported through the SX1278 LoRa radio, while a second SX1278-equipped ESP32 acts as the receiving node.

> Exact GPIO values are not stated as universal facts because they depend on the ESP32 board variant and the wiring used in the physical prototype. Verify the wiring against the actual hardware before flashing firmware.

---

## 📡 LoRa packet format

The application payload follows:

```text
BEEWATCH,<class>,<confidence>,<node_id>,<sequence>
```

The receiver validates the packet prefix, extracts the fields, and reports the received values through the serial monitor. Confidence is represented as a decimal value between 0 and 1 by the application layer.

---

## 📱 Blynk monitoring

The Blynk layer is documented separately in `blynk/`. The monitoring interface is intended to expose useful deployment information such as:

- Latest bee/background classification
- Classification confidence
- Packet sequence
- Node identifier
- Last update status
- Received signal information when supplied by the receiver
- Activity history/trend when historical storage is enabled

Keep Blynk authentication tokens and Wi-Fi credentials outside Git. Use the configuration guide in `blynk/configuration/blynk_setup.md`.

---

## 📁 Repository structure

```text
smart-pollination-monitoring/
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── hardware/
│   ├── README.md
│   ├── components/
│   │   └── components_list.md
│   └── circuit/
│       └── connection_guide.md
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
│   ├── project-materials.md
│   └── references.md
└── images/
    ├── banner.svg
    ├── hardware/
    ├── ml/
    └── blynk/
```

---

## 🚀 Quick start

### 1. Create the Python environment

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

### 2. Preprocess the actual dataset

```bash
python ai_model/preprocessing/preprocessing.py --input-dir "data/dataset" --output-dir "data/processed"
```

### 3. Train the CNN

```bash
python ai_model/training/train.py --data-dir "data/processed" --output "ai_model/model/beewatch_cnn.keras"
```

### 4. Run inference

```bash
python ai_model/inference/inference.py --model "ai_model/model/beewatch_cnn.keras" --input "path/to/recording.wav"
```

### 5. Prepare ESP32 + LoRa

Open the required sketch in Arduino IDE or PlatformIO, install ESP32 board support and the SX1278/LoRa library used by the sketch, then verify the GPIO definitions against the actual hardware.

---

## 🧪 Field deployment sequence

1. Mount the INMP441 at the observation location.
2. Connect the microphone to the ESP32 I2S interface.
3. Power the sensor node using a stable supply.
4. Capture representative recordings under real field conditions.
5. Label recordings as bee activity or background noise.
6. Preprocess the recordings using the repository pipeline.
7. Train and validate the CNN using the actual dataset.
8. Evaluate on recordings not used for training.
9. Configure matching LoRa settings on transmitter and receiver.
10. Configure Blynk with the user's actual template/datastream settings.
11. Deploy and monitor classification behaviour and packet reception.

---

## 🛡️ Reproducibility & authenticity

This repository is intentionally conservative about experimental claims. It does **not** invent or silently assume:

- Dataset size or source
- Training/validation/test performance
- LoRa range
- Battery life
- Field detection rate
- Unverified GPIO wiring
- Blynk credentials
- Trained model weights that were not actually produced

When new measurements are available, document the dataset, split, preprocessing settings, model version and test conditions alongside the result.

---

## 📚 Documentation

- `hardware/README.md` — hardware role and deployment notes
- `hardware/components/components_list.md` — component list
- `hardware/circuit/connection_guide.md` — connection guide
- `ai_model/dataset_info.md` — dataset organization and labeling
- `ai_model/preprocessing/preprocessing.py` — audio preprocessing
- `ai_model/training/train.py` — CNN training
- `ai_model/inference/inference.py` — inference
- `firmware/` — ESP32 LoRa transmitter/receiver firmware
- `blynk/` — dashboard and configuration documentation
- `documentation/project-materials.md` — supplied report/image evidence notes
- `images/` — original project visuals, organized by hardware, ML and Blynk

---

<div align="center">

### 🌱 Sense → Classify → Communicate → Monitor

*Built as a practical AI + IoT exploration for smarter pollination monitoring.*

**MIT License** · See `LICENSE`

</div>
