"""Run CNN inference on one real audio recording."""

from __future__ import annotations

import argparse
from pathlib import Path

import librosa
import numpy as np
import tensorflow as tf

SAMPLE_RATE = 16000
N_MELS = 128
IMAGE_SIZE = (128, 128)
CLASSES = ["Background Noise", "Bee Activity"]


def reduce_noise(audio: np.ndarray) -> np.ndarray:
    stft = librosa.stft(audio)
    magnitude, phase = librosa.magphase(stft)
    noise_profile = np.percentile(magnitude, 20, axis=1, keepdims=True)
    clean_magnitude = np.maximum(magnitude - noise_profile, 0.0)
    return librosa.istft(clean_magnitude * phase, length=len(audio))


def prepare_audio(path: Path) -> np.ndarray:
    audio, _ = librosa.load(path, sr=SAMPLE_RATE, mono=True)
    if audio.size == 0:
        raise ValueError("The audio file contains no samples.")
    audio = librosa.util.normalize(audio)
    audio = reduce_noise(audio)
    mel = librosa.feature.melspectrogram(
        y=audio,
        sr=SAMPLE_RATE,
        n_mels=N_MELS,
        fmin=50,
        fmax=SAMPLE_RATE // 2,
        power=2.0,
    )
    mel = librosa.power_to_db(mel, ref=np.max)
    mel = (mel - mel.min()) / (mel.max() - mel.min() + 1e-8)
    mel = librosa.util.fix_length(mel, size=128, axis=1)[:128, :128]
    if mel.shape != IMAGE_SIZE:
        raise ValueError(f"Unexpected model input shape: {mel.shape}")
    return mel.astype(np.float32)[None, ..., None]


def predict(model_path: Path, audio_path: Path) -> tuple[str, float]:
    model = tf.keras.models.load_model(model_path)
    sample = prepare_audio(audio_path)
    probabilities = model.predict(sample, verbose=0)[0]
    index = int(np.argmax(probabilities))
    return CLASSES[index], float(probabilities[index])


def main() -> None:
    parser = argparse.ArgumentParser(description="Classify bee-related acoustic activity.")
    parser.add_argument("--model", type=Path, required=True)
    parser.add_argument("--input", type=Path, required=True)
    args = parser.parse_args()

    label, confidence = predict(args.model, args.input)
    print(f"Prediction: {label}")
    print(f"Confidence: {confidence:.4f}")


if __name__ == "__main__":
    main()
