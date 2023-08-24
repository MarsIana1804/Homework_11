from collections import UserDict
from datetime import datetime
import re

class Field:
    def __init__(self, val: str):
        self.__value = None 
        self.value = val

    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, new_val):
        self.__value = new_val

class Name(Field):
    pass

class Phone(Field):

    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, new_val):
        valid_phone_number = self.set_value(new_val)
        if valid_phone_number:
            self.__value = valid_phone_number

    def set_value(self, new_phone):
        phone_pattern = re.compile(r'\+\d{11}|\+\d{12}')
        if not phone_pattern.match(new_phone):
            raise ValueError("Incorrect number format. Use format '+12345678901' or '+123456789012.")
        else:
            return phone_pattern.match(new_phone).group()
        

class Birthday(Field):

    @property
    def value(self):
        return self.__value

    @value.setter  
    def value(self, new_value):
        valid_date = self.set_value(new_value)
        if valid_date:
            self.__value = valid_date

    def set_value(self, new_val):
        
        date_pattern = re.compile(r'\d{2}-\d{2}-\d{4}')
        if not date_pattern.match(new_val):
            raise ValueError("Incorrect date format. Use format 'DD-MM-YYYY'.")
         
        current_date = datetime.now().date()
        input_date = datetime.strptime(new_val, "%d-%m-%Y").date()
        
        if input_date > current_date:
            raise ValueError("Birthday date can't be in the future.")
        
        else:
            return input_date
    


class Record():

    def __init__(self, n: Name, ph: Phone=None, b: Birthday=None) -> None:
        self.name = n
        self.phones = []

        if ph:
            self.add_phone_object(ph)

        if b:
            self.birthday = b
            print(self.birthday.value)

    def days_to_birthday(self):

        self.current_datetime = datetime.now().date()
        #self.b_date = b_date
        #self.birthday_dt = datetime.strptime(self.b_date, "%d.%m.%Y").date()
        self.birthday_dt = self.birthday.value.replace(year=self.current_datetime.year)

        self.days_to = self.birthday_dt - self.current_datetime
        self.total_seconds = self.days_to.total_seconds()
        self.total_seconds = int(self.total_seconds)
        self.days_from_total_seconds = self.total_seconds / (60 * 60 * 24)

        if int(self.days_from_total_seconds) < 0:
            self.birthday_dt = self.birthday_dt.replace(year=self.current_datetime.year + 1)
            self.days_to = self.birthday_dt - self.current_datetime
            return self.days_to
        else:
            self.birthday_dt = self.birthday_dt.replace(year=self.current_datetime.year)
            self.days_to = self.birthday_dt - self.current_datetime
            return self.days_to
            
        

    def add_phone_object(self, ph_n: Phone):
        self.phones.append(ph_n)
    
    def remove_phone_obj(self, phone_obj: Phone):
        self.phones.remove(phone_obj)

    def edit_phone_obj(self, new_number: str, i):
        self.phones[i].value = new_number
  
    def __str__(self): 
        return f"{self.name.value} {[ph.value for ph in self.phones]} {self.birthday.value}"


class AddressBook(UserDict):
    def add_record(self, rec: Record):
        self.data[rec.name] = rec

    def __iter__(self):
        return self.rec_generator(3)  # Set the batch size (3 in this example)

    def rec_generator(self, N):
        records = list(self.data.values())
        for i in range(0, len(records), N):
            yield records[i:i + N]


if __name__ == '__main__':
    name = Name('Bill')
    phone = Phone('+12345678901')
    new_phone = Phone('+36367647637')
    phone_number3 = Phone('+55555555555')
    bd = Birthday("22-05-1990")
    rec = Record(name, phone, bd)
    print(name)
    print(phone)
    print(bd)
    print(rec)
    print(rec.days_to_birthday())
    rec.add_phone_object(new_phone)
    print(rec.phones)
    print(rec.phones[1].value)
    rec.edit_phone_obj('+380936007646', 1)
    print(rec.phones[1].value)
    rec.remove_phone_obj(new_phone)
    print(rec.phones)



    








