  # -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
  config.vm.hostname = "pyjobs-dev"

  # Если нужна виртуалка с ip, раскомментировать строку ниже
  # config.vm.network "private_network", ip: "10.0.0.5"
  # При необходимости, можно изменить порты
  config.vm.network "forwarded_port", guest: 8000, host: 8080

  config.vm.provider "virtualbox" do |vb|
    # количество памяти на машину
    vb.memory = "1024"
  end

  # Необходимо для работы ansible
  config.vm.provision "shell", inline: <<-SHELL
      apt-get update
      apt-get install -y python
  SHELL

  config.vm.provision :ansible do |ansible|
    # Путь до плейбука
    ansible.playbook = "dev.yml"
    ansible.ask_vault_pass = true
    ansible.verbose = false
  end
end
