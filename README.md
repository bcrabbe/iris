Install
___

Ppip3.6 install -U flask
pip3.6 install numpy sklearn

run
___
env FLASK_APP=server.py flask run

curl -d '{
"features":[
    [1,1,1,1],
    [2,2,2,2],
    [3,3,3,3]
  ]
}' -H "Content-Type: application/json" -X POST http://localhost:5000
