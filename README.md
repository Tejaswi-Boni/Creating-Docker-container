# MLProject

#create conda environment
conda create -p venv python==3.7 -y

conda activate venv

#Flask installation

pip install -r requirements.txt

#Build docker image

docker build -t <image_name>:<tag_name>

Image_name : should be lower case

#Run docker image

docker run -p 5000:5000 -e PORT = 5000 <Imageid>

#to check running container

docker ps

#to stop docker container

docker stop <container_id>