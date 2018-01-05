import cv2
import keyboard

folderDirectory = "pics/"

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

	while True:
		try:
			f = open(filename(filenum))
			f.close()
			filenum += 1
		except IOError as e:
			break

	while cap.isOpened():
		
		_,frame = cap.read()
		cv2.imshow('frame', frame)		
		
		if cv2.waitKey(1) & 0xFF == ord('p'):
			cv2.imwrite(filename(filenum), frame)
 			filenum += 1
		if cv2.waitKey(1) & 0xFF == ord('q'):
		        break

	cv2.destroyAllWindows()
	del(cap)

if __name__ == '__main__':
    main()
