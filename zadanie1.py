f=input("Придумайте пароль:"+chr(10))
s=input("Повторите пароль:"+chr(10))
print(100*"\n")
if f==s:
    print("Пароль принят")
else:
    print("Пароль не принят")