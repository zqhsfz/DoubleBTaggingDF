#Tue Aug 18 16:40:18 2015"""Automatically generated. DO NOT EDIT please"""
from GaudiKernel.GaudiHandles import *
from GaudiKernel.Proxy.Configurable import *

class DerivationFramework__JetAugmentationTool( ConfigurableAlgTool ) :
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
    'MomentPrefix' : 'DFCommonJets_', # str
    'InputJets' : 'AntiKt4EMTopoJets', # str
    'CalibMomentKey' : 'Calib', # str
    'JetCalibTool' : PublicToolHandle(''), # GaudiHandle
  }
  _propertyDocDct = { 
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(DerivationFramework__JetAugmentationTool, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DerivationFrameworkJetEtMiss'
  def getType( self ):
      return 'DerivationFramework::JetAugmentationTool'
  pass # class DerivationFramework__JetAugmentationTool

class DerivationFramework__JetDecorAlg( ConfigurableAlgorithm ) :
  __slots__ = { 
    'OutputLevel' : 0, # int
    'Enable' : True, # bool
    'ErrorMax' : 1, # int
    'ErrorCount' : 0, # int
    'AuditAlgorithms' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditReinitialize' : False, # bool
    'AuditRestart' : False, # bool
    'AuditExecute' : False, # bool
    'AuditFinalize' : False, # bool
    'AuditBeginRun' : False, # bool
    'AuditEndRun' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'MonitorService' : 'MonitorSvc', # str
    'RegisterForContextService' : False, # bool
    'EvtStore' : ServiceHandle('StoreGateSvc'), # GaudiHandle
    'DetStore' : ServiceHandle('StoreGateSvc/DetectorStore'), # GaudiHandle
    'UserStore' : ServiceHandle('UserDataSvc/UserDataSvc'), # GaudiHandle
    'InputCollection' : '', # str
    'MomentsToCopy' : [  ], # list
  }
  _propertyDocDct = { 
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(DerivationFramework__JetDecorAlg, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DerivationFrameworkJetEtMiss'
  def getType( self ):
      return 'DerivationFramework::JetDecorAlg'
  pass # class DerivationFramework__JetDecorAlg
