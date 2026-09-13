"""Train the three-stage CNN used for bee-activity classification."""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow as tf

IMAGE_SHAPE = (128, 128, 1)


def load_dataset(data_dir: Path):
    classes = ["Background Noise", "Bee Activity"]
    x, y = [], []
    for label, class_name in enumerate(classes):
        class_dir = data_dir / class_name
        if not class_dir.exists():
            continue
        for file in sorted(class_dir.glob("*.npy")):
            arr = np.load(file).astype("float32")
            if arr.shape != (128, 128):
                continue
            x.append(arr[..., None])
            y.append(label)
    if not x:
        raise FileNotFoundError(
            f"No processed .npy samples found in {data_dir}. "
            "Run preprocessing first."
        )
    return np.stack(x), np.asarray(y, dtype="int64"), classes


def build_model() -> tf.keras.Model:
    inputs = tf.keras.Input(shape=IMAGE_SHAPE)
    x = tf.keras.layers.Conv2D(16, 3, padding="same", activation="relu")(inputs)
    x = tf.keras.layers.MaxPooling2D()(x)
    x = tf.keras.layers.Conv2D(32, 3, padding="same", activation="relu")(x)
    x = tf.keras.layers.MaxPooling2D()(x)
    x = tf.keras.layers.Conv2D(64, 3, padding="same", activation="relu")(x)
    x = tf.keras.layers.MaxPooling2D()(x)
    x = tf.keras.layers.GlobalAveragePooling2D()(x)
    x = tf.keras.layers.Dense(64, activation="relu")(x)
    x = tf.keras.layers.Dropout(0.30)(x)
    outputs = tf.keras.layers.Dense(2, activation="softmax")(x)
    model = tf.keras.Model(inputs, outputs)
    model.compile(
        optimizer=tf.keras.optimizers.Adam(),
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"],
    )
    return model


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--epochs", type=int, default=25)
    parser.add_argument("--batch-size", type=int, default=32)
    args = parser.parse_args()

    x, y, classes = load_dataset(args.data_dir)
    x_train, x_val, y_train, y_val = train_test_split(
        x, y, test_size=0.20, random_state=42, stratify=y
    )

    model = build_model()
    model.summary()
    model.fit(
        x_train,
        y_train,
        validation_data=(x_val, y_val),
        epochs=args.epochs,
        batch_size=args.batch_size,
        shuffle=True,
    )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    model.save(args.output)
    (args.output.parent / "classes.txt").write_text("\n".join(classes) + "\n", encoding="utf-8")
    print(f"Saved model: {args.output}")


if __name__ == "__main__":
    main()
