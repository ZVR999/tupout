# function input
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
#function output
#[("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]

def tupOut(dic):
    lis = []
    for x in dic.items():
        lis.append(x)  
        #lis.append((x,y))  
    print lis
tupOut(my_dict)
# python tupout.py
