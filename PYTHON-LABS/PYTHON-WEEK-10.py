# import numpy as np

# # Create an array of 10 zeros
# zeros = np.zeros(10)

# # Create an array of 10 ones
# ones = np.ones(10)

# # Create an array of 10 fives
# fives = np.full(10, 5)

# # Concatenate the arrays
# result = np.concatenate((zeros, ones, fives))

# print(result)
def main():
# Open file for output
    outfile=open('python.txt','w')
# Write data to the file
    outfile.write("Bill Clinton\n")
    outfile.write("George Bush\n")
    outfile.write("Barack Obama") 
    print(outfile)
    # Close the output file
    outfile.close()  
main()
