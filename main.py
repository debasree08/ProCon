from preprocessing.preprocess import TrajectoryPreprocessor

# Dataset location
DATA_PATH = "data/raw"

# Recording to process
RECORDING_ID = 00

# Preprocess
preprocessor = TrajectoryPreprocessor(DATA_PATH)

df = preprocessor.process(RECORDING_ID)

print(df.head())

