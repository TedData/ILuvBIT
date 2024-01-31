from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email

class AddForm(FlaskForm):
    V_ID = StringField('Car_ID', validators=[DataRequired()])
    B_ID = SelectField('Model', validators=[DataRequired()],choices=[('X1', 'X1'), ('X2', 'X2'), ('X3', 'X3'), ('X4', 'X4'), ('X5', 'X5')])
    Model = SelectField('Model', validators=[DataRequired()],choices=[('AUTO', 'AUTO'), ('HAND', 'HAND')])
    Kilometers = StringField('Kilometers', validators=[DataRequired()])
    Price = StringField('Price', validators=[DataRequired()])
    C_Year = StringField('Year', validators=[DataRequired()])
    Accident = SelectField('Accident', validators=[DataRequired()],choices=[('N', 'N'), ('Y', 'Y')])
    Car_brand = StringField('Brand', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

class SelectForm(FlaskForm):
    Model = SelectField('Model', choices=[], coerce=int)
    V_ID = SelectField('V_ID', choices=[], coerce=int)
    Location = SelectField('Location', choices=[], coerce=int)
    Car_brand = SelectField('Car_brand', choices=[], coerce=int)
    submit = SubmitField('Submit')

class DeleteForm(FlaskForm):
    V_ID = SelectField('V_ID', choices=[], coerce=int)
    submit = SubmitField('Submit')

class DeleteCascadeForm(FlaskForm):
    B_ID = SelectField('B_ID', choices=[], coerce=int)
    submit = SubmitField('Submit')

class ModifyForm(FlaskForm):
    V_ID = SelectField('V_ID', choices=[], coerce=int)
    B_ID = SelectField('Model', validators=[DataRequired()],choices=[('X1', 'X1'), ('X2', 'X2'), ('X3', 'X3'), ('X4', 'X4'), ('X5', 'X5')])
    Model = SelectField('Model', validators=[DataRequired()],choices=[('AUTO', 'AUTO'), ('HAND', 'HAND')])
    Kilometers = StringField('Kilometers', validators=[DataRequired()])
    Price = StringField('Price', validators=[DataRequired()])
    C_Year = StringField('Year', validators=[DataRequired()])
    Accident = SelectField('Accident', validators=[DataRequired()],choices=[('N', 'N'), ('Y', 'Y')])
    Car_brand = StringField('Brand', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

class BookForm(FlaskForm):
    V_ID = SelectField('V_ID', choices=[], coerce=int)
    Name = StringField('Name', validators=[DataRequired()])
    Phone_No = StringField('Phone_No', validators=[DataRequired()])
    Email = StringField('Email', validators=[Email()])
    submit = SubmitField('Sign Up')

class PasswordForm(FlaskForm):
    Password = StringField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')