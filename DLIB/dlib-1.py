#/usr/bin/python

import dlib
import cv2
import glob
import numpy as np

class face_recognition:
    '''
    模型路径
    predictor_path = "./face_model/shape_predictor_68_face_landmarks.dat"
    face_rec_model_path = "./face_model/dlib_face_recognition_resnet_model_v1.dat"

    # 调用注意事项，因为模型底层是外国人写的。所以路径图片名字千万别使用中文，这样它直接找不到
    好像是OpenCV的问题吧，一直没有解决。中文他会乱码。真的坑。
    '''

    def __init__(self,predictor_path,face_rec_model_path):
        self.predictor_path = predictor_path
        self.face_rec_model_path = face_rec_model_path
        self.detector = dlib.get_frontal_face_detector()
        self.shape_predictor = dlib.shape_predictor(self.predictor_path)
        self.face_rec_model = dlib.face_recognition_model_v1(self.face_rec_model_path)

    def face_detection(self,url_img_1,url_img_2):
        img_path_list = [url_img_1,url_img_2]
        dist = []
        for img_path in img_path_list:
            img = cv2.imread(img_path)
            # 转换rgb顺序的颜色。
            b, g, r = cv2.split(img)
            img2 = cv2.merge([r, g, b])
            # 检测人脸
            faces = self.detector(img, 1)
            if len(faces):
                for index, face in enumerate(faces):
                    # # 提取68个特征点
                    shape = self.shape_predictor(img2, face)
                    # 计算人脸的128维的向量
                    face_descriptor = self.face_rec_model.compute_face_descriptor(img2, shape)

                    dist.append(list(face_descriptor))
            else:
                pass
        return dist

    # 欧式距离
    def dist_o(self,dist_1,dist_2):
        dis = np.sqrt(sum((np.array(dist_1)-np.array(dist_2))**2))
        return dis

    def score(self,url_img_1,url_img_2):
        url_img_1 = glob.glob(url_img_1)[0]
        url_img_2 = glob.glob(url_img_2)[0]
        data = self.face_detection(url_img_1,url_img_2)
        goal = self.dist_o(data[0],data[1])
        # 判断结果，如果goal小于0.6的话是同一个人，否则不是。我所用的是欧式距离判别
        return 1-goal


predictor_path = "/home/lzq/python_project/python_book_code/DLIB/dat/shape_predictor_68_face_landmarks.dat"
face_rec_model_path = "/home/lzq/python_project/python_book_code/DLIB/dat/dlib_face_recognition_resnet_model_v1.dat"
face_ = face_recognition(predictor_path,face_rec_model_path)
# img_1 = './faces/User.1.4.jpg'
# img_2 = './faces/User.1.46.jpg'
img_1 = '/home/lzq/python_project/python_book_code/DLIB/face/jj1.jpg'
img_2 = '/home/lzq/python_project/python_book_code/DLIB/face/jj2.jpg'
goal = face_.score(img_1,img_2)
print(goal)