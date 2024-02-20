from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from commons.sql_alchemy_base import Base


class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)

    address_id = Column(Integer, ForeignKey('addresses.id'))
    address = relationship('Address', back_populates='companies')

    employees = relationship('Employee', back_populates='company')


    def __str__(self):
        return f'{self.name}'