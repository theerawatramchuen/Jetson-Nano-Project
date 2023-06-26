import cv2 as cv
import numpy as np
from pyueye import ueye
import sys


class UeyeCamera:
    def __init__(self):
        self.hCam = ueye.HIDS(0)             #0: first available camera;  1-254: The camera with the specified camera ID
        self.sInfo = ueye.SENSORINFO()
        self.cInfo = ueye.CAMINFO()
        self.pcImageMemory = ueye.c_mem_p()
        self.MemID = ueye.int()
        self.rectAOI = ueye.IS_RECT()
        self.pitch = ueye.INT()
        self.nBitsPerPixel = ueye.INT(24)    #24: bits per pixel for color mode; take 8 bits per pixel for monochrome
        self.channels = 3                    #3: channels for color mode(RGB); take 1 channel for monochrome
        self.m_nColorMode = ueye.INT()		# Y8/RGB16/RGB24/REG32
        self.bytes_per_pixel = int(self.nBitsPerPixel / 8)
        self.hCamConnected = False
        self.x = 0
        self.y = 0
        self.img_buffers = []
        self.bufferCount = 100

    
    def connection(self,width,height):
        try:
            self.nRet = ueye.is_InitCamera(self.hCam, None)
            if self.nRet != ueye.IS_SUCCESS:
                return False
            self.nRet = ueye.is_GetCameraInfo(self.hCam, self.cInfo)
            if self.nRet != ueye.IS_SUCCESS:
                return False
            self.nRet = ueye.is_GetSensorInfo(self.hCam, self.sInfo)
            if self.nRet != ueye.IS_SUCCESS:
                return False
            self.nRet = ueye.is_ResetToDefault(self.hCam)
            if self.nRet != ueye.IS_SUCCESS:
                return False
            self.nRet = ueye.is_SetDisplayMode(self.hCam, ueye.IS_SET_DM_DIB)
            self.colorCameraModel()
            self.width, self.height = self.setAOIimage(self.x,self.y,width,height)
            if self.width == None or self.height == None:
                return False
            self.nRet = ueye.is_CaptureVideo(self.hCam, ueye.IS_DONT_WAIT)
            if self.nRet != ueye.IS_SUCCESS:
                return False
            self.nRet = ueye.is_InquireImageMem(self.hCam, self.pcImageMemory, self.MemID, self.width, self.height, self.nBitsPerPixel, self.pitch)
            if self.nRet != ueye.IS_SUCCESS:
                return False
            else:
                return True
        except Exception as ex:
            print(ex)
            return False

    def colorCameraModel(self):  
        if int.from_bytes(self.sInfo.nColorMode.value, byteorder='big') == ueye.IS_COLORMODE_CBYCRY:
                self.m_nColorMode = ueye.IS_CM_BGRA8_PACKED
                self.nBitsPerPixel = ueye.INT(32)
                self.bytes_per_pixel = int(self.nBitsPerPixel / 8)
        else:
                self.m_nColorMode = ueye.IS_CM_MONO8
                self.nBitsPerPixel = ueye.INT(8)
                self.bytes_per_pixel = int(self.nBitsPerPixel / 8)
    
    def setAOIimage(self,x,y,w,h):
        self.nRet = ueye.is_AOI(self.hCam, ueye.IS_AOI_IMAGE_GET_AOI, self.rectAOI, ueye.sizeof(self.rectAOI))
        if self.nRet != ueye.IS_SUCCESS:
            return None,None
        self.rectAOI.s32X = ueye.int(x)
        self.rectAOI.s32Y = ueye.int(y)
        self.rectAOI.s32Width = ueye.int(w)
        self.rectAOI.s32Height = ueye.int(h)
        nRet = ueye.is_AOI(self.hCam, ueye.IS_AOI_IMAGE_SET_AOI, self.rectAOI, ueye.sizeof(self.rectAOI))
        if nRet != ueye.IS_SUCCESS:
            return None,None                                                          
        width = self.rectAOI.s32Width
        height = self.rectAOI.s32Height
        nRet = ueye.is_AllocImageMem(self.hCam, width, height, self.nBitsPerPixel, self.pcImageMemory, self.MemID)
        if nRet != ueye.IS_SUCCESS:
            return None,None
        else:           
            nRet = ueye.is_SetImageMem(self.hCam, self.pcImageMemory, self.MemID)
            if nRet != ueye.IS_SUCCESS:
                return None,None
            else:
                nRet = ueye.is_SetColorMode(self.hCam, self.m_nColorMode)
        return width,height
    
    def check(self,code):
        if code != ueye.IS_SUCCESS:
            return False
        return True
    
    def clearBuffer(self):
        ueye.is_ClearSequence(self.hCam)
    #     ueye.is_FreezeVideo (cam, ctypes.c_int(0x0000))  #IS_DONT_WAIT  = 0x0000, or IS_GET_LIVE = 0x8000
    #     ueye.is_CopyImageMem (cam, self.pcImageMemory, pid, ImageData.ctypes.data)


    def clearMemory(self):
        ueye.is_FreeImageMem(self.hCam, self.pcImageMemory, self.MemID)

    def disconnect(self):
        if self.hCamConnected == True:
            ueye.is_FreeImageMem(self.hCam, self.pcImageMemory, self.MemID)
            ueye.is_ExitCamera(self.hCam)

if __name__ == '__main__':
    cam = UeyeCamera()
    camconnect = cam.connection(1920,1080)
    print("connection ",camconnect)
    if(camconnect):
        while(cam.nRet == ueye.IS_SUCCESS):

            # Retrieve and discard frames to clear the memory buffer
            for _ in range(cam.bufferCount):
                array = ueye.get_data(cam.pcImageMemory, cam.width, cam.height, cam.nBitsPerPixel, cam.pitch, copy=False)
        
            frame = np.reshape(array,(cam.height.value, cam.width.value, cam.bytes_per_pixel))
            frame = cv.cvtColor(frame,cv.COLOR_BGRA2BGR,frame,3)

            cv.imshow("frame", frame)

            # filename = 'testsave.jpg'
            # cv.imwrite(filename,frame)

            if (cv.waitKey(1) == ord("q")):
                break
        cam.disconnect()
        cv.destroyAllWindows()


