import numpy as np
import cv2

def headPoseEstimation(face_landmarks, face_2d, face_3d, iw, ih):
    for idx, lm in enumerate(face_landmarks.landmark):
        # ---------------------- Get the points of the face -----------------------------
        # if idx == 33 or idx == 263 or idx == 1 or idx == 61 or idx == 291 or idx == 199:
        # # ----------- Draw a line in the nose --------------------
        # nose_2d = (lm.x * iw, lm.y * ih)
        # nose_3d = (lm.x * iw, lm.y * ih, lm.z * 3000)

        # ------------------ Convert to other points ------------------
        x, y = int(lm.x * iw), int(lm.y * ih)

        # -------------- Store it in 2D and 3D ------------------
        face_2d.append([x, y])
        face_3d.append([x, y, lm.z])

    # ------------- Convert it back to NumPy array ------------------
    face_2d = np.array(face_2d, np.float64)
    face_3d = np.array(face_3d, np.float64)

    # ---------------- The camera matrix -------------------
    focal_length = 1 * iw

    cam_matrix = np.array([[focal_length, 0, ih / 2],
                           [0, focal_length, iw / 2],
                           [0, 0, 1]])

    # ---------------- The distortion parameters ----------------
    dist_matrix = np.zeros((4, 1), dtype=np.float64)

    # --------------- Solve PnP -------------------------
    success, rot_vec, trans_vec = cv2.solvePnP(face_3d, face_2d, cam_matrix, dist_matrix)

    # ------------------ Get rotational matrix --------------
    rmat, jac = cv2.Rodrigues(rot_vec)

    # ----------------------- Get angles ----------------------------
    angles, mtxR, mtxQ, Qx, Qy, Qz = cv2.RQDecomp3x3(rmat)

    # --------------------- Get y rotation degrees ------------------
    x = angles[0] * 360
    y = angles[1] * 360
    # z = angles[2] * 360
    return x, y, face_2d, face_3d