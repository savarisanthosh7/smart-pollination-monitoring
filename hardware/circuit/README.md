# Circuit / Wiring Reference

This folder documents the intended signal flow rather than claiming an exact recovered schematic.

## Connections to verify

### INMP441 → ESP32

The INMP441 is a digital I2S microphone. Connect power and ground according to the module's datasheet and map the I2S clock, word-select and data signals to the GPIOs selected in the final firmware.

### SX1278 → ESP32

The SX1278 normally uses SPI plus control pins. The final prototype must verify:

- SPI SCK
- SPI MISO
- SPI MOSI
- Chip select (NSS/SS)
- Reset
- DIO0 interrupt/status pin
- 3.3 V supply and ground

The example firmware contains a configurable starting pin map, but it is explicitly not a substitute for the project's original wiring.

## Field safety

Use an appropriate regulated supply and antenna for the selected SX1278 variant and comply with the applicable radio-frequency rules for the deployment location.
