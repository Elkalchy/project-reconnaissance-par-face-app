import cv2
import json

def start_recognition(face_name):
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer.yml')
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    font = cv2.FONT_HERSHEY_SIMPLEX

    with open('names.json', 'r') as fs:
        names = json.load(fs)
        names = list(names.values())

    cam = cv2.VideoCapture(0)
    cam.set(3, 640)
    cam.set(4, 480)

    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)

    while True:
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(int(minW), int(minH)))

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            id, confidence = recognizer.predict(gray[y:y + h, x:x + w])

            if confidence > 20:
                name = names[id] if id < len(names) else "Who are you?"
                confidence_text = f"{round(confidence)}%"

                # Compare detected name with entered name
                if name.lower() == face_name.lower():
                    cv2.putText(img, "This is a criminal!", (x, y - 20), font, 1, (0, 0, 255), 2)
                else:
                    cv2.putText(img, name, (x + 5, y - 5), font, 1, (255, 255, 255), 2)
            else:
                name = "Who are you?"
                confidence_text = "N/A"
                cv2.putText(img, name, (x + 5, y - 5), font, 1, (255, 255, 255), 2)

            cv2.putText(img, confidence_text, (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

        cv2.imshow('camera', img)

        k = cv2.waitKey(10) & 0xff
        if k == 27:  # Escape key
            break

    print("Exiting Program.")
    cam.release()
    cv2.destroyAllWindows()
