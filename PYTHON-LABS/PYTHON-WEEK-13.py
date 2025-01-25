# file=open('python.txt','r')
# sfile= file.read()
# ufile= sfile.replace("daver","david")
# print(sfile)
# print(ufile)

# name=input('enter your name')
# guest=open('guest.txt','w')
# guest.write(name)
# guest.close()
# print(f"Your name '{name}' has been written to guest.txt.")



# f1 = open("jj", 'w')
# f1.write("something")
# f1.close()

# def main():
# # Open file for output
#     outfile=open('python.txt','w')
# # Write data to the file
#     outfile.write("Bill Clinton\n")
#     outfile.write("George Bush\n")
#     outfile.write("Barack Obama") 
#     print(outfile)
#     # Close the output file
#     outfile.close()  
# main()

def main():
# Open file for output
    outfile=open('python.txt','x')
# Write data to the file
    outfile.write("var, account_balance, client_name")
    outfile.write("var = 1\n account_balance = 1000.0\nclient_name = 'John Doe'") 
    print(outfile)
    # Close the output file
    outfile.close()  
main()
