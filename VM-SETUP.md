You'll want to clone this repository into an environment including python, git,
a text editor, and a Unix-style command line.

# Installing the BCE VM

You should have gotten a URL for the BCE VM. You can import this in VirtualBox.

# Installing on your own

Install Continuum anaconda, ensure that you're running the latest version, and
make sure you have git and a text editor installed!

# Backup method

Get a course instructor to set you up with an account on the dlab-collaboratool
server. They will tell you your username (you'll replace that wherever it says
`<username>` below) and password.

    ssh <youraccount>@dlab-collaboratool.berkeley.edu
    git clone <your-git-python-fundamentals>
    cd python-fundamentals/cheat-sheets
    ./start-ipython.sh

# Previous method

## Installing a custom VM using Vagrant

After installing [Vagrant](http://www.vagrantup.com/downloads.html) and
[VirtualBox](https://www.virtualbox.org/wiki/Downloads), navigate to the
location of the python_fun.box (provided by the class), and type:

    vagrant box add python_fun python_fun.box virtualbox

## Getting the files from GitHub for Vagrant

Make a github account: https://github.com
Fork and clone our github repository: https://github.com/dlab-berkeley/python-fundamentals
cd to where you put the above clone, then
Run `vagrant up` followed by `vagrant ssh`

## Inside the VM

    cd /vagrant
    ./ipython-from-inside-vagrant.sh

## Then, in your browser

http://10.10.10.10:8888


