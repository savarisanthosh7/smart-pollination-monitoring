#include <SPI.h>
#include <LoRa.h>

// Set these values to the GPIO wiring used by the physical prototype.
const int LORA_SS = 5;
const int LORA_RST = 14;
const int LORA_DIO0 = 2;
const long LORA_FREQUENCY = 433E6;
const char* NODE_ID = "field-node-01";

unsigned long sequenceNumber = 0;

bool validClass(const String& label) {
  return label == "Bee Activity" || label == "Background Noise";
}

bool parseClassificationLine(String line, String& label, float& confidence) {
  line.trim();
  int first = line.indexOf(',');
  if (first <= 0) return false;

  label = line.substring(0, first);
  String score = line.substring(first + 1);
  score.trim();
  confidence = score.toFloat();

  if (!validClass(label)) return false;
  if (confidence < 0.0f || confidence > 1.0f) return false;
  return true;
}

void sendClassification(const String& label, float confidence) {
  sequenceNumber++;

  LoRa.beginPacket();
  LoRa.print("BEEWATCH,");
  LoRa.print(label);
  LoRa.print(",");
  LoRa.print(confidence, 4);
  LoRa.print(",");
  LoRa.print(NODE_ID);
  LoRa.print(",");
  LoRa.print(sequenceNumber);
  LoRa.endPacket();

  Serial.print("TX: BEEWATCH,");
  Serial.print(label);
  Serial.print(",");
  Serial.print(confidence, 4);
  Serial.print(",");
  Serial.print(NODE_ID);
  Serial.print(",");
  Serial.println(sequenceNumber);
}

void setup() {
  Serial.begin(115200);
  while (!Serial) delay(10);

  LoRa.setPins(LORA_SS, LORA_RST, LORA_DIO0);
  if (!LoRa.begin(LORA_FREQUENCY)) {
    Serial.println("LoRa initialization failed");
    while (true) delay(1000);
  }

  Serial.println("BeeWatch transmitter ready");
  Serial.println("Input format: Bee Activity,0.9500");
  Serial.println("Input format: Background Noise,0.9500");
}

void loop() {
  if (!Serial.available()) return;

  String line = Serial.readStringUntil('\n');
  String label;
  float confidence;

  if (!parseClassificationLine(line, label, confidence)) {
    Serial.println("Invalid classification input");
    return;
  }

  sendClassification(label, confidence);
}
