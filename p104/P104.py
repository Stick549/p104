import cv2
img  = cv2.imread("solar-system.jpg")
cv2.putText(img,"sun",(20,300), cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Mercury",(100,300), cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"Venus",(200,200), cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"earth",(300,300), cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"mars",(400,200), cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"jupiter",(500,300), cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"saturn",(700,200), cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"uranus",(1000,300), cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,"netpune",(1100,200), cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.imshow("output", img)
cv2.waitKey(0)