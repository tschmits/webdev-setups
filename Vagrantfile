# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.box = "debian-73-x64-virtualbox-nocm"
  config.vm.box_url = "http://puppet-vagrant-boxes.puppetlabs.com/debian-73-x64-virtualbox-nocm.box"

  config.vm.network "forwarded_port", guest: 8000, host: 8111
  config.vm.network "forwarded_port", guest: 80, host: 8000
  config.vm.network "private_network", ip: "192.168.10.2"

  config.vm.synced_folder "src/", "/srv/app/src/"

  config.vm.define "default", primary: true do |default|
    default.vm.provision :ansible do |ansible|
      ansible.playbook = "provisioning/deploy.yml"
      ansible.inventory_path = "provisioning/hosts.cfg"
      ansible.verbose = "vvvv"
      ansible.limit = "vagrant"
      ansible.ask_sudo_pass = false
    end
  end

end
