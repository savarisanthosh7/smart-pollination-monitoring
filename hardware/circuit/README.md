# Circuit and Wiring Guide

This document defines the electrical interfaces used by the prototype architecture. It deliberately avoids presenting unverified GPIO numbers as if they were the final physical wiring.

## 1. INMP441 to ESP32

The INMP441 is a digital I2S microphone. The connection uses:

| INMP441 signal | ESP32 function |
|---|---|
| VDD | 3.3 V supply |
| GND | Ground |
| SCK / BCLK | I2S bit clock GPIO |
| WS / LRCLK | I2S word-select GPIO |
| SD | I2S data-input GPIO |
| L/R | Channel-select connection according to the microphone board wiring |

The actual GPIO numbers must be set in the transmitter firmware to match the prototype.

## 2. SX1278 to ESP32

The SX1278 communicates over SPI. The typical signal groups are:

| SX1278 signal | ESP32 function |
|---|---|
| VCC | Module-compatible supply |
| GND | Ground |
| SCK | SPI clock |
| MOSI | SPI controller-to-radio data |
| MISO | SPI radio-to-controller data |
| NSS / CS | Chip-select GPIO |
| RESET | Reset GPIO |
| DIO0 | Radio interrupt/status GPIO |
| ANT | Suitable antenna connection |

Use the exact GPIO assignments from the physical board and the selected LoRa library configuration. Do not connect the antenna port without an appropriate antenna/load configuration.

## 3. Receiver

The receiver uses the same SPI radio interface. It must use compatible LoRa frequency and modulation settings with the transmitter.

## 4. Power

The power design must provide a stable regulated supply. The exact regulator/current rating depends on the selected ESP32 board, SX1278 module and deployment power source. Do not infer a battery capacity or runtime without measurement.

## 5. Bring-up sequence

1. Test ESP32 alone.
2. Verify INMP441 I2S capture.
3. Verify SX1278 initialization.
4. Test transmitter and receiver with a known short packet.
5. Verify packet parsing.
6. Connect the AI output to the packet-generation path.
7. Connect the monitoring service.
8. Perform an outdoor range and reliability test.

## 6. Field installation

Mount the microphone where the target acoustic environment is measurable but protected from rain and direct contamination. Keep the antenna clear of large conductive objects and use an enclosure appropriate for the deployment environment.
