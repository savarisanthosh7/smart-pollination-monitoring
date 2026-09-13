#include <SPI.h>
#include <LoRa.h>

// Verify these GPIO assignments against the actual prototype before use.
const int LORA_SS = 5;
const int LORA_RST = 14;
const int LORA_DIO0 = 2;
const long LORA_FREQUENCY = 433E6;

void setup() {
  Serial.begin(115200);
  while (!Serial) { delay(10); }

  LoRa.setPins(LORA_SS, LORA_RST, LORA_DIO0);
  if (!LoRa.begin(LORA_FREQUENCY)) {
    Serial.println("LoRa initialization failed");
    while (true) { delay(1000); }
  }
  Serial.println("BeeWatch receiver ready");
}

void loop() {
  int packetSize = LoRa.parsePacket();
  if (!packetSize) {
    return;
  }

  String packet;
  while (LoRa.available()) {
    packet += (char)LoRa.read();
  }

  Serial.print("Received: ");
  Serial.println(packet);
  Serial.print("RSSI: ");
  Serial.println(LoRa.packetRssi());
  Serial.print("SNR: ");
  Serial.println(LoRa.packetSnr());
}
