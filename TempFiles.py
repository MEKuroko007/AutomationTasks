import os
print("---------------tmp----------------")
#path=os.system('echo %TEMP%')
print("do you want to show tmp files or remove it : ")
print("""
        1-- Display files 
        2-- remove temp files
    """)

choose=input("choose on choices 1,2 : ")
if choose==1:
    print(os.system('START %TEMP%'))
elif choose==2:
    path=os.system('echo %TEMP%')
    R_files=os.system('del /q/f/s path\* ')
    print("files has been deleted")
