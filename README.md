# Jetson-Nano-Project
### Example Deployment Digits Caffe Model for Jetson-Inference Image Classification 
#### Put Command Line at Jetson nano Terminal with Correct Home Path Directory
$ ./imagenet-camera.py \
--prototxt=/home/thee/Desktop/catdogpanda/deploy.prototxt \
--model=/home/thee/Desktop/catdogpanda/snapshot_iter_16890.caffemodel \
--labels=/home/thee/Desktop/catdogpanda/labels.txt \
--input_blob=data \
--output_blob=softmax \
--camera=/dev/video0 --width=640 --height=480


### IDS Camera Lib installation
https://www.ensenso.com/manual/installation-on-nvidia-jetson.htm

### Sample cv2.VideoCapture() of Opencv
https://www.programcreek.com/python/example/85663/cv2.VideoCapture

### Darknet YOLO v3 on Jetson Nano
https://ai4sig.org/2019/06/jetson-nano-darknet-yolov3/?fbclid=IwAR0yq3C2yRK4WVe56UGH_V78Q8eQBYBPq-SG9HDou3tqChKiVvZ9-AC5kes

### Hello AI World : NVIDIA Jetson
![](https://github.com/dusty-nv/jetson-inference/raw/master/docs/images/deep-vision-header.jpg)
https://github.com/dusty-nv/jetson-inference
