from typing import List
from sqlalchemy.orm import Session
from models.addresses import Address


class AddressManager():
    def __init__(self, session: Session) -> None:
        self.session = session

    def create_address(self, address: Address):
        # Izbjegavamo unos duplih podataka
        address_from_db = self.session.query(Address).filter_by(street_number=address.street_number).first()
        if address_from_db is None:
            self.session.add(address)
            self.session.commit()

    def get_address(self, id) -> Address:
        return self.session.query(Address).filter_by(id=id).first()
    
    def get_addresses(self, id) -> List[Address]:
        return self.session.query(Address).all()
    
    def update_address(self, id, new_address):
        address = self.session.query(Address).filter_by(id=id).first()
        address = new_address
        self.session.commit()

    def delete_address(self, id):
        address = self.session.query(Address).filter_by(id=id).first()
        self.session.delete(address)
        self.session.commit()
