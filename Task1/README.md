# ♻️ Edge AI Waste Classification Model

This project implements a lightweight Convolutional Neural Network (CNN) to classify waste items using **Edge AI**. It is designed for real-time deployment on devices such as Raspberry Pi or Android smartphones via **TensorFlow Lite**.

## 📌 Assignment Theme
**Pioneering Tomorrow’s AI Innovations**  
This submission fulfills the PLP Edge AI Prototype requirement — focusing on privacy, low latency, and real-time intelligent decision-making.

---

## 📂 Project Structure

| File | Description |
|------|-------------|
| `recyclenet_model.ipynb` | Full Colab notebook: training, evaluation, and conversion to TFLite |
| `recyclenet_model.tflite` | TensorFlow Lite version for deployment on edge devices |
| `recyclenet_model.h5` | Full model in HDF5 format (Keras legacy format) |
| `waste_dataset` | Training and validation image dataset (not included due to size) |

---

## 🧠 Model Summary

- **Architecture**: 3-layer CNN with ReLU activations and softmax output
- **Input shape**: 128x128 RGB images
- **Output**: 2 classes (e.g., recyclable vs non-recyclable)
- **Framework**: TensorFlow / Keras
- **Accuracy**:  
  - Final Training Accuracy: `89.42%`  
  - Final Validation Accuracy: `91.44%`

---

## 📊 Training Performance

| Epoch | Training Acc | Val Acc | Val Loss |
|-------|--------------|---------|----------|
| 1     | 76.78%       | 86.15%  | 0.3580   |
| 2     | 84.72%       | 87.39%  | 0.3286   |
| 3     | 86.00%       | 90.81%  | 0.2522   |
| 4     | 87.91%       | 87.66%  | 0.3207   |
| 5     | 89.42%       | 91.44%  | 0.2521   |

---

## 🔍 Edge AI Benefits

- ✅ **Low Latency**: Model runs locally on device without internet connection
- ✅ **Enhanced Privacy**: No data sent to cloud
- ✅ **Efficient Deployment**: Lightweight `.tflite` model for mobile/IoT
- ✅ **Energy-Efficient**: Ideal for battery-powered or offline environments

---

## 🚀 Deployment Instructions

1. Convert model to TensorFlow Lite:
    ```python
    converter = tf.lite.TFLiteConverter.from_keras_model(model)
    tflite_model = converter.convert()
    ```

2. Save the model:
    ```python
    with open("recyclenet_model.tflite", "wb") as f:
        f.write(tflite_model)
    ```

3. Deploy the `.tflite` file to a compatible device (e.g., Raspberry Pi or Android app).

---

