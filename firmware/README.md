# Firmware

ESP32 firmware is separated into transmitter and receiver applications.

- `esp32_transmitter/` sends classification packets over SX1278 LoRa.
- `esp32_receiver/` receives packets and reports RSSI/SNR over serial.

Install the LoRa Arduino library appropriate for the selected SX1278 module. Verify the radio frequency and GPIO configuration for the hardware actually used.
