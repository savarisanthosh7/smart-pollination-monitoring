# Blynk Dashboard

The Blynk dashboard is the remote user interface for the monitoring system.

## Dashboard information

The dashboard should expose the latest information received from the LoRa field node through the gateway/application layer.

### Primary values

- **Classification:** `Bee Activity` or `Background Noise`
- **Confidence:** classifier probability for the selected class
- **Node ID:** identifies the transmitting field node
- **Sequence:** detects packet progression and helps identify missed/duplicated packets
- **RSSI:** radio signal strength reported by the receiver
- **SNR:** LoRa signal-to-noise ratio reported by the receiver
- **Last update:** time of the latest successfully received record

## Suggested layout

```text
┌─────────────────────────────────────┐
│       SMART POLLINATION MONITOR      │
├──────────────────┬──────────────────┤
│ Classification   │ Confidence       │
│ Bee Activity     │ 0.00 – 1.00      │
├──────────────────┼──────────────────┤
│ Node ID          │ Sequence         │
│ field-node-01    │ received value   │
├──────────────────┼──────────────────┤
│ RSSI             │ SNR              │
│ receiver value   │ receiver value   │
├─────────────────────────────────────┤
│       Activity history / trend      │
└─────────────────────────────────────┘
```

The values shown above describe the dashboard fields, not fabricated live measurements.

## Alerting

An alert can be configured for a sustained `Bee Activity` state or another project-defined condition after the actual field monitoring logic is finalized. Thresholds should be determined from the project's measured data rather than inserted as arbitrary demo values.

## Dashboard setup

Create the actual datastreams in the Blynk console, assign the corresponding widgets, and use the real datastream identifiers in the gateway integration. Authentication credentials must remain outside the repository.
