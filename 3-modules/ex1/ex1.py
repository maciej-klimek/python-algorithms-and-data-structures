import os, glob, shutil

def categorise(files):
    for file in files:
        fileName = os.path.basename(file)   
        print(fileName)
        try: 
            os.mkdir(f"dirs/{fileName[0]}")
            shutil.move(file, f"dirs/{fileName[0]}")
            print("stworzono")
        except FileExistsError:
            shutil.move(file, f"dirs/{fileName[0]}")
            print("przeniesiono")

                
    
            
            

def main():
    fileList = glob.glob("dane/*", recursive = True)
    categorise(fileList)

main()

