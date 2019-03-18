try:
    from PIL import Image, ImageEnhance
except ImportError:
    import Image
import pytesseract
import numpy as np


def digit_ocr(img_name, img, boxes, class_mapping):

    # img_path = './images/train_set/img0001.png'
    # img = Image.open(img_path)
    #
    # boxes = np.load('boxes.npy').item()

    # class_mapping = np.load('class_mapping.npy').item()
    img = Image.fromarray(img)

    line =[img_name]

    try:
        digit_boxes = boxes[[key for key, value in class_mapping.items() if value == 'Digit'][0]]
    except Exception as e:
        if e == 'KeyError: 0':
            pass
    else:

        config = '--psm 13 --oem 3 -c tessedit_char_whitelist="0123456789"'

        for i, digit_box in enumerate(digit_boxes):
            # digit_box[1] += 30
            img = img.crop(tuple(digit_box[:-1]))
            result_path = './images/res_img/0318/{}_{}_pre.png'.format(img_name, i)
            img.save(result_path)

            img = img.convert('L')
            img = ImageEnhance.Brightness(img).enhance(0.1)
            img = ImageEnhance.Contrast(img).enhance(2.0)
            img = ImageEnhance.Contrast(img).enhance(4.0)
            img = ImageEnhance.Brightness(img).enhance(0.2)
            img = ImageEnhance.Contrast(img).enhance(10.0)
            result_path = './images/res_img/0318/{}_{}_pos.png'.format(img_name, i)
            img.save(result_path)

            # img.show()
            res = pytesseract.image_to_string(img, config=config)
            line.append(res)

            print(pytesseract.image_to_string(img, config=config))

            print('well')

        line.append('\n')
        with open('res.txt', 'a') as f:
            line = ', '.join(line)
            f.write(line)

"""
# test = False
test = True

if test:
    img_path = './images/train_set/img0001.png'
    img = Image.open(img_path)

    boxes = np.load('boxes.npy').item()

    class_mapping = np.load('class_mapping.npy').item()

    digit_boxes = boxes[[key for key, value in class_mapping.items() if value == 'Digit'][0]]

    # config = '--classify_bln_numeric_mode True'

    config = '--psm 13 --oem 3 -c tessedit_char_whitelist="0123456789"'

    for digit_box in digit_boxes:
        digit_box[1] += 30

        img = img.crop(tuple(digit_box[:-1])).convert('L')
        img = ImageEnhance.Brightness(img).enhance(0.1)
        img = ImageEnhance.Contrast(img).enhance(2.0)
        img = ImageEnhance.Contrast(img).enhance(4.0)
        img = ImageEnhance.Brightness(img).enhance(0.2)
        img = ImageEnhance.Contrast(img).enhance(10.0)

        img.show()

        print(pytesseract.image_to_string(img, config=config))

        print('well')

else:
    img_path = '111.jpg'
    img = Image.open(img_path).convert('L')
    img = ImageEnhance.Brightness(img).enhance(0.1)
    img = ImageEnhance.Contrast(img).enhance(2.0)
    img = ImageEnhance.Contrast(img).enhance(4.0)
    img = ImageEnhance.Brightness(img).enhance(0.2)
    img = ImageEnhance.Contrast(img).enhance(16.0)

    # img.show()
    config = '--psm 13 --oem 3 -c tessedit_char_whitelist="0123456789"'
    # config = '-outputbase digits'
    print(pytesseract.image_to_string(img, lang='eng', config=config))

"""

