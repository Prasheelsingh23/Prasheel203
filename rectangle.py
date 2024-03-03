def main():
   lenght = getlenght()
   width = getwidth()
   area = calculatearea(lenght,width)
   displayarea(area)

def getlenght():
    lenght = int(input("lenght :"))
    return lenght
def getwidth():
    width = int(input("width :"))
    return width
 

def calculatearea(lenght,width):
   
    area = lenght * width
    return area
 
def displayarea(area):
    print("Area is:", area)
    
main()
    
