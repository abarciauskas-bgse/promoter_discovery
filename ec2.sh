ssh -i ~/.ssh/abarciauskas.pem ubuntu@ec2-54-193-98-81.us-west-1.compute.amazonaws.com

# One time on the instance
sudo pip install --upgrade pip
sudo pip install ipython
sudo pip install jupyter
sudo pip install keras
sudo apt-get install libhdf5-dev
sudo pip install h5py
sudo pip install --upgrade --no-deps git+git://github.com/Theano/Theano.git --user

#clone my repo
git clone https://github.com/abarciauskas-bgse/promoter_discovery
cd promoter_discovery

THEANO_FLAGS=mode=FAST_RUN,device=gpu,floatX=float32 ipython notebook

#ssh -i ~/.ssh/abarciauskas-bgse.pem -L 10000:localhost:8888 ubuntu@ec2-54-193-98-81.us-west-1.compute.amazonaws.com

# if permissions error
# sudo chown -R ubuntu:ubuntu /home/ubuntu/
