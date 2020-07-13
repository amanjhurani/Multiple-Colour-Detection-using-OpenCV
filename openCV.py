import cv2
import numpy as np
#image read and show
# img = cv2.imread("img/hero.jpg")
# cv2.imshow("Output",img)



# cap = cv2.VideoCapture("Aman Jhurani.mp4")
# cap = cv2.VideoCapture(0)
# cap.set(3,640)
# cap.set(4,480)
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video",img)
#     if cv2.waitKey(1) & 0xFF ==ord('q'):
#         break

# kernel = np.ones((5,5),np.uint8)

# img = cv2.imread("img/team-1.jpg")
# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)

# imgCanny = cv2.Canny(img,150,200)  #edge detection
# imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)

# imgErode = cv2.erode(imgDialation,kernel,iterations=1)



# cv2.imshow("Gray Image", imgGray)
# cv2.imshow("Blur Image", imgBlur)
# cv2.imshow("Edge Image", imgCanny)
# cv2.imshow("Dialate Image", imgDialation)
# cv2.imshow("Erode Image", imgErode)

# img = cv2.imread("img/team-1.jpg")
# print(img.shape)

# imgResize = cv2.resize(img,(200,200))

# imgCropped = img[0:200,200:500]

# cv2.imshow("Image",img)
# cv2.imshow("Cropped Image",imgCropped)

# img = np.zeros((512,512,3),np.uint8)
# print(img)
# img[200:300,100:300] = 255,0,0
# cv2.line(img,(0,0),(512,512),(255,0,0),5)
# cv2.rectangle(img,(0,0),(212,212),(255,255,0),cv2.FILLED)

# cv2.imshow("Image",img)


# Wrap prespective

# width, height = 500,350

# img = cv2.imread("img/pers.jpg")
# pts1 = np.float32([[27,166],[189,169],[57,349],[211,312]])
# pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

# matrix = cv2.getPerspectiveTransform(pts1,pts2)
# imageOutput = cv2.warpPerspective(img,matrix,(width,height))


# cv2.imshow("Image",img)
# cv2.imshow("Output Image",imageOutput)





# img = cv2.imread("img/pers.jpg")

# imagehor = np.hstack((img,img))
# imagever = np.vstack((img,img))

# cv2.imshow("Horizontal",imagehor)
# cv2.imshow("Vertical",imagever)

def empty():
    pass

cv2.namedWindow("Trackbars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("Hue Min","Trackbars",0,179,empty)
cv2.createTrackbar("Hue Max","Trackbars",0,179,empty)
cv2.createTrackbar("Sat Min","Trackbars",0,255,empty)
cv2.createTrackbar("Sat Max","Trackbars",0,255,empty)
cv2.createTrackbar("Val Min","Trackbars",0,255,empty)
cv2.createTrackbar("Val Max","Trackbars",0,255,empty)
while True:
    img = cv2.imread("car.jpg")
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min","Trackbars")
    h_max = cv2.getTrackbarPos("Hue Max","Trackbars")
    s_min = cv2.getTrackbarPos("Sat Min","Trackbars")
    s_max = cv2.getTrackbarPos("Sat Max","Trackbars")
    v_min = cv2.getTrackbarPos("Val Min","Trackbars")
    v_max = cv2.getTrackbarPos("Val Max","Trackbars")
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])

    mask = cv2.inRange(imgHSV,lower,upper)
    imgResult = cv2.bitwise_and(img,img,mask=mask)



    # cv2.imshow("Original",img)
    # cv2.imshow("HSV",imgHSV)
    # cv2.imshow("Mask",mask)
    cv2.imshow("Result",imgResult)
    cv2.waitKey(1)