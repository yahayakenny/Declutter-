import os
import shutil

downloads_path = '/Users/yahayakenny/Downloads'

code_path = os.path.join(downloads_path, "Code")
img_path = os.path.join(downloads_path, "Images")
books_path = os.path.join(downloads_path, "Books")
videos_path = os.path.join(downloads_path, "Videos")
music_path = os.path.join(downloads_path, "Music")


if not os.path.isdir(code_path):
    os.makedirs(code_path)
    print("Code folder created")
    
    
if not os.path.isdir(img_path):
    os.makedirs(img_path)
    print("Images folder created")
    
    
if not os.path.isdir(books_path):
    os.makedirs(books_path)
    print("Books folder created")
    
        
if not os.path.isdir(music_path):
    os.makedirs(music_path)
    print("Music folder created")
    
        
if not os.path.isdir(videos_path):
    os.makedirs(videos_path)
    print("Video folder created")
    
        

files = [f for f in os.listdir(downloads_path)]


for file in files:
  file_path = os.path.join(downloads_path, file)
  
  if file_path.endswith('.py') or file_path.endswith('.js') or file_path.endswith('.html'):
    print('move file to Code folder')
    shutil.move(file_path, code_path)
  
  if file_path.endswith('.png') or file_path.endswith('.jpg') or file_path.endswith('.jpeg'):
    print('move file to Images folder')
    shutil.move(file_path, img_path)
  
  if file_path.endswith('.pdf') or file_path.endswith('.docs') or file_path.endswith('.epub') or file_path.endswith('.ppt'):
    print('move file to Books folder')
    shutil.move(file_path, books_path)

  if file_path.endswith('.mkv') or file_path.endswith('.mp4') or file_path.endswith('.avi'):
    print('move file to Videos folder')
    shutil.move(file_path, videos_path)

  if file_path.endswith('.mp3'):
    print('move file to Music folder')
    shutil.move(file_path, music_path)

