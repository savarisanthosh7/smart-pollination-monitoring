#include <SPI.h>
#include <LoRa.h>

// Set these values to the GPIO wiring used by the physical prototype.
const int LORA_SS = 5;
const int LORA_RST = 14;
const int LORA_DIO0 = 2;
const long LORA_FREQUENCY = 433E6;

bool parsePacket(const String& packet, String& label, float& confidence, String& nodeId, unsigned long& sequence) {
  if (!packet.startsWith("BEEWATCH,")) return false;

  String body = packet.substring(9);
  int p1 = body.indexOf(',');
  int p2 = body.indexOf(',', p1 + 1);
  int p3 = body.indexOf(',', p2 + 1);
  if (p1 <= 0 || p2 <= p1 || p3 <= p2) return false;

  label = body.substring(0, p1);
  confidence = body.substring(p1 + 1, p2).toFloat();
  nodeId = body.substring(p2 + 1, p3);
  sequence = strtoul(body.substring(p3 + 1).c_str(), nullptr, 10);

  if (label != "Bee Activity" && label != "Background Noise") return false;
  if (confidence < 0.0f || confidence > 1.0f) return false;
  if (nodeId.length() == 0) return false;
  return true;
}

void setup() {
  Serial.begin(115200);
  while (!Serial) delay(10);

  LoRa.setPins(LORA_SS, LORA_RST, LORA_DIO0);
  if (!LoRa.begin(LORA_FREQUENCY)) {
    Serial.println("LoRa initialization failed");
    while (true) delay(1000);
  }

  Serial.println("BeeWatch receiver ready");
}

void loop() {
  int packetSize = LoRa.parsePacket();
  if (!packetSize) return;

  String packet;
  while (LoRa.available()) packet += (char)LoRa.read();

  String label;
  String nodeId;
  float confidence;
  unsigned long sequence;

  if (!parsePacket(packet, label, confidence, nodeId, sequence)) {
    Serial.print("Rejected packet: ");
    Serial.println(packet);
    return;
  }

  Serial.println("--- LoRa packet ---");
  Serial.print("Node: ");
  Serial.println(nodeId);
  Serial.print("Classification: ");
  Serial.println(label);
  Serial.print("Confidence: ");
  Serial.println(confidence, 4);
  Serial.print("Sequence: ");
  Serial.println(sequence);
  Serial.print("RSSI: ");
  Serial.println(LoRa.packetRssi());
  Serial.print("SNR: ");
  Serial.println(LoRa.packetSnr());
}
