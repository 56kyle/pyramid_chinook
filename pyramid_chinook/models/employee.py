from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    ForeignKey,
    DateTime,
)

from sqlalchemy.orm import relationship
from .meta import Base


class Employee(Base):
    __tablename__ = 'Employee'
    EmployeeId = Column(Integer, primary_key=True)
    LastName = Column(Text)
    FirstName = Column(Text)
    Title = Column(Text)
    ReportsTo = Column(ForeignKey('Employee.EmployeeId'))
    BirthDate = Column(DateTime)
    HireDate = Column(DateTime)
    Address = Column(Text)
    City = Column(Text)
    State = Column(Text)
    Country = Column(Text)
    PostalCode = Column(Text)
    Phone = Column(Text)
    Fax = Column(Text)
    Email = Column(Text)



