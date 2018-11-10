Install
___
python3.6 -m venv irisEnv
source irisEnv/bin/activate
pip install -r requirements.txt

<!-- pip3.6 install -U flask -->
<!-- pip3.6 install numpy sklearn -->

run local
___

env FLASK_APP=app/main.py flask run

test
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
