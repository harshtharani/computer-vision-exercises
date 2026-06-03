import cv2

video_path = "samples_data_vtest.avi"

cap = cv2.VideoCapture(video_path)

fps = cap.get(cv2.CAP_PROP_FPS)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

duration = total_frames / fps

print("FPS:", fps)
print("Total Frames:", total_frames)
print("Duration:", duration, "seconds")

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'XVID')

out = cv2.VideoWriter(
    "Outputs/sample_10s.avi",
    fourcc,
    fps,
    (width, height)
)

frame_count = 0
max_frames = int(fps * 10)

delay = int(1000 / fps)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    elapsed_time = frame_count / fps
    remaining_time = duration - elapsed_time

    cv2.putText(
        frame,
        f"Elapsed: {elapsed_time:.1f}s",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.putText(
        frame,
        f"Remaining: {remaining_time:.1f}s",
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2
    )

    cv2.imshow("Video Playback", frame)

    if frame_count < max_frames:
        out.write(frame)

    frame_count += 1

    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

cap.release()
out.release()

cv2.destroyAllWindows()