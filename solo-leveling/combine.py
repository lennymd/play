from time import sleep

text = ""
t = open("solo_leveling.txt","a")

# for ch in range(1,244):
#     print(ch)
#     f = open("chapters/chapter-"+str(ch)+".txt","r")
#     t.write(f.read())
#     f.close()
#     sleep(0.5)

# sleep(10)
# print("moving to extra chapters")

for ch in range(0,27):
    print(ch)
    f = open("chapters/chapter-extra-"+str(ch)+".txt","r")
    t.write(f.read())
    f.close()
    sleep(0.5)

print("all done")