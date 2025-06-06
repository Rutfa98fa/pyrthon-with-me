import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID') ##อัดวิดีโอ

result = cv2.VideoWriter("output.mp4", fourcc,20.0,(640,480)) 

while (cap.isOpened): ##เช็ควิดีโอพร้อมยัง ถ้าค่า frame none ref false
    ##ref รับค่าจากกล้องจากการเช็ค ถ้า ref เป็น True จะได้ frame
    ref , frame = cap.read() ##รับภาพจากกล้อง Frame/Frame
    if ref == True: ##ถ้่า ref True จะรันวิดีโอต่อ
        cv2.imshow("output",frame)
        result.write(frame) ##รับค่าแต่ล่ะ frame ที่อ่านมาจากกล้่อง
        if cv2.waitKey(1) & 0xFF == ord("e"): ##ให้รอรับคีย์ e เพื่อ break loop
            break

result.release()
cap.release()
cv2.destroyAllWindows()