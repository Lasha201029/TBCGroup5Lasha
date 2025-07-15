from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, DateField, RadioField, SubmitField, SelectField
from flask_wtf.file import FileField, FileRequired
from wtforms.validators import DataRequired, equal_to




class RegisterForm(FlaskForm) :
    name = StringField( "აირჩიე სახელი", validators=[DataRequired()])
    password = PasswordField("მოიფიქრე პაროლი", validators=[DataRequired()])
    repeat_password = PasswordField("გაიმეორე პაროლი", validators=[DataRequired(), equal_to("password")])
    birthday = DateField("მონიშნე დაბადების თარიღი")
    gender = RadioField("აირჩიე სქესი", choices = [("კაცი", "კაცი"), ("ქალი", "ქალი")])
    country = SelectField("აირჩიე ქვეყანა", choices = [ ("საქართველო", "საქართველო"), ("ამერიკა", "ამერიკა"),("ესპანეთი", "ესპანეთი"),("საფრანგეთი",  "საფრანგეთი"),("გერმანია", "გერმანია"), ("რუსეთი", "რუსეთი"), ("სხვა", "სხვა")] )
    submit = SubmitField("register")
    submits = SubmitField("save")

class EditRegisterForm(FlaskForm) :
    name = StringField( "აირჩიე სახელი", validators=[DataRequired()])
    password = PasswordField("მოიფიქრე ახალი პაროლი", validators=[DataRequired()])
    birthday = DateField("მონიშნე  ახალი დაბადების თარიღი")
    gender = RadioField("აირჩიე სქესი", choices = [("კაცი", "კაცი"), ("ქალი", "ქალი")])
    country = SelectField("აირჩიე ქვეყანა", choices = [ ("საქართველო", "საქართველო"), ("ამერიკა", "ამერიკა"),("ესპანეთი", "ესპანეთი"),("საფრანგეთი",  "საფრანგეთი"),("გერმანია", "გერმანია"), ("რუსეთი", "რუსეთი"), ("სხვა", "სხვა")] )
    role = RadioField("აირჩიე როლი" , choices=["admin", "moderator", "guest" ])
    submits = SubmitField("save")

class LoginForm(FlaskForm):
    name = StringField("აირჩიე სახელი", validators=[DataRequired()])
    password = PasswordField("მოიფიქრე პაროლი", validators=[DataRequired()])
    submits = SubmitField("login")


class CardForm(FlaskForm):
    name = StringField("აირჩიე სახელი", validators=[DataRequired()])
    img = FileField("აირჩიე ფოტო", validators=[FileRequired()])
    link = StringField("აირჩიე ლინკი", validators=[DataRequired()])
    submit = SubmitField("addcard")

class EditCardForm(FlaskForm):
    name = StringField("აირჩიე სახელი", validators=[DataRequired()])
    img = FileField("აირჩიე ფოტო", validators=[FileRequired()])
    part = StringField("აირჩიე კუთხე", validators=[DataRequired()])
    submit = SubmitField("addcard")
    submits = SubmitField("edit card")

class AddCardForm(FlaskForm):
    name = StringField("აირჩიე სახელი", validators=[DataRequired()])
    part = SelectField("აირჩიე კუთხე", coerce=str, validators=[DataRequired()])
    img = FileField("აირჩიე ფოტო", validators=[FileRequired()])
    submit = SubmitField("addcard")
