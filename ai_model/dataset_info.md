# Dataset Information

## Classification classes

The project is a binary acoustic classification task with the following labels:

```text
Bee Activity
Background Noise
```

## Directory layout

```text
data/
└── dataset/
    ├── Bee Activity/
    │   ├── recording_001.wav
    │   └── ...
    └── Background Noise/
        ├── recording_001.wav
        └── ...
```

Supported source formats in the preprocessing implementation are WAV, MP3, FLAC and OGG. WAV is recommended for field recordings because it preserves the captured waveform without an additional lossy encoding step.

## Labeling guidance

### Bee Activity
Use this class for recordings where the acoustic event of interest is bee activity and the label has been established from the actual recording/observation procedure.

### Background Noise
Use this class for recordings representing the environmental sound conditions that should not be classified as bee activity, such as ordinary field/background recordings according to the project's labeling protocol.

Do not label a recording as bee activity merely because it contains an arbitrary insect, machinery sound or other tonal event. The labeling rule should be documented with the experiment.

## Required metadata

For every recording used in a serious experiment, retain a metadata record containing as many of the following as are available:

- File name
- Class label
- Date/time
- Recording location or observation-point identifier
- Recorder/node identifier
- Sampling rate
- Recording duration
- Weather/environmental conditions when relevant
- Distance/orientation from the observation source when known
- Notes about unusual noise or events

## Data split

The training implementation uses a stratified 80/20 train-validation split with random seed 42. Keep recordings from the same continuous event/session together when designing a rigorous evaluation so that near-duplicate segments do not leak between training and validation.

## Dataset provenance

The repository does not claim a public dataset source or a specific number of recordings because those facts must come from the actual data collection/source used for the project. Add the verified source, license and class counts here when the dataset is finalized.

## Privacy and licensing

Only commit audio for which the project has permission to store and redistribute the recordings. Large raw datasets are excluded by `.gitignore` by default.
