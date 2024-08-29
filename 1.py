class Hash:
    def _init__(self):
        self.buckets=[[],[],[],[],[]]
    def insert(self,key):
        bindex=key%5
        self.buckets[bindex].appened(key)
        print(key,"inserted in bucket no.",bindex+1)
    def search(self,key):
        bindex=key%5
        if key in self.buckets[bindex]:
            print(key,"present in bucket no.",bindex+1)
        else:
            print(key,"present in bucket no.",bindex+1)
    def display(self):
        for i in range(0,5):
            print("/n bucket no.",i+1,end=":")
hsh=Hash()
while True:
    print("/n Hash operations 1.insert 2.search 3.display 4.quit")
    ch=int(input("enter your choice:"))
    if ch==1:
        key=int(input("enter key to be inserted:"))
        hsh.insert(key)
    elif ch==2:
        key=int(input("/n enter key to be searched:"))
        hsh.search(key)
    elif ch==3:
        hsh.display()
    else:
        break