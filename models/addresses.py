from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from commons.sql_alchemy_base import Base

class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True)
    street_number = Column(String(50), nullable=False)
    zip_code = Column(String(50), nullable=False)
    city = Column(String(150), nullable=False)

    companies = relationship('Company', back_populates='address')
    employees = relationship('Employee', back_populates='address')

    def __str__(self):
        return f'{self.street_number}, {self.zip_code} {self.city}'
