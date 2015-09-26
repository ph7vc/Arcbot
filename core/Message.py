"""
    Class Name : MessageParser

    Description:
        Simple class to standardize message data

    Contributors:
        - Patrick Hennessy

    License:
        CL4M-B0T is free software: you can redistribute it and/or modify it
        under the terms of the GNU General Public License v3; as published
        by the Free Software Foundation
"""
import time

class messageType:
    MESSAGE = 0
    PRESSENCE = 1

class Envelope():
    def __init__(self, sender, channel, **kwargs):
        self.sender = sender
        self.channel = channel

        for key, value in kwargs.items():
            setattr(self, key, value)

class Message():
    def __init__(self, type, senderID, channelID, content=None, timestamp=time.time()):
        self.type = type
        self.timestamp = timestamp
        self.sender = senderID
        self.channel = channelID
        self.content = content

    def __call__(self):
        return Envelope(self.sender,self.channel)
