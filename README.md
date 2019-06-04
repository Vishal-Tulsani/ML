# What Is Computer Vision?

To simplify the answer to this – Let us consider a scenario.

We all use Facebook, correct? Let us say you and your friends went on a vacation and you clicked a lot of pictures and you want to upload them on Facebook and you did. But now, wouldn’t it take so much time just to find your friends faces and tag them in each and every picture? Well, Facebook is intelligent enough to actually tag people for you.

So, how do you think the auto tag feature works? In simple terms, it works on computer vision.

Computer Vision is an interdisciplinary field that deals with how computers can be made to gain a high-level understanding from digital images or videos.

The idea here is to automate tasks that the human visual systems can do. So, a computer should be able to recognize objects such as that of a face of a human being or a lamppost or even a statue.

# What Is OpenCV?

OpenCV is a Python library which is designed to solve computer vision problems. OpenCV was originally developed in 1999 by Intel but later it was supported by Willow Garage.

OpenCV supports a wide variety of programming languages such as C++, Python, Java etc. Support for multiple platforms including Windows, Linux, and MacOS.

OpenCV Python is nothing but a wrapper class for the original C++ library to be used with Python. Using this, all of the OpenCV array structures gets converted to/from NumPy arrays.

This makes it easier to integrate it with other libraries which use NumPy. For example, libraries such as SciPy and Matplotlib.

Next up on this OpenCV Python Tutorial blog, let us look at some of the basic operations that we can perform with OpenCV. 
Basic Operations With OpenCV?

Let us look at various concepts ranging from loading images to resizing them and so on.
Loading an image using OpenCV:
	
1-Import cv2

 #colored Image
 
2-Img = cv2.imread (“Penguins.jpg”,1)
 
 #Black and White (gray scale)
 
3-Img_1 = cv2.imread (“dog.jpg”,0)

As seen in the above piece of code, the first requirement is to import the OpenCV module.

Later we can read the image using imread module. The 1 in the parameters denotes that it is a color image. If the parameter was 0 instead of 1, it would mean that the image being imported is a black and white image. The name of the image here is ‘Penguins’. Pretty straightforward, right?
Image Shape/Resolution:

We can make use of the shape sub-function to print out the shape of the image. Check out the below image:
	
Import cv2
 
 #Black and White (gray scale)
 
Img = cv2.imread (“cat.jpg”,0)
 
Print(img.shape)

By shape of the image, we mean the shape of the NumPy array. As you see from executing the code, the matrix consists of 768 rows and 1024 columns.
Displaying the image:

Displaying an image using OpenCV is pretty simple and straightforward. Consider the below image:
	
import cv2
 
 #Black and White (gray scale)
 
Img = cv2.imread (“dog.jpg”,0)
 
cv2.imshow(“Penguins”, img)
 
cv2.waitKey(0)
 
 #cv2.waitKey(2000)
 
cv2.destroyAllWindows()

As you can see, we first import the image using imread. We require a window output to display the images, right?

We use the imshow function to display the image by opening a window. There are 2 parameters to the imshow function which is the name of the window and the image object to be displayed.

Later, we wait for a user event. waitKey makes the window static until the user presses a key. The parameter passed to it is the time in milliseconds.

And lastly, we use destroyAllWindows to close the window based on the waitForKey parameter.
Resizing the image:

Similarly, resizing an image is very easy. Here’s another code snippet:
	
import cv2
 
 #Black and White (gray scale)
 
img = cv2.imread (“cat.jpg”,0)
 
resized_image = cv2.resize(img, (650,500))
 
cv2.imshow(“cat”, resized_image)
 
cv2.waitKey(0)
 
cv2.destroyAllWindows()

Here, resize function is used to resize an image to the desired shape. The parameter here is the shape of the new resized image.

Later, do note that the image object changes from img to resized_image, because of the image object changes now.

Rest of the code is pretty simple to the previous one, correct?

I am sure you guys are curious to look at the cat, right? This is the image we were looking to output all this while!


