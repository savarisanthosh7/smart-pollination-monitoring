# Hardware Components

## Core prototype hardware

| Component | Function | Interface |
|---|---|---|
| ESP32 development board | Embedded controller for sensing/control and radio communication | I2S, SPI, GPIO |
| INMP441 digital MEMS microphone | Environmental acoustic sensing | I2S |
| SX1278 LoRa transceiver | Wireless transmission/reception of classification data | SPI |
| Regulated power supply | Stable electrical supply for the node | Power |
| Jumper wires/connectors | Prototype interconnection | Electrical |
| Field enclosure | Environmental protection for electronics | Mechanical |

## Roles

**INMP441:** captures the acoustic signal as digital I2S data.

**ESP32:** interfaces with the microphone and radio and manages the embedded node.

**SX1278:** transports compact application packets between the field transmitter and receiver.

**Receiver ESP32:** receives and parses the LoRa packet and can forward the decoded data to the monitoring layer.

## Prototype build record

The final bill of materials should record the exact purchased ESP32 board, SX1278 module variant, microphone breakout, power source, antenna and enclosure used in the physical prototype. Generic component names are used here because the exact commercial part numbers were not supplied.

## Electrical checks

- Confirm module supply voltage before powering.
- Confirm common ground between connected modules.
- Verify I2S microphone wiring.
- Verify SPI wiring and LoRa control lines.
- Verify antenna/load arrangement before radio transmission.
- Use a suitable enclosure for field conditions.
