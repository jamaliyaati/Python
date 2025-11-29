class Picture:
    def __init__(self,desc,width,height,Fcolour):
        
        self.__desc = desc 
        self.__width = width
        self.__height = height
        self.__Fcolour = Fcolour


    def GetDescription(self,desc):
        desc = self.__desc
        return desc
    
    def GetHeight(self,Height):
        height = self.__height
        return height 
    
    def GetWidth(self,width):
        width = self.__width
        return width

    def GetColour(self,colour):
        colour = self.__Fcolour
        return colour
    
    def SetDescription(self,Sdesc):
        self.__desc = Sdesc

PictureArray = []
for i in range(100):
    PictureArray.append(Picture("",0,0,""))

def ReadData():
    filename = "Pictures.txt"
    counter = 0

    try:
        File = open(filename,'r')
        Description = (File.readline()).strip()
        while Description != "":
            Width = int((File.readline()).strip())
            Height = int((File.readline()).strip())
            Frame = int((File.readline()).strip())
            PictureArray[counter] = Picture(Description,Width,Height, Frame)

            
            counter += 1
            Description = (File.readline()).strip()
        File.close()
    except:
        FileNotFoundError
        print("file not found")
    return PictureArray,counter

    