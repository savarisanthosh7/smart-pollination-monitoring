# ESP32 + LoRa Firmware

The firmware directory contains the two embedded roles in the communication path:

- `esp32_transmitter/transmitter.ino` — sends validated AI classification records through SX1278 LoRa.
- `esp32_receiver/receiver.ino` — receives, validates and decodes the records.

## Communication protocol

Application packets use the following format:

```text
BEEWATCH,<class>,<confidence>,<node_id>,<sequence>
```

Allowed classes are exactly:

```text
Bee Activity
Background Noise
```

Confidence is expected in the range `0.0` to `1.0`.

## Transmitter integration

The transmitter accepts a classification record over its serial input in this format:

```text
Bee Activity,0.9500
```

or:

```text
Background Noise,0.9500
```

This makes the radio firmware independent of the Python CNN runtime. A host/embedded AI implementation can supply the real classification output to the ESP32 without changing the LoRa packet format.

## Radio configuration

Both sketches currently use the same configurable LoRa frequency and radio control-pin definitions. These values are not presented as final prototype wiring; verify them against the actual ESP32/SX1278 assembly before deployment.

## Required Arduino libraries

- ESP32 board support package
- `LoRa` library compatible with the SX127x family
- `SPI` library supplied with the Arduino/ESP32 environment

## Deployment checklist

- Verify antenna connection.
- Verify supply voltage.
- Verify SPI wiring.
- Verify NSS/CS, RESET and DIO0 wiring.
- Verify both radios use the same frequency/configuration.
- Confirm packet reception in the receiver serial monitor.
- Only then connect the receiver output to the cloud/dashboard integration.
