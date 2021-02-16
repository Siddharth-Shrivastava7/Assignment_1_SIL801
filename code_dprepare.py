from PIL import Image
import os

save_root = './data_folder'
src_root = './dataset'
bbox1 = (1,1,31,31)  # converting 32*32 into 30*30 image ... if req then do this also

text = open('groundTruthValues.txt')
lines = text.readlines()
index = 0 

for linenumber, line in enumerate(lines[1:]):
    img_name = line.split(',')[0]
    str_gt = line.split(',')[1].split('\n')[0]
    img = Image.open(os.path.join(src_root, img_name + '.png'))
    linenumber = linenumber % 16 #16 because number of lines per image to read
    if (linenumber == 0 ): 
        index = index + 1 
    for column_number,gt in enumerate(str_gt):
        bbox = (32*column_number, 32*linenumber, 32*(column_number+1), 32*(linenumber+1))
        img_c = img.crop(bbox) # 32*32 
        img_cc = img_c.crop(bbox1) # 30*30 
        img_cc.save(os.path.join(save_root, gt, str(linenumber) + '_' + str(column_number) +  '_' + str(index) + '.png'))