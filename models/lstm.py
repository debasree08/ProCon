from tensorflow.keras.models import Sequential

from tensorflow.keras.layers import LSTM,Dense

# model=Sequential()

# model.add(LSTM(64,input_shape=(3,1)))

# model.add(Dense(4,activation='softmax'))

timesteps = X_train.shape[1]
n_features = X_train.shape[2]

model = Sequential()

model.add(
    LSTM(
        64,
        input_shape=(timesteps, n_features)
    )
)

model.add(Dense(4, activation='softmax'))

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

model.summary()

############################## data splitting ##########################

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(
    X,
    Y,
    test_size=0.2,
    stratify=Y,
    random_state=42
)

############################## training ##########################

from tensorflow.keras.callbacks import EarlyStopping

early_stop = EarlyStopping(
    monitor='val_loss',
    patience=10,
    restore_best_weights=True
)

history = model.fit(
    X_train,
    y_train,
    validation_split=0.2,
    epochs=100,
    batch_size=64,
    callbacks=[early_stop],
    verbose=1
)

############################## results ##########################

from sklearn.metrics import *

pred=np.argmax(model.predict(X_test),axis=1)

print("Accuracy",
      accuracy_score(y_test,pred))

print("Micro F1",
      f1_score(y_test,pred,
               average='micro'))

print("Macro F1",
      f1_score(y_test,pred,
               average='macro'))

print(classification_report(
    y_test,
    pred
))

