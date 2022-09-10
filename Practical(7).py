# there are dictionaries in python
# you can make a dictionary in python by using the d = {} function
# or d= dict{}
# a key is normally a string and the value is numarical
d = {}
d ["George"] = 24
d ["Tom"] = 32
d ["Jenney"] = 16
print (d["Tom"])
print (d["George"])
print (d["Jenney"])
d[10] = 100
print (d[10])
# the following is how to iterate over key-value pairs
for key, value in d.items():
    print("key:")
    print(key)
    print("value:")
    print(value)
    print("")
