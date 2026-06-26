
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import (
    Input, LSTM, Dense, Dropout, Conv1D,
    LayerNormalization, MultiHeadAttention,
    GlobalAveragePooling1D, BatchNormalization
)

def build_lstm(n_features, n_classes, name_suffix=""):
    inputs  = Input(shape=(1, n_features), name="input")
    x       = LSTM(128, return_sequences=False, name="lstm")(inputs)
    x       = Dropout(0.3, name="drop1")(x)
    x       = Dense(64, activation="relu", name="dense1")(x)
    x       = Dropout(0.2, name="drop2")(x)
    outputs = Dense(n_classes, activation="softmax", name="output")(x)
    model   = Model(inputs, outputs, name=f"LSTM_{name_suffix}")
    model.compile(optimizer="adam",
                  loss="sparse_categorical_crossentropy",
                  metrics=["accuracy"])
    return model

def build_cnn_lstm(n_features, n_classes, name_suffix=""):
    inputs = Input(shape=(1, n_features), name="input")
    x = Conv1D(64,  kernel_size=1, activation="relu", padding="same", name="conv1")(inputs)
    x = BatchNormalization(name="bn1")(x)
    x = Conv1D(128, kernel_size=1, activation="relu", padding="same", name="conv2")(x)
    x = BatchNormalization(name="bn2")(x)
    x = Dropout(0.2, name="drop1")(x)
    x = LSTM(128, return_sequences=False, name="lstm")(x)
    x = Dropout(0.3, name="drop2")(x)
    x = Dense(64, activation="relu", name="dense1")(x)
    x = Dropout(0.2, name="drop3")(x)
    outputs = Dense(n_classes, activation="softmax", name="output")(x)
    model   = Model(inputs, outputs, name=f"CNN_LSTM_{name_suffix}")
    model.compile(optimizer="adam",
                  loss="sparse_categorical_crossentropy",
                  metrics=["accuracy"])
    return model

def build_transformer_lstm(n_features, n_classes, name_suffix=""):
    inputs = Input(shape=(1, n_features), name="input")
    x      = LSTM(128, return_sequences=True, name="lstm")(inputs)
    x      = LayerNormalization(name="ln1")(x)
    attn   = MultiHeadAttention(num_heads=4, key_dim=32,
                                dropout=0.1, name="attention")(x, x)
    x      = tf.keras.layers.Add(name="add1")([x, attn])
    x      = LayerNormalization(name="ln2")(x)
    ffn    = Dense(256, activation="relu", name="ffn1")(x)
    ffn    = Dropout(0.1, name="ffn_drop")(ffn)
    ffn    = Dense(128, name="ffn2")(ffn)
    x      = tf.keras.layers.Add(name="add2")([x, ffn])
    x      = LayerNormalization(name="ln3")(x)
    x      = GlobalAveragePooling1D(name="gap")(x)
    x      = Dense(64, activation="relu", name="dense1")(x)
    x      = Dropout(0.3, name="drop1")(x)
    outputs = Dense(n_classes, activation="softmax", name="output")(x)
    model   = Model(inputs, outputs, name=f"TransLSTM_{name_suffix}")
    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
                  loss="sparse_categorical_crossentropy",
                  metrics=["accuracy"])
    return model
