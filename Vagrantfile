# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  # All Vagrant configuration is done here. The most common configuration
  # options are documented and commented below. For a complete reference,
  # please see the online documentation at vagrantup.com.

  # Every Vagrant virtual environment requires a box to build off of.
  config.vm.box = "python_fun"

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  # config.vm.network :forwarded_port, guest: 80, host: 8080

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  config.vm.network :private_network, ip: "10.10.10.10"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network :public_network

  # If true, then any SSH connections made will enable agent forwarding.
  # Default value: false
  # config.ssh.forward_agent = true

  # This will enable X11 forwarding over SSH
  # config.ssh.forward_x11 = true

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  # config.vm.synced_folder "../data", "/vagrant_data"

  # On Windows, the VM will mount /vagrant with all modes set, e.g. 777.
  # This interferes with ansible, within the guest, which doesn't tolerate
  # an executable inventory file. We only apply this on Windows so there are no
  # adverse affects on *nix / OSX.
  if Vagrant::Util::Platform.windows?
    config.vm.synced_folder ".", "/vagrant", :mount_options=> ["dmode=755","fmode=644"]
  end

  # VirtualBox specific configuration
  config.vm.provider :virtualbox do |vb|
    # If you want to boot with graphics
    # vb.gui = true

    # This works on newer Vagrant (tested on 1.4.1), Ubuntu uses
    # a cloud-credible 512MB by default.
    vb.memory = 2048
  end

end
