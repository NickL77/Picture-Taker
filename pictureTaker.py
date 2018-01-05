import cv2
import keyboard

#set folder for where the pictures will be saved
folderDirectory = "pics/"

#Naming conventions for the pictures.
def filename(fnum):
	if fnum < 10:
		fname = folderDirectory + "000" + str(fnum) + ".jpg"
	elif fnum < 100:
		fname = folderDirectory + "00" + str(fnum) + ".jpg"
	elif fnum < 1000:
		fname = folderDirectory + "0" + str(fnum) + ".jpg"
	else:
		fname = folderDirectroy + str(fnum) + ".jpg"
	return fname

def main():
	print "Welcome, press 'p' to take a picture and 'Ctrl+C' to quit"

	cap = cv2.VideoCapture(0)
	filenum = 0

	#Iterate to the next picture name
	while True:
		try:
			f = open(filename(filenum))
			f.close()
			filenum += 1
		except IOError as e:
			break

	#Loop to capture and display feed
	while cap.isOpened():
		
		_,frame = cap.read()
		cv2.imshow('frame', frame)		
		
		#use to capture picture
		if cv2.waitKey(1) & 0xFF == ord('p'):
			cv2.imwrite(filename(filenum), frame)
 			filenum += 1
		#this doesn't work. Just use CTRL+C for now
		if cv2.waitKey(1) & 0xFF == ord('q'):
		        break

	cv2.destroyAllWindows()
	del(cap)

if __name__ == '__main__':
    main()
