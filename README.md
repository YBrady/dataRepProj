<img align="left" src="/images/GMIT-logo.png" alt="GMIT" width="200"/>                               <img align="right" src="/images/data-analytics.png" alt="HDipDA" width="300"/>  

# Data Representation Semester 2 2019 #

___________________________________________

**Module Name**: Data Representation  
**Assignment**: Web Application Project 
**Module Number**: 52957  
**Student Name**: Yvonne Brady  
**Student ID**: G00376355  
___________________________________________


## 1.0 General Description

It being Christmas, this project involves a North Pole console. There is a html front-end application linking via FLASK server to a mySQL database.  

## 2.0 HTML Application
Features include:
* Login required for access beyond homepage. Username / passwords as follows:
    - santa@claus.com / santaclaus
    - elf@santa.com / ontheshelf
    - me@me.com / mepassword
* On screen animation
    - Easter egg (click on Believe)
* Linkage to Weather and Gmail APIs
    - Categorises mails into "Indication of Nice / Naughty" based on content
    - Email address: datarep.northpole@gmail.com
    - Password available on moodle submission page.

### 2.1 Pages
There are four pages as follows:  
* Home - need to log in here to access any other screen
* List Admin - to view and amend Naughty and Nice Lists
* Workshop Admin - to see which toys are being manufactured and which that have been requested are not yet on the production list
* Weather and Messaging Center - Link to provide weather details at North Pole for Christmas Eve 2018, 2019 and current weather. (Too early for Christmas 2020 details.)

## 3.0 mySQL Application
There is a SQL dump of the database included with some sample data in there too.    
* Database name: drproject
* Two Tables:
    - people: houses information on children on the naughty and nice lists  
    - toys: houses information on the workshop output

## 4.0 Python  
* Server: projServer.py
* DAO: santaDAO.py
* APIs: projApi.py

## 5.0 Conclusion
This was an enjoyable project to do, I only wish I had more time for it. There are lots more I could have done with respect to packing sleigh / stock reconcilliations etc.  

Apologies for my inexpert putting together of the site and hacking of the login in particular. In my defence - am no web developer!

Many thanks for a very enjoyable module.