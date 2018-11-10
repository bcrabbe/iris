Install
___
*requires python3.6.5*

python3.6 -m venv env
source env/bin/activate
pip install -r requirements.txt

run local
___

env FLASK_APP=app/main.py flask run

Test
___

curl -d '{
"features":[
    [1,1,1,1],
    [2,2,2,2],
    [3,3,3,3]
  ]
}' -H "Content-Type: application/json" -X POST http://localhost:5000

curl -v http://localhost:5000/test

docker
___

docker build -t iris:latest .
docker run -p 5000:80 --name iris iris


Installing python3.6 with homebrew
---
```brew install https://raw.githubusercontent.com/Homebrew/homebrew-core/f2a764ef944b1080be64bd88dca9a1d80130c558/Formula/python.rb```
or switch with:
``` brew switch python 3.6.5_1```
