import os
import subprocess
import shutil
import random
directory = "./dataset"


#folder structure
#root
    #ffmpeg.exe
    #thisscript.py
    #folder_dataset
        #folder_category_a
            #movie1.mov
            #movie2.mp4
        #folder_category_b
            #movie_1.mov
            #movie_2.mov

print("START")

def createFrames():
    global directory
    folders = os.listdir(directory)
    
    for folder in folders:    
        full_folder_path = os.path.join(directory,folder)
       
        if os.path.isdir(full_folder_path):
            #create a folder named frames
            path = os.path.join(full_folder_path, "frames")
            if not os.path.exists(path):
                os.mkdir(path)

           
            movies = os.listdir(full_folder_path)
           
            for movie in movies:
                file_path = os.path.join(full_folder_path,movie)
                if os.path.isfile(file_path):
                    
                    #remove spaces from names
                    newfilename = movie.replace(" ","")
                    newpath = os.path.join(full_folder_path,newfilename)
                    if newfilename != movie:
                        os.rename(file_path, newpath)

                    full_frame_path = os.path.join(path,os.path.splitext(movie)[0]+"_")

                    subprocess.call(['ffmpeg', '-i', newpath, full_frame_path+"%04d.jpg"])


#curate frames auto
#for count, element in enumerate(mylist, 1): # Start counting from 1
    #if count % 10 == 0:
        # do something

def curateFrames():
    global directory
    folders = os.listdir(directory)
    for folder in folders:
        full_folder_path = os.path.join(directory,folder)
        if os.path.isdir(full_folder_path):
            #create a folder named frames
            target_folder = os.path.join(full_folder_path, "frames_curated")
            if not os.path.exists(target_folder):
                os.mkdir(target_folder)
            
            source_folder = os.path.join(full_folder_path, "frames")
            print("CREATING ",source_folder, target_folder)
            source_frames = os.listdir(source_folder)
            for count, element in enumerate(source_frames, 0): # Start counting from 1
                if count % 1 == 0:
                    source_file = os.path.join(source_folder, element)
                    target_file = os.path.join(target_folder, element)
                    shutil.copy(source_file, target_file)

def cleanUPCurated():
    global directory
    folders = os.listdir(directory)
    for folder in folders:    
        full_folder_path = os.path.join(directory,folder)
        if os.path.isdir(full_folder_path):
            target_folder = os.path.join(full_folder_path, "frames_curated")
            print("DELETE ",target_folder)
            if os.path.isdir(target_folder):
                shutil.rmtree(target_folder)


def balance():
    max_number = 870
    global directory
    folders = os.listdir(directory)
    for folder in folders:    
        full_folder_path = os.path.join(directory,folder, "frames_curated")
       
        files = os.listdir(full_folder_path)
        number_to_delete = len(files) - max_number
        
        if number_to_delete>0:
            print("DELETE FILES ", full_folder_path, len(files))
            print("TOTAL TO DELETE ",number_to_delete)
            files = random.sample(files, number_to_delete) 
            for file in files:  # Go over each file name to be deleted
                full_file_path = os.path.join(full_folder_path,file)
                os.remove(full_file_path)  # Remove the file
            print("*****************************")

#createFrames()
#cleanUPCurated()
#curateFrames()
balance()
