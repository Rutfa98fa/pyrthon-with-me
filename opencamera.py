import cv2
import datetime
cap= cv2.VideoCapture(0)

while (True):
    ##ref รับค่าจากกล้องการเช็ค ถ้า ref เป็นจริงจะได้ frame
    ref , frame = cap.read() ##รับภาพจากกล้องเฟรมต่อเฟรม
    if ref == True:
        ##แแสดงเวลาเรียลไทม์
        currentDate = str(datetime.datetime.now())
        cv2.putText(frame,currentDate,(10,30),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),cv2.LINE_4)
        cv2.imshow("output",frame)
        

        if cv2.waitKey(1) & 0xFF == ord("e"): ##ให้รอรับคีย์ 
            break

cap.release()
cv2.destroyAllWindows()

