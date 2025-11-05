import shutil

source = "D://IO//Rays.png";
target = "D://IO//Sunrays.png";

shutil.copyfile(source, target)
print(source + " is copied to " + target)
