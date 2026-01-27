import cv2
import numpy as np
import time
import os

CAM_INDEX = 0
MIN_MOTION_SECONDS = 5.0
MIN_AREA = 600
SAVE_DIR = "motion_frames"
COOLDOWN_SECONDS = 2.0

GRACE_SECONDS = 1.0   # <- klucz: ile sekund braku ruchu tolerujemy zanim zresetujemy

os.makedirs(SAVE_DIR, exist_ok=True)

cap = cv2.VideoCapture(CAM_INDEX)
if not cap.isOpened():
    raise RuntimeError("Nie mogę otworzyć kamery. Zmień CAM_INDEX (0/1/2) i zamknij apki używające kamery.")

ret, frame = cap.read()
if not ret or frame is None:
    cap.release()
    raise RuntimeError("Nie mogę odczytać klatki z kamery.")

roi = cv2.selectROI("Wybierz ROI i ENTER", frame, showCrosshair=True, fromCenter=False)
cv2.destroyWindow("Wybierz ROI i ENTER")

x, y, w, h = roi
if w == 0 or h == 0:
    cap.release()
    raise RuntimeError("ROI ma zerowy rozmiar.")

fgbg = cv2.createBackgroundSubtractorMOG2(history=300, varThreshold=25, detectShadows=False)

motion_start_time = None
last_motion_time = None      # <- zapamiętujemy kiedy ostatnio był ruch
saved_for_episode = False
last_save = 0.0

print("Start. ESC=wyjście, r=ponowny wybór ROI")

while True:
    ret, frame = cap.read()
    if not ret or frame is None:
        break

    roi_frame = frame[y:y+h, x:x+w]

    fgmask = fgbg.apply(roi_frame)

    fgmask = cv2.GaussianBlur(fgmask, (5, 5), 0)
    _, fgmask = cv2.threshold(fgmask, 200, 255, cv2.THRESH_BINARY)

    kernel = np.ones((5, 5), np.uint8)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel, iterations=1)
    fgmask = cv2.dilate(fgmask, kernel, iterations=2)

    contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    motion = False
    best = None
    best_area = 0

    for c in contours:
        area = cv2.contourArea(c)
        if area < MIN_AREA:
            continue
        motion = True
        rx, ry, rw, rh = cv2.boundingRect(c)
        if area > best_area:
            best_area = area
            best = (rx, ry, rw, rh)

    now = time.time()

    cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 2)

    if motion:
        last_motion_time = now

        if motion_start_time is None:
            motion_start_time = now
            saved_for_episode = False

        elapsed = now - motion_start_time

        if best is not None:
            rx, ry, rw, rh = best
            cv2.rectangle(frame, (x+rx, y+ry), (x+rx+rw, y+ry+rh), (0, 255, 0), 2)

        cv2.putText(frame, f"Ruch: {elapsed:.1f}s / {MIN_MOTION_SECONDS:.1f}s",
                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        if elapsed >= MIN_MOTION_SECONDS and not saved_for_episode and (now - last_save) >= COOLDOWN_SECONDS:
            ts = time.strftime("%Y%m%d_%H%M%S")
            path = os.path.join(SAVE_DIR, f"motion_{ts}.jpg")
            cv2.imwrite(path, frame)
            print("[ZAPIS]", path)
            saved_for_episode = True
            last_save = now

    else:
        # <- zamiast resetować od razu, dajemy "GRACE_SECONDS" na krótkie zaniki
        if motion_start_time is not None:
            # jeśli nigdy nie było ruchu, last_motion_time może być None
            gap = now - (last_motion_time if last_motion_time is not None else motion_start_time)

            cv2.putText(frame, f"Przerwa: {gap:.1f}s / {GRACE_SECONDS:.1f}s",
                        (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

            if gap > GRACE_SECONDS:
                motion_start_time = None
                last_motion_time = None
                saved_for_episode = False

        cv2.putText(frame, "Brak ruchu",
                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)

    cv2.imshow("LIVE - Motion ROI", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == 27:
        break
    elif key == ord('r'):
        roi = cv2.selectROI("Wybierz ROI i ENTER", frame, showCrosshair=True, fromCenter=False)
        cv2.destroyWindow("Wybierz ROI i ENTER")
        x, y, w, h = roi
        if w > 0 and h > 0:
            motion_start_time = None
            last_motion_time = None
            saved_for_episode = False
            fgbg = cv2.createBackgroundSubtractorMOG2(history=300, varThreshold=25, detectShadows=False)

cap.release()
cv2.destroyAllWindows()
