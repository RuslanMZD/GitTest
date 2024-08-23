file = open("test.txt", 'r')
content = file.read()
print(content)
file.close()

file = open('example.txt','r')
for line in file:
    print(line.strip())
file.close()

file = open('example.txt','w',encoding='utf-8')

try:
    with open("example.txt",'a',encoding='utf-8') as file
        file.write("Новая линия.")
except FileNotFoundError as e:
    print(e)

input_file =open("input_image.jpg","rb")
content=input_file.read()
output_image=open("output_image.jpg",'wb')
output_image.write(content)
input_file.close()
output_image.close()

class Test:
    def __init__(self,name:str,age:int):
        self.name = name
        self.age = age
        self.drop_value="Drop data"
    def __reduce__(self):
        return (self.__class__,(self.name,self.age))
    def __repr__(self):
        return f"{self.name} , {self.age}"

test = Test("Ruslan",31)
serialize_obj = pickle.dumps(test)
deserialize_obj=pickle.loads(serialize_obj)
print(deserialize_obj)