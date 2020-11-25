time.sleep(0.5)                                  
# orb-1 initialization
orb = cv2.ORB_create()
-small_image = cv2.resize(image,dsize=(480,360) )

#orb-2 convert to gray scale
gray = cv2.cvtcolor(small_image,cv2.COLOR_BGR2GRAY)
gray = cv2.equalizeHist( gray )

# orb-3 detect & compute orb
Kp, des = orb.detectAndCompute(gray,None)

# orb-4 draw keypoints
small_image = cv2.drawKeypoints(gray, kp, None,(255,0,0), flags=0) 