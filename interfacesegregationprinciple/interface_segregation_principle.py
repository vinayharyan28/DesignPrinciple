"""
Interface segregation Principle
Instead of method fat interface, create interfaces as small as possible based on a
group of methods each one serving one submodule. for example this is bad example.
"""

from abc import ABCMeta, abstractmethod


class EventParser(metaclass=ABCMeta):
    @abstractmethod
    def from_xml(self, xml_data):
        """Parse an event from XML"""

    @abstractmethod
    def from_json(self, json_data):
        """Parse an event from JSON"""


"""
why this is bad? Because what if a class that implements this interface
doesn't need to use the from_json method? here we force a class to implement an 
interface they dont want to use. the true approach is to create 2 different interface 
for those function

"""


class XMLEventParser(metaclass=ABCMeta):
    @abstractmethod
    def from_xml(self, xml_data):
        """Parse an event from XML"""


class JSONEventParser(metaclass=ABCMeta):
    @abstractmethod
    def from_json(self, json_data):
        """Parse an event from JSON"""
