How to run the Alexa Skill
_____________________________________________________________________________________

Skill Information: 

Name your Alexa Skill to start it on a device or echosim.io (Eg: Tricon Bot)

---------------------------------------
Interaction Model:

Intent Schema:

{
  "intents": [
    {
      "slots": [
        {
          "name": "visitor",
          "type": "AMAZON.US_FIRST_NAME"
        }
      ],
      "intent": "GetVisitorIntent"
    },
    {
      "slots": [
        {
          "name": "person",
          "type": "LIST_OF_EMPLOYEE"
        }
      ],
      "intent": "GetEmployeeIntent"
    },
    {
      "intent": "AMAZON.YesIntent"
    },
    {
      "slots": [
        {
          "name": "name",
          "type": "NAME_OF_EMPLOYEE"
        }
      ],
      "intent": "GetNumberIntent"
    }
  ]
}



Add Slot types:

LIST_OF_EMPLOYEE 

manish
kanchan
henry
aisha
vikash


NAME_OF_EMPLOYEE

manish
kanchan
henry
aisha
vikash


Sample Utterances:

GetVisitorIntent {visitor}
GetVisitorIntent I am {visitor}
GetVisitorIntent My name is {visitor}
GetEmployeeIntent {person}
GetEmployeeIntent I want to talk to {person}
GetEmployeeIntent I am here to meet {person}
GetEmployeeIntent {person} called me to meet
GetEmployeeIntent I have a meeting with {person}
AMAZON.YesIntent Sure
AMAZON.YesIntent Yes
GetNumberIntent {name} phone number
GetNumberIntent Can you tell me {name} phone number
GetNumberIntent Tell me {name} number
GetNumberIntent Give me {name}  number
GetNumberIntent  What is {name} phone number
GetNumberIntent  can i get {name}  number

-------------------------------------------------------

Configuration:

Service Endpoint Type --> HTTPS

and copy paste your ngrok link htts://123xyz.io/tricon_recption and rest everything is default

----------------------------------------------------------

SSL Certificate:

Certificate for NA Endpoint:

select (My development endpoint is a sub-domain of a domain that has a wildcard certificate from a certificate authority )

Rest everyting can be left blank.

