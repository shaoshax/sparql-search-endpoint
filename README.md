## 透過Flask套件建立一個Sparql查詢的API，並將回應內容轉為json格式
需依循下方指令安裝套件Flask,Owlready2,flask-cors
```
pip install Flask
pip install owlready2
pip install flask-cors
``` 
以ar.owl作為範本查詢
執行sparql-endpoint.py後
編輯sqarql.html中第11行query變數輸入欲執行之指令
以瀏覽器打開該網頁後按下Executre Qurey後
會以POST方法訪問該端口並將結果以json格式回傳
至瀏覽器的檢查以查看返回之結果
