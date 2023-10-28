# Your task now is to write a Python program which accepts the radius of a circle from the user and computes area.
r = (float(input("Input the radius of the circle :"))) 
AREA = 3.14159265*r**2 # area = pi x r^2
print (f"The area of the circle with radius {r} is:",AREA)

# Your second task now is to write a Python program to accept a filename from the user and print the extension of that.
a=input("Input the Filename:")
if ".py" in a:
    print("The extension of the file is : 'python'")
elif ".7z" in a:
    print("The extension of the file is : 'compressed file'")
elif ".mp3" in a:
    print("The extension of the file is : 'audio file'")
elif ".exe" in a:
    print("The extension of the file is : 'Executable file'")
elif ".msi" in a:
    print("The extension of the file is : 'Windows installer package'")
elif ".jpeg" or ".jpg" in a:
    print("The extension of the file is : 'JPEG image'")
elif ".ppt" in a:
    print("The extension of the file is : 'PowerPoint presentation'")
else:
    print("The extension of the file is : 'unknown'")
