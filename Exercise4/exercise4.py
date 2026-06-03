import cv2

video_path = "samples_data_vtest.avi"

cap = cv2.VideoCapture(video_path)

fps = cap.get(cv2.CAP_PROP_FPS)

print("FPS:", fps)

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

    cv2.putText(
        left_frame,
        "LEFT",
        (50, 100),
        cv2.FONT_HERSHEY_SIMPLEX,
        2,
        (0, 255, 0),
        3
    )

    cv2.putText(
        right_frame,
        "RIGHT",
        (50, 100),
        cv2.FONT_HERSHEY_SIMPLEX,
        2,
        (0, 0, 255),
        3
    )

    combined_frame = cv2.hconcat(
        [left_frame, right_frame]
    )

    print(combined_frame.shape)

    cv2.imshow(
        "Side By Side Video",
        combined_frame
    )

    out.write(combined_frame)

    if cv2.getWindowProperty(
        "Side By Side Video",
        cv2.WND_PROP_VISIBLE
    ) < 1:
        break

    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()