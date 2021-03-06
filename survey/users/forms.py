from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField,FloatField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from survey.models import User



class RegistrationForm(FlaskForm):
    username = StringField('Username',
                                validators=[DataRequired(), Length(min=2,max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])

    role =  SelectField(
        'Role',
        choices=[('admin', 'Admin'), ('client', 'Client')] , validators=[DataRequired()]
    )
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(),EqualTo('password')])

    submit = SubmitField('Save')

    def validate_username(self,username):
        user = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError('Username is already taken')
    
    def validate_email(self,email):
        user = User.query.filter_by(email= email.data).first()
        if user:
            raise ValidationError('Email is already in use')



class LoginForm(FlaskForm):
   
    email = StringField('Email', validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired()])
    
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')



class RequestResetForm(FlaskForm):
   
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self,email):
        user = User.query.filter_by(email= email.data).first()
        if user is None:
            raise ValidationError('There is no account with this email')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(),EqualTo('password')])

    submit = SubmitField('Reset Password')


class SectorForm(FlaskForm):
   
    name = StringField('Sector', validators=[DataRequired()])

    submit = SubmitField('Submit')

class IndustryForm(FlaskForm):
   
    name = StringField('Industry Name', validators=[DataRequired()])
    sector =  SelectField(
        'Sector',
        choices=[('public', 'Public'), ('private', 'Private')] , validators=[DataRequired()]
    )

    submit = SubmitField('Submit')


class JobForm(FlaskForm):
   
    name = StringField('Job Title', validators=[DataRequired()])
    sector =  SelectField(
        'Sector',
        choices=[('public', 'Public'), ('private', 'Private')] , validators=[DataRequired()]
    )
    industry =  SelectField(
        'Industry',
        choices=[('banking', 'Banking'), ('mining', 'Mining')] , validators=[DataRequired()]
    )
    area =  SelectField(
        'Area of Operation',
        choices=[('public', 'Area 1'), ('private', 'Area 2')] , validators=[DataRequired()]
    )
   

    submit = SubmitField('Submit')

class AreaForm(FlaskForm):
   
    name = StringField('Area of Operation', validators=[DataRequired()])
    sector =  SelectField(
        'Sector',
        choices=[('public', 'Public'), ('private', 'Private')] , validators=[DataRequired()]
    )
    industry =  SelectField(
        'Industry',
        choices=[('banking', 'Banking'), ('mining', 'Mining')] , validators=[DataRequired()]
    )
    
   

    submit = SubmitField('Submit')



class ClientForm(FlaskForm):
   
    name = StringField('Registered Company Name', validators=[DataRequired()])
    reg = StringField('Company Registration Number', validators=[DataRequired()])
    financial_year_end = StringField('Financial Year End', validators=[DataRequired()])
    company_type = StringField('Company Type', validators=[DataRequired()])
    vat = StringField('VAT Number', validators=[DataRequired()])
    telephone = StringField('Telephone Number', validators=[DataRequired()])
    fax = StringField('Fax Number', validators=[DataRequired()])
    email = StringField('Email Address', validators=[DataRequired()])
    website = StringField('Website Address', validators=[DataRequired()])
    date_of_incorporation = StringField('Date of Incorporation', validators=[DataRequired()])
    country_of_incorporation = StringField('Country of Incorporation', validators=[DataRequired()])
    chairman_firstname = StringField(" Firstname", validators=[DataRequired()])
    chairman_lastname = StringField(" Lastname", validators=[DataRequired()])
    chairman_other_names = StringField(" Other Name", validators=[DataRequired()])
    chairman_email = StringField(" Email Address", validators=[DataRequired()])
    chairman_nationality = StringField(" Nationality", validators=[DataRequired()])
    chairman_phone = StringField(" Phone ", validators=[DataRequired()])
    key_firstname = StringField("Firstname", validators=[DataRequired()])
    key_lastname = StringField("Lastname", validators=[DataRequired()])
    key_other_names = StringField(" Other Name", validators=[DataRequired()])
    key_email = StringField(" Email Address", validators=[DataRequired()])
    key_nationality = StringField(" Nationality", validators=[DataRequired()])
    key_phone = StringField(" Phone Number", validators=[DataRequired()])
    ceo_firstname = StringField("Firstname", validators=[DataRequired()])
    ceo_lastname = StringField("Lastname", validators=[DataRequired()])
    ceo_other_names = StringField(" Other Name", validators=[DataRequired()])
    ceo_email = StringField(" Email Address", validators=[DataRequired()])
    ceo_nationality = StringField(" Nationality", validators=[DataRequired()])
    ceo_phone = StringField(" Phone Number", validators=[DataRequired()])

    current_auditor_name = StringField("Name", validators=[DataRequired()])
    current_auditor_address = StringField("Address", validators=[DataRequired()])
    current_auditor_city = StringField(" City", validators=[DataRequired()])
    current_auditor_country = StringField(" Country", validators=[DataRequired()])

    previous_auditor_name = StringField("Name", validators=[DataRequired()])
    previous_auditor_address = StringField("Address", validators=[DataRequired()])
    previous_auditor_city = StringField(" City", validators=[DataRequired()])
    previous_auditor_country = StringField(" Country", validators=[DataRequired()])


    company_secretary_name = StringField("Name", validators=[DataRequired()])
    company_secretary_address = StringField("Address", validators=[DataRequired()])
    company_secretary_city = StringField(" City", validators=[DataRequired()])
    company_secretary_country = StringField(" Country", validators=[DataRequired()])

    
    sector =  SelectField(
        'Sector',
        choices=[('public', 'Public'), ('private', 'Private')] , validators=[DataRequired()]
    )
    industry =  SelectField(
        'Industry',
        choices=[('banking', 'Banking'), ('mining', 'Mining')] , validators=[DataRequired()]
    )
    area =  SelectField(
        'Area of Operation',
        choices=[('public', 'Area 1'), ('private', 'Area 2')] , validators=[DataRequired()]
    )
    mailing_building = StringField('Street Line 1', validators=[DataRequired()])
    mailing_street = StringField('Street Line 2', validators=[DataRequired()])
    mailing_city = StringField('City/Town', validators=[DataRequired()])
    mailing_region = StringField('Region', validators=[DataRequired()])
    mailing_country = StringField('Country', validators=[DataRequired()])


    street_building = StringField('Building', validators=[DataRequired()])
    street_street = StringField('Street', validators=[DataRequired()])
    street_city = StringField('City/Town', validators=[DataRequired()])
    street_country = StringField('Country', validators=[DataRequired()])


    contact_firstname = StringField('Firstname', validators=[DataRequired()])
    contact_middlename = StringField('Middlename', validators=[DataRequired()])
    contact_lastname = StringField('Lastname', validators=[DataRequired()])
    job = StringField('Job Title', validators=[DataRequired()])
     
    # job =  SelectField(
    #     'Job Title',
    #     choices=[('manager', 'Manager'), ('associate', 'Associate')] , validators=[DataRequired()]
    # )
    email = StringField('Email Address', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired()])


   


    registration = StringField('Registration Number', validators=[DataRequired()])

    tax_id = StringField('Tax ID', validators=[DataRequired()])

    submit = SubmitField('Submit')





class SurveyForm(FlaskForm):
   
    base_salary = FloatField('Annual Base Salary (GHS)', validators=[DataRequired()])
    
    company_bonus_performance = FloatField('Company Performance Bonus', validators=[DataRequired()])
    individual_bonus_performance = FloatField('Individual Performance Bonus', validators=[DataRequired()])
    annual_bonus = FloatField('Annual Bonus', validators=[DataRequired()])
    incentive_bonus = FloatField('Incentive Bonus', validators=[DataRequired()])
    other_bonus = FloatField('Other bonus', validators=[DataRequired()])


    staff_bus = FloatField('Staff Bus', validators=[DataRequired()])
    company_car = FloatField('Company Car', validators=[DataRequired()])
    personal_travel = FloatField('Personal Travel', validators=[DataRequired()])
    petrol = FloatField('Petrol', validators=[DataRequired()])
    vehicle = FloatField('Vehicle', validators=[DataRequired()])
    driver = FloatField('Driver', validators=[DataRequired()])

    health_insurance = FloatField('Health', validators=[DataRequired()])
    medical_assistance = FloatField('Medical Assistance', validators=[DataRequired()])
    funeral_assistance = FloatField('Funeral Assistance', validators=[DataRequired()])
    life_insurance = FloatField('Life Insurance', validators=[DataRequired()])
    group_accident = FloatField('Group Personnel Accident', validators=[DataRequired()])


    club_membership = FloatField('Club Membership', validators=[DataRequired()])
    school_fees = FloatField('School fees (Paid by employer)', validators=[DataRequired()])
    vacation = FloatField('Vacation', validators=[DataRequired()])
    housing = FloatField('Housing', validators=[DataRequired()])
    telephone = FloatField('Telephone', validators=[DataRequired()])
    security = FloatField('Security', validators=[DataRequired()])
    other_benefits = FloatField('Other Benefits', validators=[DataRequired()])

    
    vehicle_maintenance = FloatField('Vehicle Maintenance', validators=[DataRequired()])
    allowance_vehicle = FloatField('Vehicle', validators=[DataRequired()])
    transport = FloatField('Transport', validators=[DataRequired()])
    fuel = FloatField('Fuel', validators=[DataRequired()])
    car = FloatField('Car', validators=[DataRequired()])
    allowance_driver = FloatField('Driver', validators=[DataRequired()])
    

    domestic = FloatField('Domestic Safety and Security', validators=[DataRequired()])
    allowance_housing = FloatField('Housing', validators=[DataRequired()])
    utilities = FloatField('Utilities', validators=[DataRequired()])
    meal = FloatField('Meal', validators=[DataRequired()])
    allowance_telephone = FloatField('Telephone', validators=[DataRequired()])


    entertainment = FloatField('Entertainment', validators=[DataRequired()])
    education = FloatField('Education', validators=[DataRequired()])
    vacation = FloatField('Vacation', validators=[DataRequired()])
    uniform = FloatField('Uniform', validators=[DataRequired()])
    mobile_money = FloatField('Mobile Money', validators=[DataRequired()])
    misc = FloatField('Miscellaneous', validators=[DataRequired()])
    

   
    
    


    



    submit = SubmitField('Submit')