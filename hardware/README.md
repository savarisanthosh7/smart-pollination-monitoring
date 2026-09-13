# Hardware

This directory documents the physical sensing and communication hardware used by the Smart Pollination Monitoring System.

## Hardware chain

```text
INMP441 microphone
       │ I2S
       ▼
     ESP32
       │ SPI
       ▼
   SX1278 LoRa
       │
     LoRa link
       ▼
ESP32 + SX1278 receiver
```

## Hardware roles

### 1. INMP441 MEMS microphone

The INMP441 provides digital environmental audio through I2S. It is the acoustic sensing element used to capture bee-related sound and surrounding noise.

### 2. ESP32

The ESP32 is the embedded controller for the sensing/radio node. It handles peripheral communication, sampling/control logic and LoRa communication.

### 3. SX1278 LoRa transceiver

The SX1278 is used for long-range, low-data-rate wireless transport of the classification packet from the field node to the receiving node.

### 4. Receiver ESP32

A second ESP32 with an SX1278 can receive the LoRa packet and expose the decoded information to the monitoring/gateway layer.

## Prototype considerations

- Verify the exact ESP32 board model before assigning GPIO pins.
- Verify the SX1278 module's operating voltage and logic levels for the selected board/module.
- Keep the microphone mechanically isolated from vibration sources.
- Protect the electronics from moisture, dust and direct weather exposure during field deployment.
- Record the actual radio frequency and antenna used in the deployment log.

## Validation checklist

- [ ] INMP441 produces valid I2S samples.
- [ ] ESP32 receives stable audio data.
- [ ] SX1278 initializes successfully.
- [ ] Transmitter and receiver use the same radio configuration.
- [ ] Receiver parses the complete application packet.
- [ ] Monitoring layer receives the decoded data.
- [ ] Field enclosure does not obstruct the microphone or antenna.

The repository does not invent a GPIO map. The final pin map must match the physical prototype and should be recorded after wiring is verified.
