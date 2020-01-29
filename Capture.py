import cv2, os, numpy as np, time
cap = cv2.VideoCapture(0)
path = './images/'
h = s = p = e = 0
while True:
	_, frame = cap.read()
	timestamp = str(round(time.time(),2))
	key = cv2.waitKey(1) & 0xFF
    	# Press q if you want to end the loop
	if key == ord('q'): break
	if key == ord('a'):  cv2.imwrite(path + 'a_' + timestamp + '.jpg', frame)
	if key == ord('b'):  cv2.imwrite(path + 'b_' + timestamp + '.jpg', frame)
	if key == ord('c'):  cv2.imwrite(path + 'c_' + timestamp + '.jpg', frame)
	if key == ord('d'):  cv2.imwrite(path + 'd_' + timestamp + '.jpg', frame)
	if key == ord('e'):  cv2.imwrite(path + 'e_' + timestamp + '.jpg', frame)
	if key == ord('f'):  cv2.imwrite(path + 'f_' + timestamp + '.jpg', frame)
	if key == ord('g'):  cv2.imwrite(path + 'g_' + timestamp + '.jpg', frame)
	if key == ord('h'):  cv2.imwrite(path + 'h_' + timestamp + '.jpg', frame)
	cv2.imshow('Hit q to Exit',frame)



