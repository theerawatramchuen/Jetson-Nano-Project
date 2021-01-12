import requests
import json
import time
import os
import base64
import cv2 as cv
from requests.exceptions import Timeout

def encode_frame(frame):
    img = frame
    _, imdata = cv.imencode('.JPG', frame)
    byte = base64.b64encode(imdata).decode('ascii')
    del (img)
    del (imdata)
    return byte

def dict_to_obj(our_dict):
    if "__class__" in our_dict:
        class_name = our_dict.pop("__class__")
        module_name = our_dict.pop("__module__")
        module = __import__(module_name)
        class_ = getattr(module,class_name)
        obj = class_(**our_dict)
    else:
        obj = our_dict
    return obj

def main():
    font = cv.FONT_HERSHEY_SIMPLEX
    cap = cv.VideoCapture('saw.avi')
    errCnt = 0
    gttl = 0
    addr = 'http://10.151.22.202/DL_Server'
    #addr = 'http://4320cf5fd8d3.ngrok.io/DL_Server'
    connection_url = addr + '/api/dl'
    r = requests.get(connection_url, timeout=5)

    while (cap.isOpened()):
        ret, frame = cap.read()
        if not ret:  # New
            break  # Get out if we don't read a frame successfully
        print(frame.shape)
        sum_ct = 0
        try:
            st_time = time.time()
            response = requests.post(connection_url,data={'Image' : encode_frame(frame),
                                                          'BOM':'ST',
                                                          'Operation' : 'cut',
                                                          'Process' : 'hairline',
                                                          'ProcessNO':'223',
                                                          'Client_ID':'MC-09'})
            cycle_time = time.time() - st_time
            sum_ct = sum_ct + cycle_time
            #avg_ct = sum_ct / (cnt+1)
            gttl = gttl + 1
        except Timeout:
            errCnt = errCnt + 1
            print(errCnt,'Timed Out')
        else:
            result_dict = json.loads(response.text)
            a = dict_to_obj(result_dict[0])
            print (gttl,result_dict,' cycletime(mS):',round(cycle_time*1e3),r)
        #cv2.waitKey(1000)
        print('Error Time out: %, hit',errCnt/50000*100,errCnt)

        # Display the resulting frame
        out = a['Class']
        if out == 'Good':
            cv.putText(frame, out, (10, 500), font, 4, (0, 255, 0), 5, cv.LINE_AA)
        elif out == 'Bad':
            cv.putText(frame, out, (10, 500), font, 4, (0, 0, 255), 5, cv.LINE_AA)
        elif out == 'None':
            cv.putText(frame, out, (10, 500), font, 4, (255, 255, 255), 5, cv.LINE_AA)
        else:
            out == 'Error'

#        cv.imshow('frame', frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()

if __name__ == '__main__':
    main()




