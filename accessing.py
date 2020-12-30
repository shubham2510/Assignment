#commands for executing program
#execute commands after running the program

create("shubzz",25)


create("Windows",70,3600) 


read("shubzz")


read("Windows")


create("shubzz",50)
#ERROR since the key_name already exists in the database

x.delete("shubzz")
 
t1=Thread(target=(create or read or delete),args=(key_name,value,timeout))
t1.sleep()
t2=Thread(target=(create or read or delete),args=(key_name,value,timeout)) 
t2.start()
t2.sleep()

#various errors are return by the program as per the problem statement.

