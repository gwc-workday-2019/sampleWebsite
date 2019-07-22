import filters
def main():
    print ("in main")
    filename = 'input/pineapple.jpg'
    myIm = filters.load_img(filename)
    filters.save_img(myIm,'output/mynewimage.jpg')

if __name__=="__main__":
    main()
