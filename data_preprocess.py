from preprocess import preprocesses
import shutil
import os
def data_preprocess():
    input_datadir = './train_img'
    output_datadir = './pre_img'

    obj = preprocesses(input_datadir,output_datadir)
    nrof_images_total,nrof_successfully_aligned = obj.collect_data()
#    print('Total number of images: %d' % nrof_images_total)
    for dirname in os.listdir(input_datadir)  :
        shutil.rmtree(input_datadir + "/" + dirname)
        

    print('Number of successfully aligned images: %d' % nrof_successfully_aligned)

#data_preprocess()
