"""Run inference with a trained Smart Pollination Monitoring CNN."""

from __future__ import annotations

import argparse
from pathlib import Path

import librosa
import numpy as np
import tensorflow as tf

SAMPLE_RATE = 16000
CLASSES = ["Background Noise", "Bee Activity"]


def make_input(audio_path: Path) -> np.ndarray:
    audio, sr = librosa.load(audio_path, sr=SAMPLE_RATE, mono=True)
    audio = librosa.util.normalize(audio)
    mel = librosa.feature.melspectrogram(
        y=audio, sr=sr, n_mels=128, fmin=50, fmax=sr // 2, power=2.0
    )
    mel = librosa.power_to_db(mel, ref=np.max)
    mel = (mel - mel.min()) / (mel.max() - mel.min() + 1e-8)
    mel = librosa.util.fix_length(mel, size=128, axis=1)
    mel = mel[:128, :128]
    if mel.shape != (128, 128):
        mel = np.resize(mel, (128, 128))
    return mel.astype("float32")[None, ..., None]


def predict(model_path: Path, audio_path: Path) -> tuple[str, float]:
    model = tf.keras.models.load_model(model_path)
    probabilities = model.predict(make_input(audio_path), verbose=0)[0]
    index = int(np.argmax(probabilities))
    return CLASSES[index], float(probabilities[index])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=Path, required=True)
    parser.add_argument("--input", type=Path, required=True)
    args = parser.parse_args()

    label, confidence = predict(args.model, args.input)
    print(f"Class: {label}")
    print(f"Confidence: {confidence:.4f}")


if __name__ == "__main__":
    main()
