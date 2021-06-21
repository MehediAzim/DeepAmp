import numpy as np
from tensorflow.keras.models import load_model

model = "model.h5py"
model = load_model(model)

def calculate_performance(test_num, pred_y, labels):
    tp = 0
    fp = 0
    tn = 0
    fn = 0
    for index in range(test_num):
        if labels[index] == 1:
            if labels[index] == pred_y[index]:
                tp = tp + 1
            else:
                fn = fn + 1
        else:
            if labels[index] == pred_y[index]:
                tn = tn + 1
            else:
                fp = fp + 1

    # entering any of the else statement means that the evaluation metric is invalid
    acc = float(tp + tn) / test_num
    
    if((tp + fp) != 0):
      sensitivity = float(tp) / (tp + fn)
    else:
      sensitivity = 0

    if((tn + fp) != 0):
      specificity = float(tn) / (tn + fp)
    else:
      specificity = 0

    MCC = float(tp * tn - fp * fn) / (np.sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn)))
    
    return acc, sensitivity, specificity, MCC

def classifier(data,label,args):
    
    # scores = model.evaluate([X_train_two[test_index,:,:]], y_train[test_index], verbose=0)
    probabilities = model.predict([data])
    predicted_classes = probabilities >= 0.5
    predicted_classes = predicted_classes.astype(int)

    acc,  sensitivity, specificity, MCC = calculate_performance(len(label), predicted_classes, label)
    print('Result Summary:')
    print('------------------------------')
    print('accuracy',acc, end =", ")
    print('MCC',MCC, end =", ")
    print('sensitivity',sensitivity, end =", ")
    print('specificity',specificity)