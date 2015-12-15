# Brief Summary
The goal of this website is to implement a proof of concept program that simulates the sharing of data to a 
community of users using a virtual currency. In summary the user is designed to have a wallet, 
that holds their virtual balance and can have multiple files that can be downloaded by other users. Once a 
user purchases a file using their credit, the credit will be subtracted from the purchaser's balance
and will be transferred to the owner of the file. The owner can then use that credit in addition to their original credit
to download other users' files.

# Instructions to install programs and run Webcredit

If you don't have Python installed yet, click [here for instructions on installation](https://github.com/limedaring/HelloWebApp/tree/master/installation-instructions).

The following instructions on running the program are based off of using the Juice Box virtual machine. Once you have
Python installed you can install Django and setup the environment to run the program. Open your terminal and make sure you're in
the webcredit (top-level) directory. Here is an example on how to navigate to the correct directory:

```
$ cd projects
projects $ cd webredit
```
### Start your virtual environment

Now that you're within the webcredit folder, create your virtual
environment. We'll be using virtualenv, [which we installed after we installed
Python](https://github.com/hellowebapp/hellowebapp/tree/master/installation-instructions).

```
projects/webredit $ virtualenv venv
```

And then activate the environment:

```
projects/webredit $ source venv/bin/activate
```
You should see something like this in your command line before the folder
structure - the (venv) indicates you're in the virtual environment:

```
(venv)juiceboxg@Ojuicebox ~/projects/webcredit $ 
```

(juicebox is my computer's name and username - your exact setup
may be different.)

Now you're in your bubble, so we can start installing project-specific utilities.
If you ever need to deactivate your environment, run `deactivate`.

### Install Django

Finally, it's Django time! We'll use pip to install Django, so run this in your
command line, making sure you're in your project folder and the virtual
environment is activated:

```
$ pip install Django==1.8.4
```
### Start git

We also want to start our version control system. Now that we're in our project
folder, run this command to start git:

```
$ git init
```

Running this command in your project folder will make the entire folder and its
contents part of a new Git repository. See the [Git tips page
here](https://github.com/limedaring/HelloWebApp/tree/master/git-tips).

### Start your Django project

We installed Django, now we can run the app.

## Set up your database

Django 1.7 has some fancypants utilities built in to keep your database (where
all your dynamic information is stored) managable. We need to run the initial
migration before we start the app, so in your top level folder (the one with manage.py in it), type this in:

```
$ python manage.py migrate
```

It's going to create your database automatically for you and port over some
information.

## Start your Django web app

Want to see if everything worked? In your terminal, head over to your top level
hellowebapp folder and run this command:

```
$ python manage.py runserver
```

...and you'll see the local Django development server starting, which'll serve
your project to your computer.

```
Validating models...

0 errors found
March 26, 2014 - 15:50:53
Django version 1.7.8, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Now just head to your favorite web browser and visit [http://127.0.0.1:8000](http://127.0.0.1:8000), where
you'll see the home page. 
