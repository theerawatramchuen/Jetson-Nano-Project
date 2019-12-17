# Jetson-Nano-Project
### Example Deployment Digits Caffe Model for Jetson-Inference Image Classification 
#### Put Command Line at Jetson nano Terminal with Correct Path Directory
$ ./imagenet-camera.py \
--prototxt=/home/thee/Desktop/catdogpanda/deploy.prototxt \
--model=/home/thee/Desktop/catdogpanda/snapshot_iter_16890.caffemodel \
--labels=/home/thee/Desktop/catdogpanda/labels.txt \
--input_blob=data \
--output_blob=softmax \
--camera=/dev/video0 --width=640 --height=480
