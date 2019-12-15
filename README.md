# Convin Assignment

## Clone the repository

`gir clone https://github.com/apoorvpatne10/congenial-waddle/`

## Create a virtual environment and activate it 

`virtualenv <environment name>`
`source <environment name>/bin/activate`

## Install the requirements

`pip install -r requirements.txt`

## Run initial migrations

`python manage.py migrate`

## Fire up the local server

`python manage.py runserver`

#### I. Create a model having fields of type CharField and FileField. Implement a system on top of this model which should notify the updated/created field only and its old and new value. (it shouldn’t notify about the field which is not updated). It should also notify in case content of FileField is changed. [You may use signals or any other mechanism of your choice.] 

#### II. Now suppose CharField is the encrypted value of the content of FileFIeld (or you can choose any heavy computation of your choice on the content of File(it may be just along for loop)). Implement a system which allows updating FileField content by an external party (for example invoking management command from bash or calling a Django API or your choice of making it accessible by an external party). Note: after FileField content is changed, it should notify the updated value of FileField and CharField. 

#### 1. Simple form UI for file name and file upload

![img](https://i.imgur.com/zJ6Bqst.png)

#### 2. View after a couple of files have been uploaded

![img](https://i.imgur.com/dBz3QkK.png)

#### 3. Simple notification using Django File Tracker and Django messages (with current and previous values)

![img](https://i.imgur.com/YPqtft4.png)

#### 4. Encryption of file contents using Fernet (symmetric encryption) stored in CharField

![img](https://i.imgur.com/uPV0T7p.png)

