
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
import json
import time
import random

from twilio.rest import Client

# --------------------------- Initialization --------------------------------------------------

app = Flask(__name__)
ask = Ask(app, "/tricon_reception")


@app.route('/')
def homepage():
	return "Welcome to Tricon Reception !!!"


@ask.launch
def start_skill():
	welcome = render_template('welcome_message')
	return question(welcome)


employee_list = ['Vikash','Manish', 'Kanchan', 'Henry', 'Aisha']

employee_dict = {'Manish': '+12345678901',
				'Kanchan': '+12345678901',
				'Aisha': '+12345678901',
				'Henry': '+12345678901',
				'Vikash': '+12345678901' 
}


# ------------------- Phone Number Tricon -----------------------------

@ask.intent("GetNumberIntent")
def phone_info(name):
	number = employee_dict.get(name)
	print number
	ph_num=[]
	for i in range(2,12):
		ph_num.append(number[i]+'..')

	phone_num = render_template('phone_number', number = ph_num)
	return  question (phone_num)


# -------------------------------- Main Program ----------------------------------------------

@ask.intent("GetVisitorIntent")
def get_visitor(visitor):
	visitor_message = render_template('visitor_message', visitor = visitor)
	print visitor
	return  question (visitor_message)


@ask.intent("GetEmployeeIntent")
def final_response(person):
	if (person is None):
		NoResponse = render_template('no_response')
		return question(NoResponse)

	else:
		if (person in employee_list):
			WaitResponse = render_template('wait_response', person = person)
			print person			
			message = send_message(person)
			return question(WaitResponse)


		else:
			NoPerson = render_template('personNotFound')
			return question(NoPerson)


# ----------------------------- Tricon Information ---------------------
@ask.intent('AMAZON.CancelIntent')
@ask.intent('AMAZON.StopIntent')
@ask.intent('AMAZON.NoIntent')
def no_info():
	information = render_template('no_information')
	return statement(information)


def organization_info():
	information = render_template('organization_info')
	return  question (information)

def interesting_info1():
	int_information = render_template('interesting_info1')
	return  question (int_information)

def interesting_info2():
	int_information = render_template('interesting_info2')
	return  question (int_information)

def interesting_info3():
	int_information = render_template('interesting_info3')
	return  question (int_information)

def interesting_info4():
	int_information = render_template('interesting_info4')
	return  question (int_information)


information_list = [organization_info, interesting_info1, interesting_info2, interesting_info3, interesting_info4] 

@ask.intent("AMAZON.YesIntent")
def random_info():
	return random.choice(information_list)()



#------------------- Send message using Twilio -----------------------
#you should be keeping all of this in a separate file as a gitignore file
# Your Account SID from twilio.com/console

account_sid = "your_account_sid"

# Your Auth Token from twilio.com/console
auth_token  = "your_auth_token"

client = Client(account_sid, auth_token)

def send_message(person):
	message = client.messages.create(
		to = employee_dict[person],
		from_="+19284874266",
     	body= "Someone is here to meet you at Tricon Reception"
     	)


if __name__ == '__main__':
	app.run(debug=True)

