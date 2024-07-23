import instaloader
import sys

def DownloadPpWithoutProfile(target):
    print(f"trying to download {target} 's profile picture ")
    instaloader.Instaloader().download_profile(target,profile_pic_only=True)
    print("downloaded succesfully")

def DownloadPpWithProfile(target):
    
    instaloader.Instaloader().download_profile(target,profile_pic_only=False)
    print("downloaded succesfully")

try:
    uName = str(input("type profile name :"))
    print("choose download option.")
    print("1- only profile picture")
    print("2- profile picture with posts(if account isn't private)")
    
    
    while True:
        choice = int(input())
        if(choice==1 or choice==2):
            break
        print("unkown input, enter valid value")
    print("trying to download")

    if(choice==1):
        DownloadPpWithoutProfile(uName)
    elif (choice==2):
        DownloadPpWithProfile(uName)

    print("download successfuly finished.")

except Exception as e:
    if(type(e.__cause__) == "instaloader.exceptions.LoginRequiredException"):
        print("cant download because account is private.")
    sys.exit()

