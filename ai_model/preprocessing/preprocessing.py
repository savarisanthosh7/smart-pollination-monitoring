"""Audio preprocessing for the Smart Pollination Monitoring project."""

from __future__ import annotations

import argparse
from pathlib import Path

import librosa
import numpy as np


SAMPLE_RATE = 16000
N_MELS = 128
IMAGE_SIZE = (128, 128)


def reduce_noise(audio: np.ndarray, sr: int) -> np.ndarray:
    """Apply a simple, deterministic spectral noise-reduction operation."""
    stft = librosa.stft(audio)
    magnitude, phase = librosa.magphase(stft)
    noise_profile = np.percentile(magnitude, 20, axis=1, keepdims=True)
    clean_magnitude = np.maximum(magnitude - noise_profile, 0.0)
    return librosa.istft(clean_magnitude * phase, length=len(audio))


def audio_to_mel(path: Path) -> np.ndarray:
    audio, sr = librosa.load(path, sr=SAMPLE_RATE, mono=True)
    audio = librosa.util.normalize(audio)
    audio = reduce_noise(audio, sr)
    mel = librosa.feature.melspectrogram(
        y=audio,
        sr=sr,
        n_mels=N_MELS,
        fmin=50,
        fmax=sr // 2,
        power=2.0,
    )
    mel_db = librosa.power_to_db(mel, ref=np.max)
    mel_db = (mel_db - mel_db.min()) / (mel_db.max() - mel_db.min() + 1e-8)
    mel_db = librosa.util.fix_length(mel_db, size=128, axis=1)
    mel_db = mel_db[:128, :128]
    if mel_db.shape != IMAGE_SIZE:
        mel_db = np.resize(mel_db, IMAGE_SIZE)
    return mel_db.astype(np.float32)


def preprocess_directory(input_dir: Path, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    for class_dir in sorted(p for p in input_dir.iterdir() if p.is_dir()):
        class_out = output_dir / class_dir.name
        class_out.mkdir(parents=True, exist_ok=True)
        for audio_path in sorted(class_dir.glob("*")):
            if audio_path.suffix.lower() not in {".wav", ".mp3", ".flac", ".ogg"}:
                continue
            try:
                mel = audio_to_mel(audio_path)
                np.save(class_out / f"{audio_path.stem}.npy", mel)
                print(f"Processed: {audio_path}")
            except Exception as exc:
                print(f"Skipped {audio_path}: {exc}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    preprocess_directory(args.input_dir, args.output_dir)


if __name__ == "__main__":
    main()
