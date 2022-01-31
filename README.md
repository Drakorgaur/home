# INSTALLATION

### Requirements

> `docker` and `docker-compose` needed to be installed

### Steps to install

1. Clone git repository `git clone git@github.com:Drakorgaur/home.git`
2. You need to get `.env` file. Contact collaborator to get it.  
4. Make migrations
   1. Prepare django migrations `docker-compose exec web python manage.py makemigrations`
   2. Migrate `docker-compose exec web python manage.py migrate`
5. (Optional) Create superuser `docker-compose exec web python manage.py createsuperuser` and follow it steps

### Run

>docker-compose up -d
> 

# Setting new module up
1. Run dc command `docker-compose run -w /app/home/modules/ web django-admin startapp <app_name>`
> Change permission for this folder on your local device.  
> `sudo chown -R $USER:$USER .`
2. Add next files to module:
   * urls.py
   * forms.py
3. Add next directories:
   * templates 
   * static
4. Include app in settings in `INSTALLED_APPS` add to bottom `home.modules.<app_name>`
5. Include app urls to global urls. In `source/urls.py` add  
    `path('<app_name>/', include('home.modules.<app_name>.urls')),`

   

User
---
---

#### Guest
Guest is user that will be registered in system but do not live in apartment.
Guest's name filed is required
Guest should be used in registration of some events/activities, for example - poker-night.
Guest have no specific permissions and nothing on duty.

#### Inhabitant
Inhabitant is an object that presents a person in apartment.
Inhabitant's name filed is required
Email is not required for this model. In case person didn't provide and didn't confirm email and forgot an password/email, 
person should ask admin for help.
Inhabitant have things on duty to clean up, cook or etc.
Inhabitant can create events, registrate guests, new duties, lists to buy etc.



# Modules

---
---

## Welcome

Welcome module is responsible for **user authentication** and providing  
information about the site

---

## Home

Home module is core module. This one is responsible for virtual rooms and interaction between inhabitants in them.

## Room
Room object describes apartment(have it's **Name**) and contain several modules:
* Finance
* Events
* Cleaning up
* Plans/Upgrade
* Rules

### Finance
Finance module is created to follow all bills including rent-pay and shop-payments.
Finance module contain sections:
* To buy
* Bought
* Debts
* Rent

#### To buy and Bought
*To buy* and *Bought* sections use one model, which has different status of argument *isBought*

#### Debt
Debts between inhabitants

#### Rent
Rent section contain only one unique regular bill - rent for appartment

---

### Events
Events module is created to collect information about activities is planned to be runned in appartment.

---

### Cleaning
Cleaning module is dedicated to divide duties between inhabitants

---

### Plans/Upgrade
Module to write some interesting thoughts to improve life for you and tour room-mates

---

### Rules
Summary of rules to live in 