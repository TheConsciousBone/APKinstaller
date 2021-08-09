import os
print("Please insure that an Android device is connected.")
LOCATE = input("FIle location (drag and drop the file here)? ")
CONFIRM = ("")

print("The file location is:", LOCATE)
CONFIRM = input("Please confirm your choice. Input Y or N to choose. ")
if CONFIRM == "Y":
    print("Confirmed. Installing to connected device now.")
    os.system('"cd C:\\adb"')
    os.system('"adb devices"')
    os.system("adb install " + LOCATE)
else:
    if CONFIRM == "N":
        print("Cancelled.")
    else:
        print("Invalid input. Run the executer again.")



# os.system('"cmd command goes here"')
