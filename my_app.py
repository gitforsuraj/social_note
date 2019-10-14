from flask import Flask, render_template  
from flask_materialize import Material  
from flask_wtf import Form, RecaptchaField
from flask_wtf.file import FileField
from wtforms import TextField, HiddenField, ValidationError, RadioField,\
    BooleanField, SubmitField, IntegerField, FormField, validators
from wtforms.validators import Required

app = Flask(__name__)  
Material(app)  
app.config['SECRET_KEY'] = 'USE-YOUR-OWN-SECRET-KEY-DAMNIT'
app.config['RECAPTCHA_PUBLIC_KEY'] = 'TEST'

todo_items = ['todo1', 'todo222','just simple to do']

ButtonPressed = 0

# straight from the wtforms docs:
class TelephoneForm(Form):
    country_code = IntegerField('Country Code', [validators.required()])
    area_code = IntegerField('Area Code/Exchange', [validators.required()])
    number = TextField('Number')

class ExampleForm(Form):
    field1 = TextField('First Field', description='This is field one.')
    field2 = TextField('Second Field', description='This is field two.',
                       validators=[Required()])
    hidden_field = HiddenField('You cannot see this', description='Nope')
    recaptcha = RecaptchaField('A sample recaptcha field')
    radio_field = RadioField('This is a radio field', choices=[
        ('head_radio', 'Head radio'),
        ('radio_76fm', "Radio '76 FM"),
        ('lips_106', 'Lips 106'),
        ('wctr', 'WCTR'),
    ])
    checkbox_field = BooleanField('This is a checkbox',
                                  description='Checkboxes can be tricky.')

    # subforms
    mobile_phone = FormField(TelephoneForm)

    # you can change the label as well
    office_phone = FormField(TelephoneForm, label='Your office phone')

    ff = FileField('Sample upload')

    submit_button = SubmitField('Submit Form')


    def validate_hidden_field(form, field):
        raise ValidationError('Always wrong')

@app.route('/',methods=["GET", "POST"])  
def my_app():
    form = ExampleForm()   
    global ButtonPressed
    ButtonPressed += 1
    return render_template('home.html', ButtonPressed = ButtonPressed,form = form, todo_items = todo_items)  

if __name__ == '__main__':  
    app.run(debug = True)  

@app.route("/forward/")
def move_forward():
    #Moving forward code
    forward_message = "Moving Forward..."
    print(forward_message)
    return 'nothing'
    #return render_template('index.html', forward_message=forward_message);