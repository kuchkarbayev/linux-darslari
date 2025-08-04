from faker import Faker    

def generate_fake_data():
    fake = Faker()
        
    return {
        "name": fake.name(),
        "country": fake.country(),
        "city": fake.city(),
        "card": fake.credit_card_number(card_type='visa'),
        "month": fake.credit_card_expire(start="now", end="+10y", date_format="%m"),
        "year": fake.credit_card_expire(start="now", end="+10y", date_format="%Y"),
        "email": fake.email(),
        "message": fake.emoji(),
        "username": fake.user_name()
    }