#/usr/bin/python
#coding=utf-8

from DLIB.face_recognition import face_recognition


predictor_path = "/home/lzq/python_project/python_book_code/DLIB/dat/shape_predictor_68_face_landmarks.dat"
face_rec_model_path = "/home/lzq/python_project/python_book_code/DLIB/dat/dlib_face_recognition_resnet_model_v1.dat"
face_ = face_recognition(predictor_path,face_rec_model_path)
img_1 = '/home/lzq/python_project/python_book_code/DLIB/face/jj1.jpg'
img_2 = '/home/lzq/python_project/python_book_code/DLIB/face/jj2.jpg'
goal = face_.score(img_1,img_2)
print(goal)