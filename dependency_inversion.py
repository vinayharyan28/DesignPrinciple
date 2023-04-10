"""
Let's say you need to charge your phone. you would connect the adapter to
the socket and it is done. you wouldn't think about what is behind the wall
and details of how you get the electricity (I mean if you are not an electrical
engineer or something like that. that should be the case with your class too.
Your high level classes (such as activityStreamer) should depend upon abstraction/interface
not concrete classes. let give an example of bad practice.
"""


class Syslog:
    def write(self, msg):
        with open('path', 'a') as f:
            f.write(msg)


class EventStreamer:
    def __init__(self):
        self.event_stream = Syslog()

    def send_event(self, event):
        self.event_stream.write(event)


"""
What are the problems with that code?
What if the name of the write() method changes? 
This class could be from a library or could be a class from the other team. 
Now you had to change your code when they change too because you depend on a 
concrete class in your high-level class.

If we want to change the data destination for a different 
one or add new ones at runtime, we are also in trouble because 
we will find ourselves constantly modifying the stream() 
method to adapt it to these requirements.

How could we design our classes so that we could get rid of those problems?


"""

from abc import ABC, abstractmethod


class EventSender(ABC):
    @abstractmethod
    def send(self, event):
        pass


class Syslog1(EventSender):
    @staticmethod
    def write_(msg):
        with open('path', 'a') as f:
            f.write(msg)

    def send(self, event):
        self.write_(event)


class EventStreamer1:
    def __init__(self, sender):
        self.event_stream = sender

    def send_event(self, event_stream):
        self.event_stream.send(event_stream)


"""
Here we are depending on the abstraction using EventSender. whatever
subclass we get, we can just call send() method of this and we know that our
event will be sent to the true place. and if we wanted to change the destination, 
we can just create a different subclass and give it in the __init__() method of EventStreamer
"""