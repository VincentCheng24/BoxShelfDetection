import glob
import shutil
ori_img_dir = '../image_data/img_V2'
save_img_dir = '../images/train_set/'

for file in glob.glob(ori_img_dir + '/*.png'):
    if file.endswith('1.png') or file.endswith('6.png'):
        shutil.copy(file, save_img_dir)
        print(file)

    print('well')
