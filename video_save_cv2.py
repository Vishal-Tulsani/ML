import cv2
cap=cv2.VideoCapture(0)
video_plugin=cv2.VideoWriter_fourcc(*'XVID')
# XVID plugin .mp4  .avi in some cases .mkv
# now saving video in a file
output=cv2.VideoWriter('Desktop/qwerty.avi',video_plugin,40,(640,480))
#  file name  plugin  FPS   resolution
while cap.isOpened():
    status,frame=cap.read()
    cv2.imshow('live',frame)
    # time for save
    output.write(frame)
    if cv2.waitKey(10) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()
output.release()
cap.release()
    
