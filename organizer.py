import os


downloads_dir = r"C:\Users\Ashutosh\Downloads"

all_files = os.listdir(downloads_dir)
all_fext = []

#split all file extensions from the dir
for f in all_files:
	_, fext = os.path.splitext(f)
	if fext not in all_fext:
		all_fext.append(fext)

#create all dirs to organise files
for ext in all_fext:
	if ext:
		os.mkdir(os.path.join(downloads_dir, ext))

#move all files to their respective dirs
for f in all_files:
	_, ext = os.path.splitext(f)
	old_path = os.path.join(downloads_dir, f)
	new_path = os.path.join(downloads_dir, ext, f)
	os.rename(old_path, new_path)