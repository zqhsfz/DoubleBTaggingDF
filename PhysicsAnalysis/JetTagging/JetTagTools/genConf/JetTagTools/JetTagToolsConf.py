#Mon Sep 14 21:25:40 2015"""Automatically generated. DO NOT EDIT please"""
from GaudiKernel.GaudiHandles import *
from GaudiKernel.Proxy.Configurable import *

class Analysis__BasicTrackGradeFactory( ConfigurableAlgTool ) :
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
    'useSharedHitInfo' : False, # bool
    'nSharedBLayer' : 0, # int
    'nSharedPix' : 0, # int
    'nSharedSct' : 1, # int
    'nSharedSi' : 999, # int
  }
  _propertyDocDct = { 
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(Analysis__BasicTrackGradeFactory, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'JetTagTools'
  def getType( self ):
      return 'Analysis::BasicTrackGradeFactory'
  pass # class Analysis__BasicTrackGradeFactory

class Analysis__DetailedTrackGradeFactory( ConfigurableAlgTool ) :
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
    'hitBLayerGrade' : True, # bool
    'useSharedHitInfo' : False, # bool
    'useRun2TrackGrading' : False, # bool
    'useInnerLayers0HitInfo' : False, # bool
    'useDetailSplitHitInfo' : False, # bool
    'useDetailSharedHitInfo' : True, # bool
    'nSharedBLayer' : 0, # int
    'nSharedPix' : 0, # int
    'nSharedSct' : 1, # int
    'nSharedSi' : 999, # int
    'nSharedInnermostPixelLayer' : 0, # int
    'nSharedNextToInnermostPixelLayer' : 0, # int
    'ptFracGrade' : False, # bool
    'ptFracCut' : 0.040000000, # float
    'ptEtaGrades' : False, # bool
    'ptLowerCuts' : [ 1000.00000000 , 4000.00000000 , 10000.00000000 ], # list
    'etaLowerCuts' : [ 0.00000000 , 0.50000000 , 1.50000000 ], # list
  }
  _propertyDocDct = { 
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(Analysis__DetailedTrackGradeFactory, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'JetTagTools'
  def getType( self ):
      return 'Analysis::DetailedTrackGradeFactory'
  pass # class Analysis__DetailedTrackGradeFactory

class Analysis__DummyTag( ConfigurableAlgTool ) :
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
    'Runmodus' : 'analysis', # str
    'writeInfo' : True, # bool
  }
  _propertyDocDct = { 
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(Analysis__DummyTag, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'JetTagTools'
  def getType( self ):
      return 'Analysis::DummyTag'
  pass # class Analysis__DummyTag

class Analysis__ExKtbbTag( ConfigurableAlgTool ) :
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
    'Runmodus' : 'analysis', # str
    'tagMode' : 'H->bb', # str
    'taggerName' : 'ExKtbb', # str
    'taggerNameBase' : 'ExKtbb', # str
    'xAODBaseName' : 'ExKtbb', # str
    'debug' : False, # bool
    'SubJetLabel' : 'ExKt2SubJets', # str
    'JFOnlyVtx' : False, # bool
  }
  _propertyDocDct = { 
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(Analysis__ExKtbbTag, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'JetTagTools'
  def getType( self ):
      return 'Analysis::ExKtbbTag'
  pass # class Analysis__ExKtbbTag

class Analysis__IPTag( ConfigurableAlgTool ) :
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
    'Runmodus' : 'analysis', # str
    'UseCHypo' : True, # bool
    'xAODBaseName' : '', # str
    'useVariables' : [  ], # list
    'impactParameterView' : '2D', # str
    'trackGradePartitions' : [ 'Good' ], # list
    'RejectBadTracks' : False, # bool
    'SignWithSvx' : False, # bool
    'SVForIPTool' : PublicToolHandle('Analysis::SVForIPTool'), # GaudiHandle
    'use2DSignForIP3D' : False, # bool
    'useD0SignForZ0' : False, # bool
    'usePosIP' : True, # bool
    'useNegIP' : True, # bool
    'useZIPSignForPosNeg' : False, # bool
    'flipIPSign' : False, # bool
    'flipZIPSign' : False, # bool
    'LikelihoodTool' : PublicToolHandle('Analysis::NewLikelihoodTool'), # GaudiHandle
    'trackSelectorTool' : PublicToolHandle('Analysis::TrackSelector'), # GaudiHandle
    'trackGradeFactory' : PublicToolHandle('Analysis::BasicTrackGradeFactory'), # GaudiHandle
    'originalTPCollectionName' : 'InDetTrackParticles', # str
    'trackAssociationName' : 'BTagTrackToJetAssociator', # str
    'referenceType' : 'ALL', # str
    'truthMatchingName' : 'TruthInfo', # str
    'checkOverflows' : False, # bool
    'purificationDeltaR' : 0.80000000, # float
    'jetPtMinRef' : 15000.000, # float
    'jetCollectionList' : [  ], # list
    'useForcedCalibration' : False, # bool
    'ForcedCalibrationName' : 'Cone4H1Tower', # str
    'SecVxFinderName' : 'InDetVKalVxInJetTool', # str
    'TrackToVertexIPEstimator' : PublicToolHandle('Trk::ITrackToVertexIPEstimator'), # GaudiHandle
    'unbiasIPEstimation' : True, # bool
    'InDetTrackSelectionTool' : PublicToolHandle('InDet::InDetTrackSelectionTool'), # GaudiHandle
    'TrackVertexAssociationTool' : PublicToolHandle('CP::TightTrackVertexAssociationTool'), # GaudiHandle
  }
  _propertyDocDct = { 
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(Analysis__IPTag, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'JetTagTools'
  def getType( self ):
      return 'Analysis::IPTag'
  pass # class Analysis__IPTag

class Analysis__JetFitterNNTool( ConfigurableAlgTool ) :
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
    'CalibrationDirectory' : 'JetFitter', # str
    'CalibrationSubDirectory' : 'NeuralNetwork', # str
    'NeuralNetworkToHistoTool' : PublicToolHandle('Trk::NeuralNetworkToHistoTool'), # GaudiHandle
    'useCombinedIPNN' : True, # bool
    'calibrationTool' : PublicToolHandle('BTagCalibrationBroker'), # GaudiHandle
    'maximumRegisteredLayers' : 4, # int
    'usePtCorrectedMass' : False, # bool
  }
  _propertyDocDct = { 
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(Analysis__JetFitterNNTool, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'JetTagTools'
  def getType( self ):
      return 'Analysis::JetFitterNNTool'
  pass # class Analysis__JetFitterNNTool

class Analysis__JetFitterNtupleWriter( ConfigurableAlgTool ) :
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
      super(Analysis__JetFitterNtupleWriter, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'JetTagTools'
  def getType( self ):
      return 'Analysis::JetFitterNtupleWriter'
  pass # class Analysis__JetFitterNtupleWriter

class Analysis__JetFitterTag( ConfigurableAlgTool ) :
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
    'Runmodus' : 'analysis', # str
    'ListHypotheses' : [ 'bottom' , 'light' , 'charm' ], # list
    'jetPtMinRef' : 15000.000, # float
    'jetCollectionList' : [  ], # list
    'useForcedCalibration' : False, # bool
    'forcedCalibrationName' : 'Cone4H1Tower', # str
    'ipinfoTaggerName' : '', # str
    'SecVxFinderName' : '', # str
    'xAODBaseName' : '', # str
    'jetfitterNtupleWriter' : PublicToolHandle('Analysis::JetFitterNtupleWriter'), # GaudiHandle
    'jetfitterClassifier' : PublicToolHandle('Analysis::JetFitterNNTool'), # GaudiHandle
  }
  _propertyDocDct = { 
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(Analysis__JetFitterTag, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'JetTagTools'
  def getType( self ):
      return 'Analysis::JetFitterTag'
  pass # class Analysis__JetFitterTag

class Analysis__JetFitterVariablesFactory( ConfigurableAlgTool ) :
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
    'secVxFinderName' : 'InDetJetFitterVxFinder', # str
    'JetFitterInstance' : 'JetFitterTag', # str
    'addNegativeTracksToPrimaryVertex' : False, # bool
    'usePtCorrectedEnergy' : False, # bool
    'useSingleTracksAlsoForMass' : False, # bool
    'revertFromPositiveToNegativeTags' : False, # bool
  }
  _propertyDocDct = { 
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(Analysis__JetFitterVariablesFactory, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'JetTagTools'
  def getType( self ):
      return 'Analysis::JetFitterVariablesFactory'
  pass # class Analysis__JetFitterVariablesFactory

class Analysis__JetVertexCharge( ConfigurableAlgTool ) :
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
    'SecVxFinderName' : '', # str
    'Runmodus' : 'analysis', # str
    'calibrationTool' : PublicToolHandle('BTagCalibrationBroker'), # GaudiHandle
    'taggerNameBase' : 'JetVertexCharge', # str
    'jetCollectionList' : [  ], # list
    'useForcedCalibration' : True, # bool
    'muonAssociationName' : 'Muons', # str
    'trackAssociationName' : 'BTagTrackToJetAssociator', # str
    'kFactor' : 0.90000000, # float
    'kFactorSV' : 0.50000000, # float
    'kFactorTV' : 0.50000000, # float
    'Trkd0Cut' : 4.5000000, # float
    'Trkz0Cut' : 2.0000000, # float
    'TrkPtCut' : 500.00000, # float
    'TrkChi2Cut' : 5.0000000, # float
    'CutPrecisionHits' : 9, # int
    'CutPixHits' : 1, # int
    'CutTRTHits' : 9, # int
    'CutBLayHits' : 0, # int
    'CutSctHits' : 4, # int
    'CutSharedHits' : 1, # int
  }
  _propertyDocDct = { 
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(Analysis__JetVertexCharge, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'JetTagTools'
  def getType( self ):
      return 'Analysis::JetVertexCharge'
  pass # class Analysis__JetVertexCharge

class Analysis__MSVVariablesFactory( ConfigurableAlgTool ) :
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
      super(Analysis__MSVVariablesFactory, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'JetTagTools'
  def getType( self ):
      return 'Analysis::MSVVariablesFactory'
  pass # class Analysis__MSVVariablesFactory

class Analysis__MV1Tag( ConfigurableAlgTool ) :
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
    'calibrationTool' : PublicToolHandle('BTagCalibrationBroker'), # GaudiHandle
    'Runmodus' : 'analysis', # str
    'xAODBaseName' : 'didyouforgettoconfigthename', # str
    'inputIP3DWeightName' : 'IP3D', # str
    'inputSV1WeightName' : 'SV1', # str
    'inputJetFitterWeightName' : 'JetFitterCombNN', # str
    'taggerNameBase' : 'MV1', # str
    'taggerName' : 'MV1', # str
  }
  _propertyDocDct = { 
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(Analysis__MV1Tag, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'JetTagTools'
  def getType( self ):
      return 'Analysis::MV1Tag'
  pass # class Analysis__MV1Tag

class Analysis__MV1cTag( ConfigurableAlgTool ) :
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
    'calibrationTool' : PublicToolHandle('BTagCalibrationBroker'), # GaudiHandle
    'Runmodus' : 'analysis', # str
    'xAODBaseName' : 'didyouforgettoconfigthename', # str
    'inputIP3DWeightName' : 'IP3D', # str
    'inputSV1WeightName' : 'SV1', # str
    'inputJetFitterWeightName' : 'JetFitterCombNN', # str
    'taggerNameBase' : 'MV1c', # str
    'taggerName' : 'MV1c', # str
  }
  _propertyDocDct = { 
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(Analysis__MV1cTag, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'JetTagTools'
  def getType( self ):
      return 'Analysis::MV1cTag'
  pass # class Analysis__MV1cTag

class Analysis__MV2Tag( ConfigurableAlgTool ) :
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
    'calibrationTool' : PublicToolHandle('BTagCalibrationBroker'), # GaudiHandle
    'forceMV2CalibrationAlias' : True, # bool
    'MV2CalibAlias' : 'AntiKt4TopoEM', # str
    'Runmodus' : 'analysis', # str
    'DecorateMvaInputs' : False, # bool
    'inputSV0SourceName' : 'SV0', # str
    'inputSV1SourceName' : 'SV1', # str
    'inputIP2DSourceName' : 'IP2D', # str
    'inputIP3DSourceName' : 'IP3D', # str
    'inputJFSourceName' : 'JetFitter', # str
    'inputJFProbSourceName' : 'JetFitterCombNN', # str
    'xAODBaseName' : '', # str
    'taggerNameBase' : 'MV2', # str
    'taggerName' : 'MV2', # str
    'decTagName' : 'MV2_inputs', # str
    'trainingConfig' : 'Default', # str
  }
  _propertyDocDct = { 
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(Analysis__MV2Tag, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'JetTagTools'
  def getType( self ):
      return 'Analysis::MV2Tag'
  pass # class Analysis__MV2Tag

class Analysis__MVbTag( ConfigurableAlgTool ) :
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
    'calibrationTool' : PublicToolHandle('BTagCalibrationBroker'), # GaudiHandle
    'forceMVbCalibrationAlias' : False, # bool
    'MVbCalibAlias' : 'AntiKt4TopoEM', # str
    'Runmodus' : 'analysis', # str
    'inputSV0SourceName' : 'SV0', # str
    'inputSV1SourceName' : 'SV1', # str
    'inputIP2DSourceName' : 'IP2D', # str
    'inputIP3DSourceName' : 'IP3D', # str
    'inputJFSourceName' : 'JetFitter', # str
    'inputJFProbSourceName' : 'JetFitterCombNN', # str
    'xAODBaseName' : '', # str
    'taggerNameBase' : 'MVb', # str
    'taggerName' : 'MVb', # str
  }
  _propertyDocDct = { 
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(Analysis__MVbTag, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'JetTagTools'
  def getType( self ):
      return 'Analysis::MVbTag'
  pass # class Analysis__MVbTag

class Analysis__MultiSVTag( ConfigurableAlgTool ) :
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
    'calibrationTool' : PublicToolHandle('BTagCalibrationBroker'), # GaudiHandle
    'Runmodus' : 'analysis', # str
    'jetCollectionList' : [  ], # list
    'useForcedCalibration' : False, # bool
    'ForcedCalibrationName' : 'AntiKt4TopoEM', # str
    'SecVxFinderName' : '', # str
    'taggerNameBase' : 'MultiSVbb1', # str
    'xAODBaseName' : '', # str
    'inputSV0SourceName' : 'SV0', # str
  }
  _propertyDocDct = { 
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(Analysis__MultiSVTag, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'JetTagTools'
  def getType( self ):
      return 'Analysis::MultiSVTag'
  pass # class Analysis__MultiSVTag

class Analysis__NewLikelihoodTool( ConfigurableAlgTool ) :
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
    'taggerName' : 'undefined', # str
    'hypotheses' : [ 'B' , 'U' , 'C' ], # list
    'calibrationTool' : PublicToolHandle('BTagCalibrationBroker'), # GaudiHandle
    'normalizedProb' : True, # bool
    'interpolate' : False, # bool
    'smoothNTimes' : 1, # int
    'vetoSmoothingOf' : [ '/N2T' , '/Sip3D' ], # list
  }
  _propertyDocDct = { 
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(Analysis__NewLikelihoodTool, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'JetTagTools'
  def getType( self ):
      return 'Analysis::NewLikelihoodTool'
  pass # class Analysis__NewLikelihoodTool

class Analysis__SVForIPTool( ConfigurableAlgTool ) :
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
      super(Analysis__SVForIPTool, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'JetTagTools'
  def getType( self ):
      return 'Analysis::SVForIPTool'
  pass # class Analysis__SVForIPTool

class Analysis__SVTag( ConfigurableAlgTool ) :
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
    'Runmodus' : 'reference', # str
    'referenceType' : 'ALL', # str
    'jetPtMinRef' : 15000.0, # float
    'LikelihoodTool' : PublicToolHandle('Analysis::NewLikelihoodTool'), # GaudiHandle
    'checkOverflows' : False, # bool
    'purificationDeltaR' : 0.80000000, # float
    'UseBinInterpol' : False, # bool
    'jetCollectionList' : [  ], # list
    'useForcedCalibration' : False, # bool
    'ForcedCalibrationName' : 'Cone4H1Tower', # str
    'SecVxFinderName' : 'SV1', # str
    'SVAlgType' : '', # str
    'xAODBaseName' : '', # str
    'UseDRJetPvSv' : True, # bool
    'UseCHypo' : True, # bool
  }
  _propertyDocDct = { 
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(Analysis__SVTag, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'JetTagTools'
  def getType( self ):
      return 'Analysis::SVTag'
  pass # class Analysis__SVTag

class Analysis__TrackSelector( ConfigurableAlgTool ) :
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
    'trackToVertexTool' : PublicToolHandle('Reco::TrackToVertex'), # GaudiHandle
    'useBLayerHitPrediction' : False, # bool
    'usePerigeeParameters' : False, # bool
    'pTMin' : 1000.0000, # float
    'usepTDepTrackSel' : False, # bool
    'pTMinOffset' : 0.0000000, # float
    'pTMinSlope' : 0.0000000, # float
    'd0Max' : 1.0000000, # float
    'z0Max' : 1.5000000, # float
    'sigd0Max' : 999.00000, # float
    'sigz0Max' : 999.00000, # float
    'etaMax' : 9999.0000, # float
    'useTrackSummaryInfo' : True, # bool
    'nHitBLayer' : 1, # int
    'nHitPix' : 2, # int
    'nHitSct' : 0, # int
    'nHitSi' : 7, # int
    'nHitTrt' : 0, # int
    'nHitTrtHighE' : 0, # int
    'useDeadPixInfo' : True, # bool
    'useDeadSctInfo' : True, # bool
    'useTrackQualityInfo' : True, # bool
    'fitChi2' : 99999.000, # float
    'fitProb' : -1.0000000, # float
    'fitChi2OnNdfMax' : 999.00000, # float
    'inputTrackCollection' : '', # str
    'outputTrackCollection' : '', # str
    'useAntiPileUpCuts' : False, # bool
    'antiPileUpSigD0Cut' : 3.0000000, # float
    'antiPileUpSigZ0Cut' : 3.8000000, # float
    'antiPileUpNHitSiCut' : 9, # int
    'antiPileUpNHolePixCut' : 9, # int
    'useTrackingTightDefinition' : False, # bool
  }
  _propertyDocDct = { 
    'DetStore' : """ Handle to a StoreGateSvc/DetectorStore instance: it will be used to retrieve data during the course of the job """,
    'UserStore' : """ Handle to a UserDataSvc/UserDataSvc instance: it will be used to retrieve user data during the course of the job """,
    'EvtStore' : """ Handle to a StoreGateSvc instance: it will be used to retrieve data during the course of the job """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(Analysis__TrackSelector, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'JetTagTools'
  def getType( self ):
      return 'Analysis::TrackSelector'
  pass # class Analysis__TrackSelector
