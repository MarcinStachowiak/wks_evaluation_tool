from sklearn.metrics import matthews_corrcoef
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import numpy as np
__author__ = "Marcin Stachowiak"
__version__ = "1.0"
__email__ = "marcin.stachowiak.ms@gmail.com"

def print_full_metrics_classification(y_true, y_pred):
    print('Matthews correlation coefficient (MCC): %f' % matthews_corrcoef(y_true, y_pred))
    print('Accuracy: %f' % accuracy_score(y_true, y_pred))
    print('Confusion Matrix:')
    print(confusion_matrix(y_true, y_pred))
    return (accuracy_score(y_true, y_pred))
