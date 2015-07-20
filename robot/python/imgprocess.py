import cv2
import numpy as np

def test(img):
    print "your ", img
     #time.sleep(5)

def harris(img):
    gray = np.float32(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))
    dst = cv2.cornerHarris(gray, 2,3,0.04)
    dst = cv2.dilate(dst,None)
    img[dst>0.01*dst.max()]=[0,0,255]
    return img

def shitomasi(img):
    gray = np.float32(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))
    corners = cv2.goodFeaturesToTrack(gray,25,0.01,10)
    corners = np.int0(corners)
    rows,cols,channels = img.shape

    for c in corners:
        x,y = c.ravel()
        cv2.circle(img,(x,y),3,255,-1)
    return img

def sift(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    sift=cv2.SIFT()
    kp = sift.detect(gray, None)
    img2=cv2.drawKeypoints(gray,kp,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    #kp,des = sift.detectAndCompute(img, None)
    return img2

def surf(img):
    surf=cv2.SURF()
    kp, des = surf.detectAndCompute(img, None)
    img1=cv2.drawKeypoints(img, kp, None, (255,0,0),4)
    return img1

def fast(img):
    fast = cv2.FastFeatureDetector()
    kp = fast.detect(img,None)
    img2 = cv2.drawKeypoints(img, kp, color=(255,0,0))
    return img2

def brief(img):
    star = cv2.FeatureDetector_create("STAR")
    brief = cv2.DescriptorExtractor_create("BRIEF")
    kp = star.detect(img,None)
    kp, des = brief.compute(img, kp)
    img2 = cv2.drawKeypoints(img, kp, color=(255,0,0))
    return img2

def orb(img):
    orb = cv2.ORB()
    kp = orb.detect(img,None)
    kp, des = orb.compute(img, kp)
    img2 = cv2.drawKeypoints(img,kp,color=(0,255,0), flags=0)
    return img2

def findContours(img):
    imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(imgray,127,255,0)
    image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) 
    return image, contours, hierarchy

def cannyEdge(img):
    return cv2.Canny(img,100,200)

def findContours(img):
    imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(imgray,127,255,0)
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    return contours

def drawContours(img):
    contours = findContours(img)
    cv2.drawContours(img, contours, -1, (0,255,0), 3)
    return img
