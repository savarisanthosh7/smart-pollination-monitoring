# Project Materials and Evidence

This repository has been enhanced using the supplied project materials from the academic mini-project report and prototype images.

## Supplied project report

The source report documents a Smart Pollination Monitoring System using bioacoustic sensing, artificial intelligence, IoT and LoRa communication. The documented pipeline is:

**MEMS microphone → ESP32 → audio preprocessing → Mel-spectrogram → CNN classification → LoRa → receiver → IoT/Blynk monitoring**

The report describes Python-based audio processing and CNN training, ESP32 firmware for acquisition/communication, LoRa transmission, receiver-side output, and remote monitoring. It also documents experimental testing of the integrated system.

## Added visual evidence

`images/project-evidence.jpg` is a compact visual board assembled from the supplied project images. It includes:

- Hardware prototype photographs
- Local LCD detection output
- Blynk monitoring screen
- CNN training-accuracy plot
- Bee Mel-spectrogram
- Confusion matrix

These are project artifacts supplied by the developer/team and are included to make the repository easier to understand and more representative of the actual work.

## Important reproducibility note

The repository keeps a distinction between **documented project artifacts** and **reproducible measurements**. A plot or screenshot supplied in the report is not treated as a substitute for rerunning the experiment. When publishing final performance numbers, record the dataset source, split, preprocessing settings, model version and test conditions used to obtain them.

## Originality and attribution

The visual board uses the supplied project photographs/figures rather than stock images. The source report remains an academic project document; repository code and documentation should be updated only with material that the team is authorized to publish.
