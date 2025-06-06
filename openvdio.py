import cv2

cap= cv2.VideoCapture("image/Video.mp4",  cv2.CAP_FFMPEG)

while (cap.isOpened): ##เช็ควิดีโอพร้อมยัง ถ้าค่า frame none ref false
    ##ref รับค่าจากกล้องการเช็ค ถ้า ref เป็นจริงจะได้ frame
    ref , frame = cap.read() ##รับภาพจากกล้องเฟรมต่อเฟรม
    if ref == True: ##ถ้่า ref เป็นจริงจะรันวิดีโอต่อ
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) ##แปลงค่าสีเป็น grey scale กำหนดตัวแปร gray 
        cv2.imshow("output",gray)
        if cv2.waitKey(1) & 0xFF == ord("e"): ##ให้รอรับคีย์ 
            break

    else :
        break ##ถ้าหากไม่การกด e จะ break loop
cap.release()
cv2.destroyAllWindows()