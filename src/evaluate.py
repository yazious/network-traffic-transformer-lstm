
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import (accuracy_score, precision_score,
                             recall_score, f1_score,
                             confusion_matrix, classification_report)

def evaluate_model(model, X_test, y_test, le, model_name):
    y_prob = model.predict(X_test, verbose=0)
    y_pred = np.argmax(y_prob, axis=1)
    return {
        "Model"    : model_name,
        "Accuracy" : accuracy_score(y_test, y_pred),
        "Precision": precision_score(y_test, y_pred, average="weighted", zero_division=0),
        "Recall"   : recall_score(y_test, y_pred, average="weighted", zero_division=0),
        "F1-Score" : f1_score(y_test, y_pred, average="weighted", zero_division=0),
    }

def plot_confusion_matrix(model, X_test, y_test, le, title, save_path):
    y_pred = np.argmax(model.predict(X_test, verbose=0), axis=1)
    cm     = confusion_matrix(y_test, y_pred)
    cm_pct = cm.astype("float") / cm.sum(axis=1)[:, np.newaxis] * 100
    plt.figure(figsize=(10, 8))
    sns.heatmap(cm_pct, annot=True, fmt=".1f", cmap="Blues",
                xticklabels=le.classes_, yticklabels=le.classes_)
    plt.title(title, fontweight="bold")
    plt.ylabel("True Label"); plt.xlabel("Predicted Label")
    plt.tight_layout()
    plt.savefig(save_path, dpi=150, bbox_inches="tight")
    plt.show()
