# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.6.0b2 (default, Oct 11 2016, 05:27:10) 
# [GCC 6.2.0 20161005]
# Embedded file name: type_Params.py
from types import *
PARAMS_TYPE_UNKNOWN = 0
PARAMS_TYPE_STATUS = 1
PARAMS_TYPE_VERSION = 2
PARAMS_TYPE_ADAPTERS = 3

class Params:

    def __init__(self):
        self.__dict__['type'] = 0
        self.__dict__['driver'] = ''

    def __getattr__(self, name):
        if name == 'type':
            return self.__dict__['type']
        if name == 'driver':
            return self.__dict__['driver']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'type':
            self.__dict__['type'] = value
        elif name == 'driver':
            self.__dict__['driver'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU8(MSG_KEY_PARAMS_TYPE, self.__dict__['type'])
        submsg.AddStringUtf8(MSG_KEY_PARAMS_DRIVER, self.__dict__['driver'])
        mmsg.AddMessage(MSG_KEY_PARAMS, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_PARAMS, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['type'] = submsg.FindU8(MSG_KEY_PARAMS_TYPE)
        self.__dict__['driver'] = submsg.FindString(MSG_KEY_PARAMS_DRIVER)