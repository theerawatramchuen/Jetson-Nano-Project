import cv2 
import os 
  
def frame_capture(file):
    cam = cv2.VideoCapture(file) 
  
    try: 
        pathsave = "H:/VideoCapture/"+ os.path.basename(path) +""

        if not os.path.exists(pathsave): 
            os.makedirs(pathsave) 
  
    except OSError: 
        print ('Error: Creating directory') 
  
 
    currentframe = 0
  
    while(True): 
      
        ret,frame = cam.read() 
  
        if ret: 
            name = 'H:/VideoCapture/'+os.path.basename(path)+'/'+ str(currentframe) +'.jpg'
            print ('Capture and Save: ' + name) 
  
            cv2.imwrite(name, frame) 

            currentframe += 1
        else: 
            break
  
    cam.release() 
    cv2.destroyAllWindows() 

for file in os.listdir("H:/clip4x/4"):
    if file.endswith(".mp4"):
        path = os.path.join("H:/clip4x/4", file)
        frame_capture(path)
        