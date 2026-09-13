# Project Documentation

This directory contains documentation that explains how the Smart Pollination Monitoring system is assembled and operated.

## System objective

Use acoustic sensing and machine learning to identify bee activity against environmental background noise, then communicate the classification over LoRa for remote monitoring.

## Functional chain

```text
Acoustic capture
→ signal preprocessing
→ Mel-spectrogram
→ CNN classification
→ classification packet
→ LoRa transmission
→ LoRa reception
→ monitoring/dashboard
```

## Engineering records to maintain

For the physical project, keep the following records alongside the repository when available:

- Hardware bill of materials and exact part numbers
- Verified GPIO/pin map
- Audio sampling configuration
- Dataset provenance and license
- Labeling protocol
- Training run configuration
- Validation/test metrics
- LoRa frequency and radio configuration
- Field range/reliability measurements
- Power source and measured operating time
- Blynk template/datastream configuration
- Deployment date and node identifier

The repository contains implementation details that are known from the project design, while measured values and prototype-specific details should be entered from actual experiments.
