# Blynk Setup

This document describes the dashboard integration without storing credentials in Git.

## Configuration flow

```text
LoRa receiver
     ↓
ESP32 / gateway application
     ↓
Blynk virtual pins
     ↓
Mobile/web dashboard
```

## Suggested widgets

- Current bee-activity state
- Classification confidence
- Last packet time
- Device connectivity status
- Activity history chart
- Alert indicator

## Credentials

Store Wi-Fi passwords, Blynk authentication tokens and other secrets in local configuration or environment variables. Never commit them to this repository.

## Integration contract

The monitoring application should convert the received packet into dashboard values. A typical packet is:

`BEEWATCH,<class>,<confidence>`

The exact Blynk virtual-pin mapping must be filled in after the original dashboard configuration is verified.
