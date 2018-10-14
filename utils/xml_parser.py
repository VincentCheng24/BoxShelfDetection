from xml.etree.ElementTree import ElementTree as ET
from pathlib import Path

xml_dir = 'D:/Misc/mini/labeled_side'
pathlist = Path(xml_dir).glob('*.xml')
# xml_file_path = 'D:/Misc/mini/labeled_side/img0001.xml'

# img_idx = xml_file_path.split('.')[0].split('/')[-1]
# txt_path = 'D:/Misc/mini/label_txt/{}.txt'.format(img_idx)

txt_path = '../dataset/samples_1011.txt'

with open(txt_path, 'a') as t:

    for xml_file_path in pathlist:
        img_path = 'D:/Misc/mini/imges_0975/{}.png'.format(str(xml_file_path).split('.')[0].split('\\')[-1])
        eTree = ET()
        print('Parsing xml file: ', xml_file_path)
        with open(xml_file_path) as f:
            root = eTree.parse(f)

        bboxes = root.findall('.//object')

        for bbox in bboxes:
            xmin = bbox.find('.//xmin').text
            ymin = bbox.find('.//ymin').text
            xmax = bbox.find('.//xmax').text
            ymax = bbox.find('.//ymax').text

            line = '{} {} {} {} {} Box'.format(img_path, xmin, ymin, xmax, ymax)
            t.write(line)
            t.write('\n')


print('well done')

