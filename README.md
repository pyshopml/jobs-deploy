# jobs-deploy

## Run the VM and deploying backend into it
### Intro
Create a virtual machine using vagrand and deploy backend inside.
Port 8000 of the guest machine is proxy for 8080 of the hosts (Can be changed in Vagrantfile).
Access to the VM:

    # run it in VM dir or with id/name (vagrant global-status)
    vagrant ssh

Default user (ubuntu) user can use `sudo` without password.

### Install virtualbox + vagrant

Download virtualbox from [here](https://www.virtualbox.org/wiki/Linux_Downloads) and vagrant from [here](https://www.vagrantup.com/downloads.html):

    mkdir tmp
    wget http://download.virtualbox.org/virtualbox/5.1.20/virtualbox-5.1_5.1.20-114628~Ubuntu~xenial_amd64.deb
    wget https://releases.hashicorp.com/vagrant/1.9.3/vagrant_1.9.3_x86_64.deb
    sudo dpkg -i virtualbox-5.1_5.1.20-114628~Ubuntu~xenial_amd64.deb
    sudo dpkg -i vagrant_1.9.3_x86_64.deb
    # remove tmp if install successfully done
    cd ..
    rm -rf tmp

### Clone repo and create VM

Clone repo from github:

    git clone https://github.com/pyshopml/jobs-deploy.git -b JOBS-096
    cd jobs-deploy/

Then run:

    vagrant up

It will asking you for Vault password. You can find it in Discord

### Check results

runserver:

    vagrant ssh               # logging in
    sudo su pyjobs            # changing user
    cd ~/pyjobs/jobs-backend/ # cd to proj dir
    source venv/bin/activate  # enabling virtualenv
    ./manage.py runserver 0.0.0.0:8000

Now check `127.0.0.1:8080` in your browser
