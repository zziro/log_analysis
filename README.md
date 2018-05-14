# log_analysis

News is a popular newspaper which has big audience of readers who are daily pending about new articles and relevant information.

In this project you will get answers such as:

* What are the most popular articles that the users prefer to read.
* What authors are most prefered to read.
* In which day the newspaper could not attent all request, base on that, the error rate was more than 1%.

To get all information listed above, the Information Technology area, store the data into three tables:

* Authors.- Store information about authors.
* Articles.- Store information regarding articles.
* Log.- Store information regarding each time the user has accessed the site.


The following are prerequisites for this project:

* Virtualbox 5.1.34.- you can download it from https://www.virtualbox.org/wiki/Download_Old_Builds_5_0 
* Vagrant 1.8.5.- you can download it from https://github.com/udacity/fullstack-nanodegree-vm


Installing tools:

Virtualbox:
	Once you download VirtualBox in your local, follow these steps: https://askubuntu.com/questions/264292/how-do-i-install-virtualboxs-deb-package	

Vagrant:
	Go to the following repository and clone the project.
   * git clone https://github.com/udacity/fullstack-nanodegree-vm

   Once you do that, you will have a folder called 'fullstack-nanodegree-vm-master' (normally is located on your Download folder), inside there, there is a folder called 'vagrant', this folder is shared between your local machine and your virtual machine. 	


Running the virtual machine:

   By command line navigate to the vagrant folder and execute 'vagrant up':
   * fullstack-nanodegree-vm-master/vagrant$ vagrant up

Logging into the virtual machine:

   By command line navigate to the vagrant folder and execute 'vagrant ssh':
   * fullstack-nanodegree-vm-master/vagrant$ vagrant ssh	

Loading data:

   By command line navigate go to the vagrant folder and clone the git 'log_analysis' project.

   * fullstack-nanodegree-vm-master/vagrant$ git clone https://github.com/zziro/log_analysis

   Inside 'log_analysis' folder there is a .zip file named newsdata.zip, unzip that using:

   * unzip newsdata.zip

   Then  you will see the file newsdata.sql, copy and paste it to the vagrant folder and execute the following command.	

   fullstack-nanodegree-vm-master/vagrant$ psql -d news -f newsdata.sql

   The commands 'psql','-d','-f' stands for:
   * psql .- The PostgreSQL command line program
   * -d .- Refers to the database to be connected ('news' database on this case) 
   * -f .-  Refers the file to be readed.

   Running the above command ensure to be connected to the 'news' database and you will able to interact with the data content on it.


Running 'Log_Analysis' project:

   Before to run the project, you will need to install the PrettyTable library. This library will rich the outputs of the results.	
   
   * fullstack-nanodegree-vm-master/vagrant$ sudo pip3 install PTable

   Change your directoy to 'log_analysis'.

   * fullstack-nanodegree-vm-master/vagrant$ cd /log_analysis

   and run the app.py

   * fullstack-nanodegree-vm-master/vagrant/log_analysis$ python app.py

   Once you that, you will see a .txt file called results.txt. 

   Note: In order to make sure if the app.py generate the results.txt file, delete it, and run the app.py file again.
