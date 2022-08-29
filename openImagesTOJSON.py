from PIL import Image
import os
import xml.etree.ElementTree as gfg
import pandas as pd
import cv2
import time

print("START")
my_classes = ["Apple","Mug","Tin can"]

my_classes_counters = [["Apple",0],["Mug",0],["Tin can",0]]

directory = "C:/Users/paperspace/fiftyone/open-images-v6/train/data"
counter = 0


def loadCSVS():

    t1 = time.time()
    #first get the detections from openimages
    detections = pd.read_csv("C:/Users/paperspace/fiftyone/open-images-v6/train/labels/detections.csv")

    count_row = detections.shape[0]  # Gives number of rows
    count_col = detections.shape[1]  # Gives number of columns

    print(count_row)
    print(count_col)

    #get the classes from openimages
    classes =  pd.read_csv("C:/Users/paperspace/fiftyone/open-images-v6/train/metadata/classes.csv")
    classes.columns =['code', 'name']

    count_row_classes = classes.shape[0]  # Gives number of rows
    count_col_classes = classes.shape[1]  # Gives number of columns

    print(count_row_classes)
    print(count_col_classes)

    t2 = time.time()
    print('Time {} seconds'.format( t2 - t1))

    return detections,classes

detections, classes = loadCSVS()

def GenerateXML(filename,img):

    global counter   
    root = gfg.Element("annotation")
      
    _folder = gfg.SubElement(root, "folder")
    _folder.text = "data"
   
    _filename = gfg.SubElement(root,"filename")
    _filename.text = filename
   
    _path = gfg.SubElement(root,"path")
    _path.text = directory+"/"+filename
  
    _source = gfg.SubElement(root,"source")
    _database = gfg.SubElement(_source,"source")
    _database.text = "Unknown"
    
    height, width, channels = img.shape
     
    _size = gfg.SubElement(root,"size")
    _width = gfg.SubElement(_size,"width")
    _width.text = str(width)
    _height = gfg.SubElement(_size,"height")
    _height.text = str(height)
    _depth = gfg.SubElement(_size,"depth")
    _depth.text = str(channels)
    
    _segmented = gfg.SubElement(root,"segmented")
    _segmented.text = "0"
    
    #now start searching for the image in the detections (might be more than one)
    subsetdetections = detections.loc[detections['ImageID'] == os.path.splitext(filename)[0]]

    classes_to_chceck = []
    for cls in my_classes:
        my_struct = [cls,False]
        classes_to_chceck.append(my_struct)
   
    for index, row in subsetdetections.iterrows():
       
        image = row['ImageID']
        labelname = classes.loc[classes['code'] == row['LabelName']].iat[0,1]
        #print(image,labelname)
        #now for this image we have to search for only one occurance of any of our classes

        for x in range(len(classes_to_chceck)):
            if classes_to_chceck[x][0] == labelname:
                if classes_to_chceck[x][1] == False:
                    classes_to_chceck[x][1] = True
                    #print(classes_to_chceck[x]) 
                    
                    #update counters
                    my_classes_counters[x][1] = my_classes_counters[x][1]+1

                    #if classes_to_chceck[x][0] == "Apple":
                    #    apple_counter = apple_counter+1
                    #if classes_to_chceck[x][0] == "Mug":
                    #   mug_counter = mug_counter+1
                    #if classes_to_chceck[x][0] == "Tin can":
                    #   tin_can_counter = tin_can_counter+1

                    #get the bounding box detections
                    perc_xmin = float(width)*float(row['XMin'])
                    perc_xmax = float(width)*float(row['XMax'])
                    perc_ymin = float(height)*float(row['YMin'])
                    perc_ymax = float(height)*float(row['YMax'])
                
                    #cv2.rectangle(img, (int(perc_xmin),int(perc_ymin)),(int(perc_xmax),int(perc_ymax)), (255,0,0), 2)
                    #img_r = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # Converting BGR to RGB
                    #cv2.imshow("result", img_r)
                    _object = gfg.SubElement(root,"object")
                    _name = gfg.SubElement(_object,"name")
                    _name.text = labelname
                    _pose = gfg.SubElement(_object,"pose")
                    _pose.text = "Unspecified"
                    _truncated = gfg.SubElement(_object,"truncated")
                    _truncated.text = "0"
                    _difficult = gfg.SubElement(_object,"difficult")
                    _difficult.text = "0"
                    _bndbox = gfg.SubElement(_object,"bndbox")
                    _xmin =  gfg.SubElement(_bndbox,"xmin")
                    _ymin =  gfg.SubElement(_bndbox,"ymin")
                    _xmax =  gfg.SubElement(_bndbox,"xmax")
                    _ymax =  gfg.SubElement(_bndbox,"ymax")
                    _xmin.text = str(int(perc_xmin))
                    _ymin.text = str(int(perc_ymin))
                    _xmax.text = str(int(perc_xmax))
                    _ymax.text = str(int(perc_ymax))
                
    tree = gfg.ElementTree(root)
    with open (directory+"/"+os.path.splitext(filename)[0]+'.xml' , "wb") as files :
        tree.write(files)

def process_images(folder):    
    global counter 
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            #height, width, channels = img.shape
            #print(height,width)
            GenerateXML(filename,img)
            print("**********************************")
            for x in range(len(my_classes_counters)):
                print(my_classes_counters[x][0],my_classes_counters[x][1])

            counter = counter+1
            print(counter)
    
process_images(directory)


# classes_to_chceck = []
# for cls in my_classes:
#     my_struct = [cls,False]
#     classes_to_chceck.append(my_struct)

# lablenames = ["Apple", "daadad","ddadasd","Tin can", "Apple","Mug","Mug","asadasd","Tin can"]


# for labelname in lablenames:
#     for x in range(len(classes_to_chceck)):
#         if classes_to_chceck[x][0] == labelname:
#             if classes_to_chceck[x][1] == False:
#                 classes_to_chceck[x][1] = True
#                 print(classes_to_chceck[x]) 