# Log Analysis Project
Udacity's third project of *Full Stack Web Developer I Nanodegree Program*

## Project Description
The objective is to perform SQL queries on a given database to retrive the desired data using **DB-API** which will help us.

## Queries to perform
1. **What are the most popular three articles of all time?**
 >Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

1. **Who are the most popular article authors of all time?**
 >That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

1. **On which days did more than 1% of requests lead to errors?**
 >The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser.

## Setup required for Project
Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem.


This project is run in a virutal machine created using Vagrant so there are a few steps to get set up:
**Installing and running the Virtual Box and Vagrant**
1. Install [Vagrant](https://www.vagrantup.com/)
2. Install [VirtualBox](https://www.virtualbox.org/)
3. Download the vagrant setup files from [Udacity's GitHub Repository](https://github.com/udacity/fullstack-nanodegree-vm)
4. Download the ```newsdata.sql``` file: [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
5. Put the newsdata.sql file into the vagrant directory
6. Add the project's file to the same directory

**Starting Vagrant and Virtual Machine**
1. Open command line and change the directory to vargrant directory.
2. Run ```vagrant.up``` to download the virtual ubuntu machine. This will cause Vagrant to download the Linux operating system and install it.
> When vagrant up is finished running, you will get your shell prompt back. 
At this point, you can run vagrant ssh to log in to your newly installed Linux VM!
3. Run ```vagrant ssh``` to start the virtual machine.

**Loading the Database**
1. Use ```cd /vagrant``` to move to vargrant directory.
2. Run ```psql -d news -f newsdata.sql``` to load the data.

**Creating necessacry views to perform queries**
1. Load the database into the virtual machine using ```psql -d news```
2. Run the following code to create view necessary for running query 1.
>SELECT path, count(*) AS views
FROM log
WHERE status = '200 OK'
GROUP BY log.path;
## Running the Queries
Once the data is loaded, run ```python newsquery.py``` to start the queries.