#include <SPI.h>
#include <LoRa.h>

// Verify these GPIO assignments against the actual prototype before use.
const int LORA_SS = 5;
const int LORA_RST = 14;
const int LORA_DIO0 = 2;
const long LORA_FREQUENCY = 433E6;

const char* classification = "Background Noise";
float confidence = 0.0f;

void setup() {
  Serial.begin(115200);
  while (!Serial) { delay(10); }

  LoRa.setPins(LORA_SS, LORA_RST, LORA_DIO0);
  if (!LoRa.begin(LORA_FREQUENCY)) {
    Serial.println("LoRa initialization failed");
    while (true) { delay(1000); }
  }
  Serial.println("BeeWatch transmitter ready");
}

void sendClassification(const char* label, float score) {
  LoRa.beginPacket();
  LoRa.print("BEEWATCH,");
  LoRa.print(label);
  LoRa.print(",");
  LoRa.print(score, 4);
  LoRa.endPacket();

  Serial.print("Sent: BEEWATCH,");
  Serial.print(label);
  Serial.print(",");
  Serial.println(score, 4);
}

void loop() {
  // Replace this demonstration state with the output of the actual
  // microphone/AI inference pipeline when deploying the prototype.
  sendClassification(classification, confidence);
  delay(5000);
}
