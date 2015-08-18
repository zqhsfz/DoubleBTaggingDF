#Tue Aug 18 16:50:33 2015"""Automatically generated. DO NOT EDIT please"""
from GaudiKernel.GaudiHandles import *
from GaudiKernel.Proxy.Configurable import *

class AngularityTool( ConfigurableAlgTool ) :
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
  }
  _propertyDocDct = { 
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(AngularityTool, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'JetSubStructureMomentTools'
  def getType( self ):
      return 'AngularityTool'
  pass # class AngularityTool

class BosonTagTool( ConfigurableAlgTool ) :
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
    'WorkingPoint' : 'medium', # str
    'TaggerAlgorithm' : 'smooth', # str
    'RecommendationsFile' : 'JetSubStructureUtils/data/config_13TeV_20150528_Wtagging.dat', # str
    'Debug' : False, # bool
    'Verbose' : False, # bool
  }
  _propertyDocDct = { 
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(BosonTagTool, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'JetSubStructureMomentTools'
  def getType( self ):
      return 'BosonTagTool'
  pass # class BosonTagTool

class CenterOfMassShapesTool( ConfigurableAlgTool ) :
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
  }
  _propertyDocDct = { 
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(CenterOfMassShapesTool, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'JetSubStructureMomentTools'
  def getType( self ):
      return 'CenterOfMassShapesTool'
  pass # class CenterOfMassShapesTool

class DipolarityTool( ConfigurableAlgTool ) :
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
    'SubJetRadius' : 0.30000000, # float
  }
  _propertyDocDct = { 
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(DipolarityTool, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'JetSubStructureMomentTools'
  def getType( self ):
      return 'DipolarityTool'
  pass # class DipolarityTool

class EnergyCorrelatorRatiosTool( ConfigurableAlgTool ) :
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
    'IncludeBeta2' : False, # bool
    'IncludeECF4' : False, # bool
  }
  _propertyDocDct = { 
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(EnergyCorrelatorRatiosTool, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'JetSubStructureMomentTools'
  def getType( self ):
      return 'EnergyCorrelatorRatiosTool'
  pass # class EnergyCorrelatorRatiosTool

class EnergyCorrelatorTool( ConfigurableAlgTool ) :
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
    'Beta' : 1.00000, # float
    'IncludeBeta2' : False, # bool
    'IncludeECF4' : False, # bool
  }
  _propertyDocDct = { 
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(EnergyCorrelatorTool, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'JetSubStructureMomentTools'
  def getType( self ):
      return 'EnergyCorrelatorTool'
  pass # class EnergyCorrelatorTool

class JetChargeTool( ConfigurableAlgTool ) :
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
    'K' : 1.0000000, # float
  }
  _propertyDocDct = { 
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(JetChargeTool, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'JetSubStructureMomentTools'
  def getType( self ):
      return 'JetChargeTool'
  pass # class JetChargeTool

class JetPullTool( ConfigurableAlgTool ) :
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
    'UseEtaInsteadOfY' : False, # bool
    'IncludeTensorMoments' : False, # bool
  }
  _propertyDocDct = { 
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(JetPullTool, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'JetSubStructureMomentTools'
  def getType( self ):
      return 'JetPullTool'
  pass # class JetPullTool

class KTSplittingScaleTool( ConfigurableAlgTool ) :
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
  }
  _propertyDocDct = { 
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(KTSplittingScaleTool, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'JetSubStructureMomentTools'
  def getType( self ):
      return 'KTSplittingScaleTool'
  pass # class KTSplittingScaleTool

class KtDeltaRTool( ConfigurableAlgTool ) :
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
    'JetRadius' : 0.40000000, # float
  }
  _propertyDocDct = { 
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(KtDeltaRTool, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'JetSubStructureMomentTools'
  def getType( self ):
      return 'KtDeltaRTool'
  pass # class KtDeltaRTool

class KtMassDropTool( ConfigurableAlgTool ) :
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
  }
  _propertyDocDct = { 
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(KtMassDropTool, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'JetSubStructureMomentTools'
  def getType( self ):
      return 'KtMassDropTool'
  pass # class KtMassDropTool

class NSubjettinessRatiosTool( ConfigurableAlgTool ) :
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
  }
  _propertyDocDct = { 
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(NSubjettinessRatiosTool, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'JetSubStructureMomentTools'
  def getType( self ):
      return 'NSubjettinessRatiosTool'
  pass # class NSubjettinessRatiosTool

class NSubjettinessTool( ConfigurableAlgTool ) :
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
    'Alpha' : 1.00000, # float
  }
  _propertyDocDct = { 
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(NSubjettinessTool, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'JetSubStructureMomentTools'
  def getType( self ):
      return 'NSubjettinessTool'
  pass # class NSubjettinessTool

class PlanarFlowTool( ConfigurableAlgTool ) :
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
  }
  _propertyDocDct = { 
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(PlanarFlowTool, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'JetSubStructureMomentTools'
  def getType( self ):
      return 'PlanarFlowTool'
  pass # class PlanarFlowTool

class QwTool( ConfigurableAlgTool ) :
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
  }
  _propertyDocDct = { 
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(QwTool, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'JetSubStructureMomentTools'
  def getType( self ):
      return 'QwTool'
  pass # class QwTool

class ShowerDeconstructionTool( ConfigurableAlgTool ) :
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
  }
  _propertyDocDct = { 
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(ShowerDeconstructionTool, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'JetSubStructureMomentTools'
  def getType( self ):
      return 'ShowerDeconstructionTool'
  pass # class ShowerDeconstructionTool

class SubjetFinderTool( ConfigurableAlgTool ) :
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
    'JetAlgorithm' : 'Kt', # str
    'JetRadius' : 0.300000, # float
    'PtMin' : 5000.00, # float
    'SubjetRecorder' : PublicToolHandle('ISubjetRecorderTool'), # GaudiHandle
    'ExclusiveNjets' : -1, # int
  }
  _propertyDocDct = { 
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(SubjetFinderTool, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'JetSubStructureMomentTools'
  def getType( self ):
      return 'SubjetFinderTool'
  pass # class SubjetFinderTool

class SubjetMakerTool( ConfigurableAlgTool ) :
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
    'type' : 'AntiKt', # str
    'R' : 0.200000, # float
    'PtCut' : 20000.0, # float
  }
  _propertyDocDct = { 
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(SubjetMakerTool, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'JetSubStructureMomentTools'
  def getType( self ):
      return 'SubjetMakerTool'
  pass # class SubjetMakerTool

class SubjetRecorderTool( ConfigurableAlgTool ) :
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
    'SubjetLabel' : '', # str
    'SubjetContainerName' : '', # str
    'SubjetAlgorithm_BTAG' : '', # str
    'SubjetRadius_BTAG' : 0.00000, # float
  }
  _propertyDocDct = { 
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(SubjetRecorderTool, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'JetSubStructureMomentTools'
  def getType( self ):
      return 'SubjetRecorderTool'
  pass # class SubjetRecorderTool

class Validator( ConfigurableAlgTool ) :
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
    'InputContainer' : '', # str
    'FloatMoments' : [  ], # list
  }
  _propertyDocDct = { 
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(Validator, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'JetSubStructureMomentTools'
  def getType( self ):
      return 'Validator'
  pass # class Validator

class VolatilityTool( ConfigurableAlgTool ) :
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
    'NumberOfIterations' : 100, # int
    'ZCut' : 0.010000000, # float
    'DCut' : 0.50000000, # float
    'ExpMin' : 0.0000000, # float
    'ExpMax' : 0.0000000, # float
    'Rigidity' : 0.10000000, # float
    'TruncationFactor' : 0.0000000, # float
  }
  _propertyDocDct = { 
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(VolatilityTool, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'JetSubStructureMomentTools'
  def getType( self ):
      return 'VolatilityTool'
  pass # class VolatilityTool
