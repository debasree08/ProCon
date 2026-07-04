from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping

# ------------------------------------------------------
# Your ProCon-m LSTM
# ------------------------------------------------------

model = Sequential()

# First LSTM layer
model.add(
    LSTM(
        units=50,
        activation='tanh',
        return_sequences=True,
        input_shape=(3,1)
    )
)

model.add(Dropout(0.20))

# Second LSTM layer
model.add(
    LSTM(
        units=50,
        activation='tanh',
        return_sequences=False
    )
)

model.add(Dropout(0.20))

# Dense layer
model.add(Dense(16, activation='tanh'))

model.add(Dropout(0.10))

# Output layer
model.add(Dense(4, activation='softmax'))

model.summary()

############################### compiling ################################

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

############################### compiling ################################

early_stop = EarlyStopping(
    monitor='val_loss',
    patience=10,
    restore_best_weights=True
)

############################### training ################################


history = model.fit(
    X_train,
    y_train,
    validation_split=0.2,
    epochs=100,
    batch_size=64,
    callbacks=[early_stop],
    verbose=1
)

############################### evaluation ################################

import numpy as npS
from sklearn.metrics import accuracy_score, f1_score, classification_report

pred = np.argmax(model.predict(X_test), axis=1)

print("Accuracy :", accuracy_score(y_test, pred))
print("Micro F1 :", f1_score(y_test, pred, average='micro'))
print("Macro F1 :", f1_score(y_test, pred, average='macro'))

print(classification_report(y_test, pred))