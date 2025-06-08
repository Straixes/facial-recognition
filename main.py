import cv2
import os

# initialiser notre webcam
cap = cv2.VideoCapture(0)
# charger notre modele, mettez le bon chemin
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#print(os.getcwd())
font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    # lire notre frame (image)
    _, image = cap.read()
    # convertir l'image en noir et blanc
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # detecter tous les visages présents
    faces = face_cascade.detectMultiScale(image_gray, 1.1, 5)
    # tracer un rectangle pour chaque visage
    for x, y, width, height in faces:
        cv2.rectangle(image, (x, y), (x + width, y + height), color=(255, 0, 0), thickness=2)
    
    # ecrire sur l'image le nombre de visages detectes
    cv2.putText(frame,'Visage detectes : ' + str(len(faces)),(40, 40), font, 1,(255,0,0),2)
    cv2.imshow("image", image)
   # afficher le rendu de la webcam et appuyez sur 'q' pour quitter
    if cv2.waitKey(1) == ord("q"):
        break

# detruire toutes les fenetres après avoir quitté le programme
cap.release()
cv2.destroyAllWindows()