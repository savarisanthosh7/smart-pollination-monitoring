# Blynk Configuration

Blynk is the remote monitoring layer for the project. The dashboard should be connected to the receiving/gateway software that has access to the decoded LoRa classification data.

## Required Blynk-side information

Create or use the actual Blynk template/device for the deployment and record the following locally:

- Blynk Template ID
- Blynk Template Name
- Blynk device/authentication token
- Wi-Fi/network credentials for the gateway, when Wi-Fi is used
- Datastream IDs used by the dashboard

**Do not commit any token, password or API key to GitHub.**

## Recommended datastream mapping

The monitoring application can expose these logical values:

| Logical value | Purpose |
|---|---|
| Classification | Latest `Bee Activity` or `Background Noise` result |
| Confidence | CNN confidence from 0 to 1 |
| Node ID | Source field node |
| Sequence | Packet sequence number |
| RSSI | Received LoRa signal strength |
| SNR | Received LoRa signal-to-noise ratio |
| Last update | Most recent packet time |

Assign actual Blynk Virtual Pins/datastream IDs in the user's Blynk console. This repository does not invent those IDs.

## Security

Keep credentials in the local environment or deployment configuration. If a credential is accidentally committed, revoke/rotate it in the provider console rather than merely deleting the line from a later commit.

## Deployment flow

```text
LoRa receiver
    ↓
decoded packet
    ↓
gateway/application
    ↓
Blynk datastream update
    ↓
mobile/web dashboard
```

The exact gateway transport can be selected during deployment; the radio firmware itself is not coupled to a Blynk credential.
