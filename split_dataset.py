import os
import subprocess
import shutil
import random
import numpy as np
source_directory = "./dataset_balanced"
target_directory = "./dataset_split"

def splitDataset():
    global source_directory
    global target_directory

    if not os.path.exists(target_directory):
      
        os.mkdir(target_directory)
        _train = os.path.join(target_directory, "train")
        _valid = os.path.join(target_directory, "valid")

        os.mkdir(_train)
        os.mkdir(_valid)

        folders = os.listdir(source_directory)
        for folder in folders:
            _foldertrain = os.path.join(_train, folder)
            _foldervalid = os.path.join(_valid, folder)

            os.mkdir(_foldertrain)
            os.mkdir(_foldervalid)
    
    
    path_train = os.path.join(target_directory, "train")
    path_valid = os.path.join(target_directory, "valid")
    
    folders = os.listdir(source_directory)
    for folder in folders:
        full_folder_path = os.path.join(source_directory,folder)
        source_files = os.listdir(full_folder_path)
        for _file in source_files:
            sourcefile = os.path.join(full_folder_path,_file)

            if np.random.rand(1) < 0.2:
                targetfile = os.path.join(path_valid,folder,_file)
                shutil.copy(sourcefile, targetfile)  
            else:
                targetfile = os.path.join(path_train,folder,_file)
                shutil.copy(sourcefile, targetfile)
                
        
    # folders = os.listdir(directory)
    
    # for folder in folders:    
    #     full_folder_path = os.path.join(directory,folder)
       
    #     if os.path.isdir(full_folder_path):
    #         #create a folder named frames
    #         path = os.path.join(full_folder_path, "frames")
    #         if not os.path.exists(path):
    #             os.mkdir(path)

           
    #         movies = os.listdir(full_folder_path)
           
    #         for movie in movies:
    #             file_path = os.path.join(full_folder_path,movie)
    #             if os.path.isfile(file_path):
                    
    #                 #remove spaces from names
    #                 newfilename = movie.replace(" ","")
    #                 newpath = os.path.join(full_folder_path,newfilename)
    #                 if newfilename != movie:
    #                     os.rename(file_path, newpath)

    #                 full_frame_path = os.path.join(path,os.path.splitext(movie)[0]+"_")

    #                 subprocess.call(['ffmpeg', '-i', newpath, full_frame_path+"%04d.jpg"])

splitDataset()