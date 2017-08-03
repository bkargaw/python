#
# Read and write files using the built-in Python file methods
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)

def main():
    # f = open('textfile.txt', "w+")
    # for i in range(10):
    #     f.write("this is line %d\r\n" % (i+1))
    #
    # f.close()
    #
    # f = open('textfile.txt', "a+")
    # for i in range(10):
    #     f.write("this is line %d\r\n" % (i+1))
    #
    # f.close()

    f = open('textfile.txt', "r")
    if f.mode == 'r':
        # content = f.read()
        # print content
        
        fl = f.readlines()
        for line in fl:
            print line
    f.close()
if __name__ == "__main__":
  main()
