# Jetson-Nano-Project

### Install v4l-utils and gv4l2
$ sudo apt-get install v4l-utils <br>
$ sudo apt-get install qv4l2 <br>

$ lsusb -t <br>
$ v4l2-ctl --list-devices <br>
$ qv4l2 -d /dev/video1 <br>

### Headless contrl via Jupyter Notebook
ssh -L 8000:localhost:8888 thee@192.168.1.49   ### From any desktop <br><br>
Start the Jupyter server on the Jetson with jupyter notebook, then go to http://localhost:8000 on your own computer <br><br>
$jupyter notebook <br>

### ROS   
Installation <br>
Follow https://github.com/dusty-nv/ros_deep_learning <br>
sudo apt-get install ros-melodic-uvc-camera* <br>
ls /dev/video* <br>
rosrun uvc_camera uvc_camera_node _device:=/dev/video1 <br>

export ROS_MASTER_URI=http://192.168.1.50:11311/       ### Or $roscore   <br>
rosrun image_publisher image_publisher __name:=image_publisher ~/jetson-inference/data/images/dog_0.jpg <br>
source ~/catkin_ws/devel/setup.bash <br>
rosrun ros_deep_learning detectnet /detectnet/image_in:=/image_publisher/image_raw _model_name:=coco-dog <br>

### Jetbot
https://github.com/NVIDIA-AI-IOT/jetbot/wiki/Bill-of-Materials?fbclid=IwAR1fxhyIXBcduk5Dqpuiawq59q_T5GrC3PtZg1VQZW1AEQD_3x4GC7owMa4

### Example Deployment Digits Caffe Model for Jetson-Inference Image Classification 
#### Put Command Line at Jetson nano Terminal with Correct Home Path Directory
$ ./imagenet-camera.py \
--prototxt=/home/thee/Desktop/catdogpanda/deploy.prototxt \
--model=/home/thee/Desktop/catdogpanda/snapshot_iter_16890.caffemodel \
--labels=/home/thee/Desktop/catdogpanda/labels.txt \
--input_blob=data \
--output_blob=softmax \
--camera=/dev/video0 --width=640 --height=480

cd ~/jetson-inference/build/aarch64/bin    ########### With USB2 Webcam (Change Camera resolution macth with your camera)

#### ######### Image Classification
$ python3 imagenet-camera.py --model=resnet18 --input_blob=input_0 --output_blob=output_0 --labels=labels.txt --width=640 --height=480 --camera=/dev/video0

$ ./imagenet-console --model=resnet18.onnx --input_blob=input_0 --output_blob=output_0 --labels=labels.txt ~/datasets/cat_dog/test/cat/01.jpg cat.jpg

$ ./detectnet-camera.py --width=640 --height=480 --camera=/dev/video0 --network=facenet  

$ ./detectnet-camera.py --width=640 --height=480 --camera=/dev/video0 --network=coco-dog

$ ./camera-capture --camera=/dev/video0 --width=640 --height=480

#### ######## Custom Model Classification
$ NET=networks/esbx

$ ./imagenet-console P3-111.jpg output_0.jpg --prototxt=$NET/deploy.prototxt --model=$NET/snapshot_iter_4752.caffemodel --labels=$NET/labels.txt --input_blob=data --output_blob=softmax

$ ./imagenet-camera --prototxt=$NET/deploy.prototxt --model=$NET/snapshot_iter_4752.caffemodel --labels=$NET/labels.txt --input_blob=data --output_blob=softmax --width=640 --height=480 --camera=/dev/video0

$ NET=networks/dogcatpanda

$ ./imagenet-camera --prototxt=$NET/deploy.prototxt --model=$NET/snapshot_iter_8000.caffemodel --labels=$NET/labels.txt --input_blob=data --output_blob=softmax --width=640 --height=480 --camera=/dev/video0

$ NET=networks/ebs5c

$ ./imagenet-console P3-111.jpg output_0.jpg --prototxt=$NET/deploy.prototxt --model=$NET/snapshot_iter_2580.caffemodel --labels=$NET/labels.txt --input_blob=data --output_blob=softmax

$ ./imagenet-camera --prototxt=$NET/deploy.prototxt --model=$NET/snapshot_iter_2580.caffemodel --labels=$NET/labels.txt --input_blob=data --output_blob=softmax --width=640 --height=480 --camera=/dev/video0

$ NET=networks/ebsx3c

$ ./imagenet-console P3-111.jpg output_0.jpg --prototxt=$NET/deploy.prototxt --model=$NET/snapshot_iter_2850.caffemodel --labels=$NET/labels.txt --input_blob=data --output_blob=softmax

#### ######## DeepStream  Resnet18 and Yolotiny3  
$ cd ~/opt/nvidia/deepstream/deepstream-4.0/bin

$ deepstream-app -c /opt/nvidia/deepstream/deepstream-4.0/samples/configs/deepstream-app/source1_usb_dec_infer_resnet_int8.txt

$ cd ~/opt/nvidia/deepstream/deepstream-4.0/sources/objectDetector_Yolo

$ deepstream-app -c deepstream_app_config_yoloV3_tiny.txt


### IDS Camera Lib installation
https://www.ensenso.com/manual/installation-on-nvidia-jetson.htm

### Sample cv2.VideoCapture() of Opencv
https://www.programcreek.com/python/example/85663/cv2.VideoCapture

### Darknet YOLO v3 on Jetson Nano
https://ai4sig.org/2019/06/jetson-nano-darknet-yolov3/?fbclid=IwAR0yq3C2yRK4WVe56UGH_V78Q8eQBYBPq-SG9HDou3tqChKiVvZ9-AC5kes

### Hello AI World : NVIDIA Jetson
![](https://github.com/dusty-nv/jetson-inference/raw/master/docs/images/deep-vision-header.jpg)
https://github.com/dusty-nv/jetson-inference

