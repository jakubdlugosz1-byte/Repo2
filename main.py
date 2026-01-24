import cv2
import requests
import numpy as np
import os
from ultralytics import YOLO

print("Ładowanie modelu YOLOv8...")
model = YOLO("yolov8n.pt")

def count_people_clean(source_path):
    image = None
    source_path = source_path.strip('"').strip("'")

    if source_path.startswith("http"):
        print(f"Pobieranie z URL: {source_path}")
        try:
            resp = requests.get(source_path, stream=True, timeout=10)
            resp.raise_for_status()
            arr = np.asarray(bytearray(resp.content), dtype=np.uint8)
            image = cv2.imdecode(arr, -1)
        except Exception as e:
            print(f"Błąd pobierania: {e}")
            return
    else:
        if os.path.exists(source_path):
            image = cv2.imread(source_path)
        else:
            print("Błąd: Taki plik nie istnieje!")
            return

    if image is None:
        print("Błąd obrazu.")
        return

    results = model(image, classes=[0], verbose=False)
    
    people_count = len(results[0].boxes)
    
    print(f"\n---> ZNALEZIONO OSÓB: {people_count} <---\n")

    height, width = image.shape[:2]
    if width > 1400 or height > 900:
        scale = 0.5
        image = cv2.resize(image, None, fx=scale, fy=scale)

    tytul_okna = f"WYNIK: {people_count} osob"
    
    cv2.imshow(tytul_okna, image)
    
    cv2.waitKey(0) 
    cv2.destroyAllWindows()


#link = "C:/Users/kubak/Downloads/images.jpg"
link = "https://reads.pl/wp-content/uploads/2025/05/NgKvu8G2coskQXj74MoKcE.jpg"
count_people_clean(link)