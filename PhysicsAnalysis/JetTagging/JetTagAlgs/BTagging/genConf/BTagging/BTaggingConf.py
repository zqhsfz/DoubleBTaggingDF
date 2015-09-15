#Mon Sep 14 21:25:47 2015"""Automatically generated. DO NOT EDIT please"""
from GaudiKernel.GaudiHandles import *
from GaudiKernel.Proxy.Configurable import *

class Analysis__BTagJetPtScaling( ConfigurableAlgTool ) :
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
    'PtScalingConstPar' : 8000.00, # float
    'PtScalingLinearPar' : 1.40000, # float
  }
  _propertyDocDct = { 
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'PtScalingLinearPar' : """ track jet to calorimeter jet pt scale """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
    'PtScalingConstPar' : """ offset for track jet to calorimeter jet pt scaling """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(Analysis__BTagJetPtScaling, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'BTagging'
  def getType( self ):
      return 'Analysis::BTagJetPtScaling'
  pass # class Analysis__BTagJetPtScaling

class Analysis__BTagLabeling( ConfigurableAlgTool ) :
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
    'JetTruthMatchTool' : PublicToolHandle('Analysis::JetQuarkLabel'), # GaudiHandle
  }
  _propertyDocDct = { 
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(Analysis__BTagLabeling, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'BTagging'
  def getType( self ):
      return 'Analysis::BTagLabeling'
  pass # class Analysis__BTagLabeling

class Analysis__BTagSecVertexing( ConfigurableAlgTool ) :
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
    'PrimaryVertexName' : 'PrimaryVertices', # str
    'SecVtxFinderList' : PublicToolHandleArray([]), # GaudiHandleArray
    'SecVtxFinderTrackNameList' : [  ], # list
    'SecVtxFinderxAODBaseNameList' : [  ], # list
    'JetFitterVariableFactory' : PublicToolHandle('Analysis::JetFitterVariablesFactory'), # GaudiHandle
    'MSVVariableFactory' : PublicToolHandle('Analysis::MSVVariablesFactory'), # GaudiHandle
  }
  _propertyDocDct = { 
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(Analysis__BTagSecVertexing, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'BTagging'
  def getType( self ):
      return 'Analysis::BTagSecVertexing'
  pass # class Analysis__BTagSecVertexing

class Analysis__BTagTool( ConfigurableAlgTool ) :
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
    'PrimaryVertexName' : 'PrimaryVertices', # str
    'TagToolList' : PublicToolHandleArray([]), # GaudiHandleArray
    'BaselineTagger' : 'IP3D+SV1', # str
    'Runmodus' : 'analysis', # str
    'BTagLabelingTool' : PublicToolHandle('Analysis::BTagLabeling'), # GaudiHandle
  }
  _propertyDocDct = { 
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(Analysis__BTagTool, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'BTagging'
  def getType( self ):
      return 'Analysis::BTagTool'
  pass # class Analysis__BTagTool

class Analysis__BTagTrackAssociation( ConfigurableAlgTool ) :
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
    'BTagAssociation' : True, # bool
    'TrackToJetAssociatorList' : PublicToolHandleArray([]), # GaudiHandleArray
    'ElectronToJetAssociatorList' : PublicToolHandleArray([]), # GaudiHandleArray
    'MuonToJetAssociatorList' : PublicToolHandleArray([]), # GaudiHandleArray
    'TrackToJetAssocNameList' : [  ], # list
    'ElectronToJetAssocNameList' : [  ], # list
    'PhotonToJetAssocNameList' : [  ], # list
    'MuonToJetAssocNameList' : [  ], # list
    'TrackContainerNameList' : [  ], # list
    'ElectronContainerNameList' : [  ], # list
    'PhotonContainerNameList' : [  ], # list
    'MuonContainerNameList' : [  ], # list
  }
  _propertyDocDct = { 
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(Analysis__BTagTrackAssociation, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'BTagging'
  def getType( self ):
      return 'Analysis::BTagTrackAssociation'
  pass # class Analysis__BTagTrackAssociation

class Analysis__JetBTaggerTool( ConfigurableAlgTool ) :
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
    'BTagTool' : PublicToolHandle('Analysis::IBTagTool'), # GaudiHandle
    'BTagName' : '', # str
    'BTagTrackAssocTool' : PublicToolHandle('Analysis::BTagTrackAssociation'), # GaudiHandle
    'BTagSVName' : '', # str
    'BTagJFVtxName' : '', # str
    'BTagSecVertexing' : PublicToolHandle('Analysis::BTagSecVertexing'), # GaudiHandle
    'BTagAugmentation' : False, # bool
    'BTagJetPtRescale' : False, # bool
    'MagFieldSvc' : ServiceHandle('AtlasFieldSvc'), # GaudiHandle
  }
  _propertyDocDct = { 
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'BTagAugmentation' : """ switch to decide whether to merely extend the BTagging information as opposed to re-tagging from scratch """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
    'BTagJetPtRescale' : """ switch to decide whether to carry out jet pt rescaling (to use calorimeter jet tunings for track jets) """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(Analysis__JetBTaggerTool, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'BTagging'
  def getType( self ):
      return 'Analysis::JetBTaggerTool'
  pass # class Analysis__JetBTaggerTool

class Analysis__StandAloneJetBTaggerAlg( ConfigurableAlgorithm ) :
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
    'JetBTaggerTool' : PublicToolHandle('Analysis::JetBTaggerTool'), # GaudiHandle
    'JetCollectionName' : '', # str
    'outputCollectionSuffix' : '', # str
  }
  _propertyDocDct = { 
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'RegisterForContextService' : """ The flag to enforce the registration for Algorithm Context Service """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(Analysis__StandAloneJetBTaggerAlg, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'BTagging'
  def getType( self ):
      return 'Analysis::StandAloneJetBTaggerAlg'
  pass # class Analysis__StandAloneJetBTaggerAlg
