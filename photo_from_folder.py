import os,shutil
import glob
import data_preprocess as dp
import cv2

def Preprocess_by_photo(Path, Id):
    src_dir = Path
    var = str(Id)
    
    
    if src_dir == './unknownfaces':
        output_datadir = './pre_img'
        output_class_dir = os.path.join(output_datadir, var)
        if not os.path.exists(output_class_dir):
            os.makedirs(output_class_dir)
        for jpgfile in glob.iglob(os.path.join(src_dir,"*.jpg")):            
            img = cv2.imread(jpgfile)
            filename = os.path.splitext(os.path.split(jpgfile)[1])[0]
            dim = (182, 182)
            resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
            FileName =  filename + ".jpg"
            output = os.path.join(output_class_dir, FileName)
            cv2.imwrite(output, resized)        
            os.remove(jpgfile)                         
    
    else:
        output_datadir = './train_img'
        output_class_dir = os.path.join(output_datadir, var)
        if not os.path.exists(output_class_dir):
            os.makedirs(output_class_dir)
        for jpgfile in glob.iglob(os.path.join(src_dir,"*.jpg")):    
            shutil.copy(jpgfile, output_class_dir)
        dp.data_preprocess()
#Preprocess_by_photo('./unknownfaces', "1")



   
    
    