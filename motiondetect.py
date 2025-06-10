import cv2
cap = cv2.VideoCapture("image/Walking.mp4")

check , frame1 = cap.read() #หาเส้นคอนทัวร์แรก
check , frame2 = cap.read()##หาเส้นคอนทัวร์ตัวถัดไป

while (cap.isOpened()):
   
    if check:
        motiondiff = cv2.absdiff(frame1,frame2) #ตรวจจับการเคลื่อนไหว
        gray = cv2.cvtColor(motiondiff,cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray,(5,5),0) ##มีการเคลื่อนที่ของวัตถุ frame1 frame2
        
        thresh , result = cv2.threshold(blur,15,255,cv2.THRESH_BINARY)
        diration = cv2.dilate(result,None,iterations=3) ##ขยายภาพคนในวิดีโอ
        contours , hierachy = cv2.findContours(diration,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
        cv2.drawContours(frame1,contours,-1,(0,255,0),2) #แสดงคอนทัวร์ใน เฟรม1
        cv2.imshow("output",frame1)
        frame1=frame2 ##ให้ไปที่เฟรมถัดไปวาดไปเรื่อยๆ
        check,frame2 = cap.read() ##เปลี่ยนค่าเฟรม2 ให้อ่านเฟรมถัดไป
        if cv2.waitKey(1) & 0xFF == ord("e"):
            break

    else :
        break

cap.release()
cv2.destroyAllWindows()    