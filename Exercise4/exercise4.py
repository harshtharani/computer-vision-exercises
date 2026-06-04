import cv2

video_path = "samples_data_vtest.avi"

cap = cv2.VideoCapture(video_path)

fps = cap.get(cv2.CAP_PROP_FPS)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

print("FPS:", fps)
print("Total Frames:", total_frames)

fourcc = cv2.VideoWriter_fourcc(*'XVID')

out = cv2.VideoWriter(
    "Outputs/side_by_side_1080p.avi",
    fourcc,
    fps,
    (1920, 1080)
)

delay = int(1000 / fps)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    left_frame = cv2.resize(frame, (960, 1080))
    right_frame = cv2.resize(frame, (960, 1080))

    combined_frame = cv2.hconcat(
        [left_frame, right_frame]
    )

    cv2.imshow(
        "Side By Side Video",
        combined_frame
    )

    out.write(combined_frame)

    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

print("Video saved successfully")