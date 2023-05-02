import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

class VideoCamera(object):
    def __init__(self):
      self.video = cv2.VideoCapture(0)

    def __del__(self):
      self.video.release()

    def get_frame(self):
      ret, frame = self.video.read()
      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      faces = face_cascade.detectMultiScale(gray, 1.1, 4)
      for (x, y, w, h) in faces:
          cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
      window_name = 'Image'
      font = cv2.FONT_HERSHEY_SIMPLEX
      
      # org
      org = (50, 50)
      
      # fontScale
      fontScale = 1
      
      # Blue color in BGR
      color = (0, 255, 25)
      
      # Line thickness of 2 px
      thickness = 2

      # Using cv2.putText() method
      image = cv2.putText(frame, "My name is {Count}".format(Count = len(faces)), org, font, 
                      fontScale, color, thickness, cv2.LINE_AA)
      
      # Displaying the image
      # cv2.imshow(window_name, image) 
      ret, jpeg = cv2.imencode('.jpg', image)
      return jpeg.tobytes()
