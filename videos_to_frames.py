import os
import subprocess
import shutil
directory = "./"

def createFrames():
    global directory
    folders = os.listdir(directory)
    for folder in folders:    
        if os.path.isdir(folder):
            #create a folder named frames
            path = os.path.join(folder, "frames")
            if not os.path.exists(path):
                os.mkdir(path)
            movies = os.listdir(folder)
            for movie in movies:
                file_path = os.path.join(folder,movie)
                if os.path.isfile(file_path):
                    
                    #remove spaces from names
                    newfilename = movie.replace(" ","")
                    newpath = os.path.join(folder,newfilename)
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
        if os.path.isdir(folder):
            #create a folder named frames
            target_folder = os.path.join(folder, "frames_curated")
            if not os.path.exists(target_folder):
                os.mkdir(target_folder)
            
            source_folder = os.path.join(folder, "frames")
            print(source_folder, target_folder)

            source_frames = os.listdir(source_folder)
           
            for count, element in enumerate(source_frames, 0): # Start counting from 1
                if count % 8 == 0:
                    source_file = os.path.join(source_folder, element)
                    target_file = os.path.join(target_folder, element)
                    shutil.move(source_file, target_file)

def cleanUPCurated():
    global directory
    folders = os.listdir(directory)
    for folder in folders:    
        if os.path.isdir(folder):
            target_folder = os.path.join(folder, "frames_curated")
            if os.path.isdir(target_folder):
                shutil.rmtree(target_folder)


cleanUPCurated()
curateFrames()



        