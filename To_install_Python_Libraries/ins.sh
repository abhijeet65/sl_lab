sudo mkdir /opt/python
sudo mkdir ~/dataset
sudo chmod 777 /opt/python
sudo chmod 777 ~/dataset
sudo wget 172.1.32.41/dataset_new.tar.gz -P ~/
sudo tar -zxvf ~/dataset_new.tar.gz -C ~/dataset/
sudo cp ~/dataset/*.* /opt/python/
sudo chmod 777 /opt/python/*.*
sudo apt-get update
sudo apt-get install python3.pip
sudo pip3 install --upgrade pip
sudo pip3 install pandas
sudo pip3 install seaborn
sudo pip3 install flask
sudo pip3 install jupyter
sudo pip3 install numpy
sudo pip3 install matplotlib
sudo pip3 install cairocffi

