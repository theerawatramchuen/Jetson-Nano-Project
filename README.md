# Jetson-Nano-Project
## Deploy NVCaffe Model from Digits with Jetson Nano

### Example Deployment Digits Caffe Model for Jetson-Inference Classification 
./imagenet-camera.py \
--prototxt=/home/thee/Desktop/catdogpanda/deploy.prototxt \
--model=/home/thee/Desktop/catdogpanda/snapshot_iter_16890.caffemodel \
--labels=/home/thee/Desktop/catdogpanda/labels.txt \
--input_blob=data \
--output_blob=softmax \
--camera=/dev/video0 --width=640 --height=480
