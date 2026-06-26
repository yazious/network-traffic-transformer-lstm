
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split

def preprocess_darknet(path):
    df = pd.read_parquet(path)
    df["Label.1"] = df["Label.1"].astype(str).str.title()
    df["Label"]   = df["Label"].astype(str).str.title()
    feature_cols  = [c for c in df.columns if c not in ["Label", "Label.1"]]
    zero_var      = [c for c in feature_cols if df[c].nunique() <= 1]
    df.drop(columns=zero_var, inplace=True)
    feature_cols  = [c for c in df.columns if c not in ["Label", "Label.1"]]
    df[feature_cols] = df[feature_cols].replace([float("inf"), float("-inf")], float("nan"))
    df.dropna(inplace=True)
    le_4 = LabelEncoder()
    le_8 = LabelEncoder()
    df["label_4class"] = le_4.fit_transform(df["Label"])
    df["label_8class"] = le_8.fit_transform(df["Label.1"])
    feature_cols = [c for c in df.columns if c not in
                    ["Label", "Label.1", "label_4class", "label_8class"]]
    X = df[feature_cols].values.astype("float32")
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)
    return X_scaled, df["label_4class"].values, df["label_8class"].values, le_4, le_8

def preprocess_cicids(folder_path):
    import os
    dfs = []
    for root, _, files in os.walk(folder_path):
        for f in files:
            if f.endswith(".csv"):
                tmp = pd.read_csv(os.path.join(root, f),
                                  encoding="utf-8", low_memory=False)
                tmp.columns = tmp.columns.str.strip()
                dfs.append(tmp)
    df = pd.concat(dfs, ignore_index=True)
    df.columns = df.columns.str.strip()
    label_col = [c for c in df.columns if "label" in c.lower()][0]
    df.dropna(inplace=True)
    feat_cols = [c for c in df.columns if c != label_col]
    df[feat_cols] = df[feat_cols].replace([float("inf"), float("-inf")], float("nan"))
    df.dropna(inplace=True)
    zero_var = [c for c in feat_cols if df[c].nunique() <= 1]
    df.drop(columns=zero_var, inplace=True)
    df[label_col] = df[label_col].str.strip().str.replace("\ufffd", "", regex=False).str.strip()
    class_counts  = df[label_col].value_counts()
    valid_classes = class_counts[class_counts >= 100].index.tolist()
    df = df[df[label_col].isin(valid_classes)]
    balanced = []
    for cls in valid_classes:
        tmp = df[df[label_col] == cls]
        if len(tmp) > 50000:
            tmp = tmp.sample(50000, random_state=42)
        balanced.append(tmp)
    df = pd.concat(balanced, ignore_index=True).sample(frac=1, random_state=42)
    le = LabelEncoder()
    df["label_enc"] = le.fit_transform(df[label_col])
    feat_cols = [c for c in df.columns if c not in [label_col, "label_enc"]]
    X = df[feat_cols].values.astype("float32")
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)
    return X_scaled, df["label_enc"].values, le

def split_and_reshape(X, y, test_size=0.2, random_state=42):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y)
    X_train = X_train.reshape(X_train.shape[0], 1, X_train.shape[1])
    X_test  = X_test.reshape(X_test.shape[0],  1, X_test.shape[1])
    return X_train, X_test, y_train, y_test
