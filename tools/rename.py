# All imports
import os

# Initialising important variables
cwd = os.getcwd() + "/"
all_files = os.listdir(cwd)
jpg = []
jpeg = []
mp4 = []

# Sorting the files
for file in all_files:
	if file.endswith(".jpg") == True:
		jpg.append(file)
	elif file.endswith(".jpeg") == True:
		jpeg.append(file)
	elif file.endswith(".mp4") == True:
		mp4.append(file)
	else:
		pass

# Defining the main function
def mainrname(list, ext):
	x = 0
	tempx = "0"
	fname = ""
	for item in list:
		x += 1
		if x < 10:
			tempx = "00" + str(x)
		elif x < 100:
			tempx = "0" + str(x)
		else:
			pass
		fname = tempx + ext
		src = item
		dest = fname
		os.rename(src, dest)

# Running the main function
if __name__ == "__main__":
	try:
		for item in jpg:
			mainrname(jpg, ".jpg")
		for item in jpeg:
			mainrname(jpeg, ".jpeg")
		for item in mp4:
			mainrname(mp4, ".mp4")
	except:
		pass
