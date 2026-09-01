import numpy as np

# Universal functions (ufuncs) adalah fungsi matematika 
# yang otomatis bekerja elementwise ke seluruh array 
# — tanpa loop, dan biasanya sangat cepat karena 
# diimplementasi di level C.
arr = np.array([1, 4, 9, 16, 25])
print(np.sqrt(arr))    # [1. 2. 3. 4. 5.]
print(np.exp(arr))     # e^x untuk tiap elemen
print(np.log(arr))     # ln(x) untuk tiap elemen

def sigmoid(x):
    return 1 / (1 + np.exp(-x))   # ini persis fungsi aktivasi di neural network!

#soal 1
x = np.array([-2, -1, 0, 1, 2])
print(sigmoid(x))

#soal 2
x = np.array([-3, -1, 0, 2, 5])
relu = np.maximum(0, x) #implementasi fungsi ReLU
print(relu)  # [0 0 0 2 5]

#soal 3
logits = np.array([2.0, 1.0, 0.1])
exp_logits = np.exp(logits) #pangkat untuk tiap elemen
softmax = exp_logits / exp_logits.sum()
print(softmax)
print(softmax.sum()) #1.0 -> selalu total 100%, ini ciri khas softmax

#soal 4
y_pred = np.array([0.9, 0.1, 0.8, 0.3])
y_true = np.array([1, 0, 1, 0])
mse = np.mean((y_pred - y_true) ** 2)
print(mse)