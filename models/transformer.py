from tensorflow.keras.layers import *

from tensorflow.keras.models import Model

inputs=Input(shape=(10,6))

x=Dense(32)(inputs)

att=MultiHeadAttention(
        num_heads=2,
        key_dim=16
)(x,x)

x=LayerNormalization()(x+att)

ff=Dense(64,activation='relu')(x)

ff=Dense(32)(ff)

x=LayerNormalization()(x+ff)

x=GlobalAveragePooling1D()(x)

outputs=Dense(4,activation='softmax')(x)

model=Model(inputs,outputs)

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

model.summary()

############################## training ##############################

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

############################## evaluation ##############################

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
