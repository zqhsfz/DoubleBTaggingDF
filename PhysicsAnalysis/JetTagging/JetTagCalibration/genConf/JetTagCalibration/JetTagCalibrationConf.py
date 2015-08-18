#Tue Aug 18 16:39:31 2015"""Automatically generated. DO NOT EDIT please"""
from GaudiKernel.GaudiHandles import *
from GaudiKernel.Proxy.Configurable import *

class Analysis__CalibrationBroker( ConfigurableAlgTool ) :
  __slots__ = { 
    'MonitorService' : 'MonitorSvc', # str
    'OutputLevel' : 7, # int
    'AuditTools' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'AuditFinalize' : False, # bool
    'EvtStore' : ServiceHandle('StoreGateSvc'), # GaudiHandle
    'DetStore' : ServiceHandle('StoreGateSvc/DetectorStore'), # GaudiHandle
    'UserStore' : ServiceHandle('UserDataSvc/UserDataSvc'), # GaudiHandle
    'folderRoot' : '/GLOBAL/BTagCalib/', # str
    'folders' : [  ], # list
    'channels' : [  ], # list
    'channelAliases' : [  ], # list
    'shadowFoldersAndChannels' : True, # bool
    'singleFolderName' : 'RUN12', # str
    'recreateHistoMap' : False, # bool
  }
  _propertyDocDct = { 
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(Analysis__CalibrationBroker, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'JetTagCalibration'
  def getType( self ):
      return 'Analysis::CalibrationBroker'
  pass # class Analysis__CalibrationBroker
