from sqlalchemy import Column, Integer, String, Sequence, VARCHAR, TEXT, Text, SmallInteger
from utilities.databases import Base


class Student(Base):
    __tablename__ = "studentB"

    StudentID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    Name = Column(String, index=True)
    Email = Column(String, index=True)
    Password = Column(String, index=True)


class Registration(Base):
    __tablename__ = "registrationB"

    RegistrationID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    StudentID = Column(Integer, index=True)
    EventID = Column(VARCHAR, index=True)


class Notification(Base):
    __tablename__ = "notificationB"

    NotificationID = Column(Integer, primary_key=True, index=True, nullable=False)
    EventID = Column(VARCHAR, index=True)
    StudentID = Column(Integer, index=True)
    Email = Column(TEXT, index=True)
    Message = Column(TEXT, index=True)
    Sent = Column(SmallInteger, index=True)


class Event(Base):
    __tablename__ = "eventB"

    id = Column(VARCHAR, primary_key=True, index=True)
    organizationName = Column(VARCHAR, index=True)
    organizationNames = Column(VARCHAR, index=True)
    name = Column(VARCHAR, index=True)
    description = Column(String, index=True)
    categoryNames = Column(VARCHAR, index=True)
    location = Column(VARCHAR, index=True)
    startsOn = Column(VARCHAR, index=True)
    endsOn = Column(VARCHAR, index=True)
    theme = Column(VARCHAR, index=True)
    benefitNames = Column(VARCHAR, index=True)
    institutionId = Column(VARCHAR, index=True)
    organizationId = Column(VARCHAR, index=True)
    organizationIds = Column(VARCHAR, index=True)
    OrganizationProfilePicture = Column(VARCHAR, index=True)
    branchId = Column(VARCHAR, index=True)
    imagePath = Column(VARCHAR, index=True)
    visibility = Column(VARCHAR, index=True)
    status = Column(VARCHAR, index=True)
    searchScore = Column(VARCHAR, index=True)
