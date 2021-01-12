import requests
import json
import time
import os
import base64
import cv2 as cv
from requests.exceptions import Timeout

def encode_img(str_img_path):
    img = cv.imread(str_img_path)
    _, imdata = cv.imencode('.JPG', img)
    byte = base64.b64encode(imdata).decode('ascii')
    del (img)
    del (imdata)
    return byte

def main():
    strpath = "C:/Users/41162395/Desktop/Dataset/"

    print("path image : "+strpath)

    list_imgfile = []

    for root, directory, file in os.walk(strpath):
              for file_selected in file:
                        if '.jpg' in file_selected:
                                  list_imgfile.append(root+file_selected)

    while (True):
        errCnt = 0
        gttl = 0
        addr = 'http://10.151.22.202/DL_Server'
        #addr = 'http://4320cf5fd8d3.ngrok.io/DL_Server'
        connection_url = addr + '/api/dl'
        r = requests.get(connection_url, timeout=5)
        for f in list_imgfile: #while (True):
            sum_ct = 0
            for cnt in range(1):
                try:
                    st_time = time.time()
                    response = requests.post(connection_url,data={'Image' : encode_img(f),
                                                                  'BOM':'ST',
                                                                  'Operation' : 'cut',
                                                                  'Process' : 'hairline',
                                                                  'ProcessNO':'223',
                                                                  'Client_ID':'MC-09'})
                    cycle_time = time.time() - st_time
                    sum_ct = sum_ct + cycle_time
                    avg_ct = sum_ct / (cnt+1)
                    gttl = gttl + 1
                except Timeout:
                    errCnt = errCnt + 1
                    print(errCnt,'Timed Out')
                else:
                    print (gttl,json.loads(response.text),f,' cyltime(mS):',round(avg_ct*1e3),round(cycle_time*1e3),r)
                #cv2.waitKey(1000)
            print('Error Time out: %, hit',errCnt/50000*100,errCnt)


if __name__ == '__main__':
    main()




