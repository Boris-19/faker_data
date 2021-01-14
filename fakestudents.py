from faker import Faker
from random import randint
import time
import datetime

fake = Faker('en-GB')

courses_list = ['Computing', 'IT', 'ICT','Business', 'Applied Law', 'Intro to Business', 'Introduction to Hospitality', 'Culinary Skills', 'Barbering', 'Hairdressing', 'Hairdressing & Barbering', 'Beauty Therapy', 'Art & Design','Creative Media', 'Film, Photography & Media', 'Interactive Media', 'Creative Media Skills', 'Performing Arts Practice', 'Music Technology', 'Music', 'Music Production', 'Music Industry Skills', ]

providers_list = ['BTEC','C&G','Restart','T-Level','Adv. Apprenticeship']



def generate_streetaddress():
    address = fake.street_address()
    address = address.replace('\n',' ')
    return address




def generateFakeStudents():
    output = "student_id,firstname,surname,age,dob,address1,address2,postcode,phone,email"
    for x in range(0,3000):
        output += ("\n"+fake.ean(prefixes=('3', ),length=8)+","
            +fake.first_name()+","
            +fake.last_name()+","
            +str(randint(16,30))+","
            +str(fake.date_of_birth(None,16,30))+","
            +generate_streetaddress()+","
            +fake.county()+","
            +fake.postcode()+","
            +fake.cellphone_number()+","
            +fake.ascii_email())           
            
            
           
    print(output)
    f= open("fakestudent.csv","w")
    f.write(output)
    f.close

def generateFakeCourse():

    
    output = "coursecode,coursetitle,hours,level,courselength,startdate,courseleader"
    
    for x in range(0,100):
        level = str(fake.random_int(1,4))
        course = fake.word(ext_word_list=courses_list)
        provider = fake.word(ext_word_list=providers_list)
        output += ("\n"+fake.bothify(text='??###?',letters='ABCDEF')+","  
        +provider+" Level "+level+" "+course+","    #Couse Title
        +str(fake.random_int(0,30))+","    #Hours per week
        +level+","     #Level of course
        +str(fake.random_int(4,52))+","    #Course Length in Weeks
        +str(fake.date_between_dates(datetime.date(2021,1,1),datetime.date(2021,6,30)))+","    #start date
        +fake.first_name()+" "+fake.last_name())


    print("\n"+output)
    f= open("fakecourse.csv","w")
    f.write(output)
    f.close

generateFakeStudents()
generateFakeCourse()
