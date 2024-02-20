from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from commons.sql_alchemy_base import Base


class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    last_name = Column(String(50), nullable=False)
    first_name = Column(String(50), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    phone = Column(String(50))
    website = Column(String(250))

    address_id = Column(Integer, ForeignKey('addresses.id'))
    address = relationship('Address', back_populates='employees')

    company_id = Column(Integer, ForeignKey('companies.id'))
    company = relationship('Company', back_populates='employees')

    def __str__(self):
        return f'{self.last_name} {self.first_name}'
