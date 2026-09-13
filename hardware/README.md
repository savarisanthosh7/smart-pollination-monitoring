# Hardware

The sensing node is designed around an ESP32, INMP441 microphone and SX1278 LoRa transceiver.

## Functional chain

```text
Acoustic environment
      ↓
   INMP441
      ↓
    ESP32
      ↓
Classification packet
      ↓
   SX1278
      ↓
    LoRa link
```

## Electrical note

Use the voltage requirements of the selected ESP32 board and SX1278 module. Verify all grounds are common and verify the actual GPIO wiring before powering the prototype.

## Validation checklist

- [ ] Microphone produces valid digital samples.
- [ ] ESP32 receives microphone data without clipping/errors.
- [ ] LoRa module initializes successfully.
- [ ] Antenna is connected before transmission.
- [ ] Receiver gets packets at the expected frequency.
- [ ] RSSI/SNR values are recorded during field testing.
