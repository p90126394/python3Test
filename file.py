#儲存檔案
#file=open("data.txt", mode="w",encoding="utf-8")
#file.write("測試中文文\n好棒棒")
#file.close()
with open("data.txt",mode="w", encoding="utf-8") as file:
    file.write("5\n3")

#讀取檔案
#with open("data.txt",mode="r", encoding="utf-8") as file:
 #   data=file.read()
#print(data)
#把檔案中的數字資料一行一行的讀取出來，並計算總合`
#sum=0
#with open("data.txt",mode="r", encoding="utf-8") as file:
 #   for line in file:
  #      sum+=int(line)
#print(sum)
#使用 Json 格式讀取、複寫檔案
import json
with open("config.json", mode="r") as file:
    data=json.load(file)
#print ("name",data["name"])
#print("version",data["version"])
print(data) #data 是一個字典資料
data["name"]="New Name"
# 把最新的資料複寫回檔案中
with open("config.json", mode="w") as file:
    json.dump(data, file)

