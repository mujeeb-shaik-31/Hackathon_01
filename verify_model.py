import tensorflow as tf

# Path to the model file
model_path = '"C:\Users\mujee\OneDrive\Documents\Desktop\GIT PROJECTS\data science projects\Hackthon project\ml_model\model.h5"'

# Try to load the model
try:
    model = tf.keras.models.load_model(model_path)
    print("Model loaded successfully!")
    model.summary()  # Print the model architecture
except Exception as e:
    print("Error loading the model:", e)