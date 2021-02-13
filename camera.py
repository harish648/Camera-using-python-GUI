from tkinter import *
import cv2
root = Tk()
root.title('Camera')


def photo():
	cap=cv2.VideoCapture(0)

	while(True):
			ret,frame=cap.read() #ret is used for booleann whereas the frame is used for capturing the image 
			
			if 0xFF==ord('a'):
				cv2.imwrite('a.jpg',frame)

			if cv2.waitKey(1) & 0xFF== ord('q'):
				break
			cv2.imshow("capture",frame)
	cap.release()
	cv2.destroyAllWindows()

def video():
	cap=cv2.VideoCapture(0)
	
	fourcc = cv2.VideoWriter_fourcc(*'XVID')#fourcc refers compressed form of the recording
	out = cv2.VideoWriter("record.mp4",fourcc,20.0,(640,480))# the arguments here are the name, fourcc, frames per second , size of the recording
	
	while(True):
		ret,frame=cap.read() #ret is used for booleann whereas the frame is used for capturing the image 

		out.write(frame)
		#For displaying in Grayscale
		gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		cv2.imshow("Capture",frame)


		if cv2.waitKey(1) & 0xFF== ord('q'):
			break
	cap.release()
	out.release()
	cv2.destroyAllWindows()

def grayscale():
	cap=cv2.VideoCapture(0)
	
	fourcc = cv2.VideoWriter_fourcc(*'XVID')#fourcc refers compressed form of the recording
	out = cv2.VideoWriter("record.mp4",fourcc,20.0,(640,480))# the arguments here are the name, fourcc, frames per second , size of the recording
	
	while(True):
		ret,frame=cap.read() #ret is used for booleann whereas the frame is used for capturing the image 

		
		#For displaying in Grayscale
		gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
		out.write(gray)
		cv2.imshow("Capture",gray)


		if cv2.waitKey(1) & 0xFF== ord('q'):
			break
	cap.release()
	out.release()
	cv2.destroyAllWindows()

button_photo=Button(root,text='Photo',padx=40,pady=20,command=photo)
button_video=Button(root,text='Video',padx=40,pady=20,command=video)
button_grayscale=Button(root,text='Grayscale Video',padx=40,pady=20,command=grayscale)

button_photo.grid(row=0,column=0)
button_video.grid(row=0,column=1)
button_grayscale.grid(row=0,column=2)

root.mainloop()