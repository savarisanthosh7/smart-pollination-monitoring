"""Train and evaluate the three-stage CNN for bee-activity audio classification."""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
import tensorflow as tf

IMAGE_SHAPE = (128, 128, 1)
CLASSES = ["Background Noise", "Bee Activity"]


def load_dataset(data_dir: Path):
    x, y = [], []
    for label, class_name in enumerate(CLASSES):
        class_dir = data_dir / class_name
        if not class_dir.exists():
            raise FileNotFoundError(f"Missing class directory: {class_dir}")
        files = sorted(class_dir.glob("*.npy"))
        if not files:
            raise FileNotFoundError(f"No processed samples in: {class_dir}")
        for file in files:
            arr = np.load(file).astype("float32")
            if arr.shape != (128, 128):
                raise ValueError(f"Invalid shape {arr.shape} in {file}; expected (128, 128)")
            x.append(arr[..., None])
            y.append(label)
    return np.stack(x), np.asarray(y, dtype="int64")


def build_model() -> tf.keras.Model:
    inputs = tf.keras.Input(shape=IMAGE_SHAPE, name="mel_spectrogram")
    x = tf.keras.layers.Conv2D(16, 3, padding="same", activation="relu")(inputs)
    x = tf.keras.layers.MaxPooling2D()(x)
    x = tf.keras.layers.Conv2D(32, 3, padding="same", activation="relu")(x)
    x = tf.keras.layers.MaxPooling2D()(x)
    x = tf.keras.layers.Conv2D(64, 3, padding="same", activation="relu")(x)
    x = tf.keras.layers.MaxPooling2D()(x)
    x = tf.keras.layers.GlobalAveragePooling2D()(x)
    x = tf.keras.layers.Dense(64, activation="relu")(x)
    x = tf.keras.layers.Dropout(0.30)(x)
    outputs = tf.keras.layers.Dense(2, activation="softmax", name="class_probability")(x)
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
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    tf.keras.utils.set_random_seed(args.seed)
    x, y = load_dataset(args.data_dir)

    x_train, x_val, y_train, y_val = train_test_split(
        x, y, test_size=0.20, random_state=args.seed, stratify=y
    )

    model = build_model()
    model.summary()

    args.output.parent.mkdir(parents=True, exist_ok=True)
    best_path = args.output.parent / "best_model.keras"
    history_path = args.output.parent / "training_history.csv"

    callbacks = [
        tf.keras.callbacks.ModelCheckpoint(
            best_path, monitor="val_loss", save_best_only=True
        ),
        tf.keras.callbacks.CSVLogger(history_path),
    ]

    model.fit(
        x_train,
        y_train,
        validation_data=(x_val, y_val),
        epochs=args.epochs,
        batch_size=args.batch_size,
        shuffle=True,
        callbacks=callbacks,
    )

    model.save(args.output)
    probabilities = model.predict(x_val, verbose=0)
    predictions = np.argmax(probabilities, axis=1)

    report = classification_report(
        y_val,
        predictions,
        target_names=CLASSES,
        digits=4,
        zero_division=0,
    )
    matrix = confusion_matrix(y_val, predictions)

    (args.output.parent / "classification_report.txt").write_text(report, encoding="utf-8")
    np.savetxt(args.output.parent / "confusion_matrix.csv", matrix, fmt="%d", delimiter=",")
    (args.output.parent / "classes.txt").write_text("\n".join(CLASSES) + "\n", encoding="utf-8")

    print(f"Training samples: {len(x_train)}")
    print(f"Validation samples: {len(x_val)}")
    print(f"Saved model: {args.output}")
    print(f"Saved best model: {best_path}")
    print("\nValidation classification report:\n")
    print(report)
    print("Confusion matrix:")
    print(matrix)


if __name__ == "__main__":
    main()
