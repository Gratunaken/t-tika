#tátika
import sys
import random
q="q"
w="w"
e="e"
r="r"
t="t"
z="z"
u="u"
i="i"
side1=[q,w,e,r]
side2=[t,z,u,i]
#a kör ciklushoz kell
help1=1
help2=2
#váltzók kiválasztása és változtatása.
while help1<help2:
    print("the variables : " ,q,w,e,r,t,z,u,i)
    var=str(input("which variable do you want to change?: "))
    new_var=str(input("the new variable:"))
    if var=="q":
        q=new_var
    if var=="w":
        w=new_var
    if var=="e":
        e=new_var
    if var=="r":
        r=new_var
    if var=="t":
        t=new_var
    if var=="z":
        z=new_var
    if var=="u":
        u=new_var
    if var=="i":
        i=new_var
    help1=help1+1
    run_the_code=str(input("do you want to play the [tátika]?(i)"))
    if run_the_code == "i":
        while help1==help2:
            tatika_help=int(input("choose a number 1-10: "))
            side_help=tatika_help%2
            if side_help==0:
                print("◉ ◉ ◉ ◉")
                tatika_help2=int(input("choose a number 1-4  :"))
                if tatika_help2==1:
                    print(q)
                if tatika_help==2:
                    print(w)
                if tatika_help==3:
                    print(e)
                if tatika_help==4:
                    print(r)
                
            if side_help!=0:
                print(side2)
    else:
        print("")
        help2=help2+1
            
            
        
