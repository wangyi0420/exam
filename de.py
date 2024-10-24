import jetson.inference
import jetson.utils

# Load the detection network
net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.5)

# Use an image as input instead of a live video stream
image_path = "/home/nvidia/jetson-inference/data/images/airplane_0.jpg"
img = jetson.utils.loadImage(image_path)

# Run object detection on the image
detections = net.Detect(img)

# Render the image and display it
jetson.utils.saveImage("output.jpg", img)

# Output detection results
for detection in detections:
    print(f"ClassID: {detection.ClassID}")
    print(f"Confidence: {detection.Confidence}")
    print(f"Left: {detection.Left}")
    print(f"Top: {detection.Top}")
    print(f"Right: {detection.Right}")
    print(f"Bottom: {detection.Bottom}")
    print(f"Width: {detection.Width}")
    print(f"Height: {detection.Height}")
    print(f"Area: {detection.Area}")
    print(f"Center: {detection.Center}")