#====================================================================
# JETM8.py 
# reductionConf flag JETM8 in Reco_tf.py   
#====================================================================

from DerivationFrameworkCore.DerivationFrameworkMaster import *
from DerivationFrameworkJetEtMiss.JetCommon import *
from DerivationFrameworkJetEtMiss.ExtendedJetCommon import *
#from DerivationFrameworkEGamma.EGammaCommon import *
from DerivationFrameworkJetEtMiss.METCommon import *

#====================================================================
# SKIMMING TOOL 
#====================================================================
triggers = [
'HLT_j15',       'HLT_j15_320eta490',
'HLT_j25',       'HLT_j25_320eta490',
'HLT_j60',       'HLT_j60_320eta490',
'HLT_j35',       'HLT_j35_320eta490',
'HLT_j45_L1RDO', 'HLT_j45_320eta490',
'HLT_j55_L1RDO', 
'HLT_j55',       'HLT_j55_320eta490',
'HLT_j85_L1RDO',
'HLT_j85',       'HLT_j85_320eta490',
'HLT_j110',      'HLT_j110_320eta490',
'HLT_j35_j35_320eta490',
'HLT_j45_j45_320eta490',
'HLT_j55_j55_320eta490',
'HLT_j60_j60_320eta490',
'HLT_j85_j85_320eta490',
'HLT_j15_j15_320eta490',
'HLT_j25_j25_320eta490',
'HLT_j360_a10_lcw_nojcalib',
'HLT_j360_a10_lcw_nojcalib_L1HT150-J20.ETA30',
'HLT_j360_a10_lcw_sub',
'HLT_j360_a10_lcw_sub_L1HT150-J20.ETA30',
'HLT_j360_a10_nojcalib',
'HLT_j360_a10_nojcalib_L1HT150-J20.ETA30',
'HLT_j360_a10_sub',
'HLT_j360_a10_sub_L1HT150-J20.ETA30',
'HLT_j360_a10r']

from DerivationFrameworkTools.DerivationFrameworkToolsConf import DerivationFramework__TriggerSkimmingTool
JETM8TrigSkimmingTool = DerivationFramework__TriggerSkimmingTool(   name           = "JETM8TrigSkimmingTool",
                                                                    TriggerListOR  = triggers )
ToolSvc += JETM8TrigSkimmingTool

# For first data
jetSelection = '(count( AntiKt10LCTopoJets.pt > 100.*GeV ) >=1)'
#jetSelection = '(count( CamKt12LCTopoJets.pt > 150.*GeV ) >=1)'
expression = jetSelection

from DerivationFrameworkTools.DerivationFrameworkToolsConf import DerivationFramework__xAODStringSkimmingTool
JETM8OfflineSkimmingTool = DerivationFramework__xAODStringSkimmingTool( name = "JETM8OfflineSkimmingTool",
                                                                        expression = expression)
ToolSvc += JETM8OfflineSkimmingTool

from DerivationFrameworkTools.DerivationFrameworkToolsConf import DerivationFramework__FilterCombinationAND
JETM8SkimmingTool = DerivationFramework__FilterCombinationAND(name="JETM8SkimmingTool", FilterList=[JETM8TrigSkimmingTool,JETM8OfflineSkimmingTool] )
ToolSvc += JETM8SkimmingTool

#====================================================================
# THINNING TOOLS 
#====================================================================
thinningTools = []

# thinning_expression = "InDetTrackParticles.pt > 0.5*GeV"
# from DerivationFrameworkInDet.DerivationFrameworkInDetConf import DerivationFramework__TrackParticleThinning
# JETM8TPThinningTool = DerivationFramework__TrackParticleThinning( name                    = "JETM8ThinningTool",
#                                                                   ThinningService         = "JETM8ThinningSvc",
#                                                                   SelectionString         = thinning_expression,
#                                                                   InDetTrackParticlesKey  = "InDetTrackParticles")

# from DerivationFrameworkInDet.DerivationFrameworkInDetConf import DerivationFramework__JetTrackParticleThinning
# JETM8JetTPThinningTool = DerivationFramework__JetTrackParticleThinning( name          = "JETM8Akt4JetTPThinningTool",
#                                                                         ThinningService         = "JETM8ThinningSvc",
#                                                                         JetKey                  = "AntiKt4EMTopoJets",
#                                                                         InDetTrackParticlesKey  = "InDetTrackParticles",
#                                                                         ApplyAnd                = True)
# ToolSvc += JETM8JetTPThinningTool
# thinningTools.append(JETM8JetTPThinningTool)

from DerivationFrameworkInDet.DerivationFrameworkInDetConf import DerivationFramework__JetTrackParticleThinning
JETM8Akt4JetTPThinningTool = DerivationFramework__JetTrackParticleThinning( name          = "JETM8Akt4JetTPThinningTool",
                                                                        ThinningService         = "JETM8ThinningSvc",
                                                                        JetKey                  = "AntiKt4EMTopoJets",
                                                                        InDetTrackParticlesKey  = "InDetTrackParticles",
                                                                        ApplyAnd                = False)
ToolSvc += JETM8Akt4JetTPThinningTool
thinningTools.append(JETM8Akt4JetTPThinningTool)

from DerivationFrameworkInDet.DerivationFrameworkInDetConf import DerivationFramework__JetTrackParticleThinning
JETM8Akt10JetTPThinningTool = DerivationFramework__JetTrackParticleThinning( name          = "JETM8Akt10JetTPThinningTool",
                                                                        ThinningService         = "JETM8ThinningSvc",
                                                                        JetKey                  = "AntiKt10LCTopoJets",
                                                                        InDetTrackParticlesKey  = "InDetTrackParticles",
                                                                        ApplyAnd                = False)
ToolSvc += JETM8Akt10JetTPThinningTool
thinningTools.append(JETM8Akt10JetTPThinningTool)

# TrackParticles associated with Muons
from DerivationFrameworkInDet.DerivationFrameworkInDetConf import DerivationFramework__MuonTrackParticleThinning
JETM8MuonTPThinningTool = DerivationFramework__MuonTrackParticleThinning(name     = "JETM8MuonTPThinningTool",
                                                                         ThinningService         = "JETM8ThinningSvc",
                                                                         MuonKey                 = "Muons",
                                                                         InDetTrackParticlesKey  = "InDetTrackParticles")
ToolSvc += JETM8MuonTPThinningTool
thinningTools.append(JETM8MuonTPThinningTool)

# TrackParticles associated with electrons
from DerivationFrameworkInDet.DerivationFrameworkInDetConf import DerivationFramework__EgammaTrackParticleThinning
JETM8ElectronTPThinningTool = DerivationFramework__EgammaTrackParticleThinning(name                    = "JETM8ElectronTPThinningTool",
                                                                               ThinningService         = "JETM8ThinningSvc",
                                                                               SGKey                   = "Electrons",
                                                                               InDetTrackParticlesKey  = "InDetTrackParticles")
ToolSvc += JETM8ElectronTPThinningTool
thinningTools.append(JETM8ElectronTPThinningTool)

# # TrackParticles associated with taus
# from DerivationFrameworkInDet.DerivationFrameworkInDetConf import DerivationFramework__TauTrackParticleThinning
# JETM8TauTPThinningTool = DerivationFramework__TauTrackParticleThinning( name            = "JETM8TauTPThinningTool",
#                                                                         ThinningService = "JETM8ThinningSvc",
#                                                                         TauKey          = "TauJets",
#                                                                         InDetTrackParticlesKey  = "InDetTrackParticles")
# ToolSvc += JETM8TauTPThinningTool
# thinningTools.append(JETM8TauTPThinningTool)

# Truth particle thinning
doTruthThinning = True
preserveAllDescendants = False
from AthenaCommon.GlobalFlags import globalflags
if doTruthThinning and globalflags.DataSource()=='geant4':
    truth_cond_WZH    = "((abs(TruthParticles.pdgId) >= 23) && (abs(TruthParticles.pdgId) <= 25))"            # W, Z and Higgs
    truth_cond_Lepton = "((abs(TruthParticles.pdgId) >= 11) && (abs(TruthParticles.pdgId) <= 16))"            # Leptons
    truth_cond_Quark  = "((abs(TruthParticles.pdgId) <=  6))"                                                # Quarks
    truth_cond_Gluon  = "((abs(TruthParticles.pdgId) == 21))"                                                # Gluons
    truth_cond_Photon = "((abs(TruthParticles.pdgId) == 22) && (TruthParticles.pt > 10000.))"                 # Photon
    
    truth_expression = '('+truth_cond_WZH+' || '+truth_cond_Lepton +' || '+truth_cond_Quark+' || '+truth_cond_Gluon+' || '+truth_cond_Photon+')'
    
    from DerivationFrameworkMCTruth.DerivationFrameworkMCTruthConf import DerivationFramework__GenericTruthThinning
    JETM8TruthThinningTool = DerivationFramework__GenericTruthThinning( name = "JETM8TruthThinningTool",
                                                                        ThinningService        = "JETM8ThinningSvc",
                                                                        ParticleSelectionString = truth_expression,
                                                                        PreserveDescendants     = preserveAllDescendants,
                                                                        PreserveGeneratorDescendants = not preserveAllDescendants,
                                                                        PreserveAncestors = True)
    
    ToolSvc += JETM8TruthThinningTool
    thinningTools.append(JETM8TruthThinningTool)    

#=======================================
# CREATE PRIVATE SEQUENCE
#=======================================

jetm8Seq = CfgMgr.AthSequencer("JETM8Sequence")
DerivationFrameworkJob += jetm8Seq
#jetm8Seq = DerivationFrameworkJob

#=======================================
# CREATE THE DERIVATION KERNEL ALGORITHM   
#=======================================

from DerivationFrameworkCore.DerivationFrameworkCoreConf import DerivationFramework__DerivationKernel
jetm8Seq += CfgMgr.DerivationFramework__DerivationKernel(	name = "JETM8Kernel", 
									SkimmingTools = [JETM8SkimmingTool],
									ThinningTools = thinningTools)

#====================================================================
# exclusive kt subjet setup
#====================================================================

def ExKt2SubjetBuilder(JetCollectionName):
    return buildExclusiveSubjets(JetCollectionName, "Kt", 2)

def ExKt3SubjetBuilder(JetCollectionName):
    return buildExclusiveSubjets(JetCollectionName, "Kt", 3)

exclusiveSubjetBuilderList = [
                              ExKt2SubjetBuilder, 
                              ExKt3SubjetBuilder,
                             ]

#====================================================================
# Special jets
#====================================================================

OutputJets["JETM8"] = []

# variable-R track-jets
addStandardJets("AntiKt", 0.4, "PV0Track", ptmin=2000, ptminFilter=7000, mods="pv0track", calibOpt="none", ghostArea=0, algseq=jetm8Seq, outputGroup="JETM8", exclusiveSubjetBuilderList=[], jetnamebase="AntiKtVR40Rmax4Rmin0Track", variableRMinRadius=0, variableRMassScale=40000)
addStandardJets("AntiKt", 0.4, "PV0Track", ptmin=2000, ptminFilter=7000, mods="pv0track", calibOpt="none", ghostArea=0, algseq=jetm8Seq, outputGroup="JETM8", exclusiveSubjetBuilderList=[], jetnamebase="AntiKtVR40Rmax4Rmin2Track", variableRMinRadius=0.2, variableRMassScale=40000)

# AntiKt10*PtFrac5Rclus20
addDefaultTrimmedJets(jetm8Seq,"JETM8",exclusiveSubjetBuilderList=exclusiveSubjetBuilderList)

# if jetFlags.useTruth:
#     addPrunedJets("CamKt", 1.0, "Truth", rcut=0.5, zcut=0.15, algseq=jetm8Seq, outputGroup="JETM8")
#     addFilteredJets("CamKt", 1.2, "Truth", mumax=1.0, ymin=0.15, algseq=jetm8Seq, outputGroup="JETM8")
#     addFilteredJets("CamKt", 1.2, "Truth", mumax=1.0, ymin=0.04, algseq=jetm8Seq, outputGroup="JETM8")
#     # addStandardJets("CamKt", 1.5, "Truth", ptmin=40000, algseq=jetm8Seq, outputGroup="JETM8")
#     addStandardJets("CamKt", 1.5, "Truth", ptmin=40000, mods=[], algseq=jetm8Seq, outputGroup="JETM8")

# # CamKtLCTopo 10 and 12
# addPrunedJets("CamKt", 1.0, "LCTopo", rcut=0.5, zcut=0.15, algseq=jetm8Seq, outputGroup="JETM8")
# addFilteredJets("CamKt", 1.2, "LCTopo", mumax=1.0, ymin=0.15, algseq=jetm8Seq, outputGroup="JETM8")
# addFilteredJets("CamKt", 1.2, "LCTopo", mumax=1.0, ymin=0.04, algseq=jetm8Seq, outputGroup="JETM8")
# # CamKt15LCTopo
# addStandardJets("CamKt", 1.5, "LCTopo", mods="calib", calibOpt="none", ghostArea=0.01, ptmin=2000, ptminFilter=50000,
#                 algseq=jetm8Seq, outputGroup="JETM8")
# AntiKt10Track
#addStandardJets("AntiKt", 1.5, "PV0Track", ptmin=40000, algseq=jetm8Seq, outputGroup="JETM8")
#addStandardJets("AntiKt", 1.0, "PV0Track", ptmin=20000, mods=[], algseq=jetm8Seq, outputGroup="JETM8", exclusiveSubjetBuilderList=exclusiveSubjetBuilderList)

# jet copy for b-tagging purpose
# lesson learnt: For jet that has never been b-tagged before, b-tagging algorithm will make a deep copy of it and overwrite with the original one with the deep copy before b-tagging
# This means, any link from external object to the jets, built before b-tagging, will becomes invalid. Remember, during the deep copy overwriting, even the container address gets changed!
# Thus, one way to get around is to make another deep copy of jet collection, store them in SG with another name, and run the b-tagging on this copy collection
addCopyJets("NewAntiKt10LCTopoTrimmedPtFrac5SmallR20Jets", "AntiKt10LCTopoTrimmedPtFrac5SmallR20Jets", algseq=jetm8Seq, outputGroup="JETM8", mods=[], doShallow=False)
#addCopyJets("NewAntiKt10PV0TrackJets", "AntiKt10PV0TrackJets", algseq=jetm8Seq, outputGroup="JETM8", mods=[], doShallow=False)


#====================================================================
# b-tagging setup
#====================================================================

# determine jet collection to be b-tagged
JetCollectionToRetag = []
JetCollectionToBtag  = []
# re-tagging, for VR purpose
JetCollectionToRetag += [
                         "AntiKt4LCTopoJets",
                         "AntiKt4PV0TrackJets",
                        ]
# parent fat-jet
JetCollectionToBtag += [
                         "NewAntiKt10LCTopoTrimmedPtFrac5SmallR20Jets",
                         # "NewAntiKt10PV0TrackJets",
                       ]
# all exclusive subjets
JetCollectionToBtag += [
                         "AntiKt10LCTopoTrimmedPtFrac5SmallR20ExKt2SubJets",
                         "AntiKt10LCTopoTrimmedPtFrac5SmallR20ExKt3SubJets",
                         #"AntiKt10PV0TrackExKt2SubJets",
                         #"AntiKt10PV0TrackExKt3SubJets",
                         "AntiKtVR40Rmax4Rmin0TrackJets",
                         "AntiKtVR40Rmax4Rmin2TrackJets",
                       ]

print "Jet collection to be re-tagged:",JetCollectionToRetag
print "Jet collections to be b-tagged:",JetCollectionToBtag

# special jet name transformation (only for track-jets actually)
JetCollectionToBtagList = [ (JetCollection, JetCollection.replace('ZTrack', 'Track').replace('PV0Track', 'Track')) for JetCollection in JetCollectionToBtag ]

# from AthenaCommon.Constants import DEBUG
# BTaggingFlags.OutputLevel = DEBUG

# b-tagging calibration channel aliase
BTaggingFlags.CalibrationChannelAliases += [
                                             "NewAntiKt10LCTopoTrimmedPtFrac5SmallR20->AntiKt10LCTopo,AntiKt6LCTopo,AntiKt6TopoEM,AntiKt4LCTopo,AntiKt4TopoEM,AntiKt4EMTopo",
                                             #"NewAntiKt10Track->AntiKt10Track,AntiKt6Track,AntiKt4Track,AntiKt10TopoEM,AntiKt6TopoEM,AntiKt4TopoEM,AntiKt4EMTopo",
                                           ]
BTaggingFlags.CalibrationChannelAliases += [
                                             "AntiKt10LCTopoTrimmedPtFrac5SmallR20ExKt2Sub->AntiKt4LCTopo",
                                             "AntiKt10LCTopoTrimmedPtFrac5SmallR20ExKt3Sub->AntiKt4LCTopo",
                                             #"AntiKt10TrackExKt2Sub->AntiKt4Track,AntiKt4TopoEM,AntiKt4EMTopo",
                                             #"AntiKt10TrackExKt3Sub->AntiKt4Track,AntiKt4TopoEM,AntiKt4EMTopo",
                                             "AntiKtVR40Rmax4Rmin0Track->AntiKt4Track,AntiKt4TopoEM,AntiKt4EMTopo",
                                             "AntiKtVR40Rmax4Rmin2Track->AntiKt4Track,AntiKt4TopoEM,AntiKt4EMTopo",
                                           ]

# specify tagger list:
BtaggerList = ['IP2D', 'IP3D', 'SV0', 'MultiSVbb1', 'MultiSVbb2', 'SV1', 'JetFitterNN', 'MV2c00', 'MV2c10', 'MV2c20', 'MV2c100', 'MV2m']

# initialize all b-tagging tool
from DerivationFrameworkFlavourTag.FlavourTagCommon import FlavorTagInit
FlavorTagInit(myTaggers      = BtaggerList,
              JetCollections = JetCollectionToRetag + JetCollectionToBtag,
              Sequencer      = DerivationFrameworkJob)


#====================================================================
# SET UP STREAM   
#====================================================================
streamName = derivationFlags.WriteDAOD_JETM8Stream.StreamName
fileName   = buildFileName( derivationFlags.WriteDAOD_JETM8Stream )
JETM8Stream = MSMgr.NewPoolRootStream( streamName, fileName )
JETM8Stream.AcceptAlgs(["JETM8Kernel"])
# for thinning
from AthenaServices.Configurables import ThinningSvc, createThinningSvc
augStream = MSMgr.GetStream( streamName )
evtStream = augStream.GetEventStream()
svcMgr += createThinningSvc( svcName="JETM8ThinningSvc", outStreams=[evtStream] )

#====================================================================
# Add the containers to the output stream - slimming done here
#====================================================================
from DerivationFrameworkCore.SlimmingHelper import SlimmingHelper
JETM8SlimmingHelper = SlimmingHelper("JETM8SlimmingHelper")
JETM8SlimmingHelper.SmartCollections = ["Electrons", "Photons", "Muons", "TauJets",
                                        "InDetTrackParticles", "PrimaryVertices"]
JETM8SlimmingHelper.AllVariables = ["BTagging_AntiKt4LCTopo", "BTagging_AntiKt4EMTopo",
                                    "BTagging_AntiKt2Track", "BTagging_AntiKt3Track", "BTagging_AntiKt4Track", #"BTagging_AntiKt3Track",
                                    "CaloCalTopoClusters",
                                    "MuonTruthParticles", "egammaTruthParticles",
                                    "TruthParticles", "TruthEvents", "TruthVertices"]
#JETM8SlimmingHelper.ExtraVariables = []

# Trigger content
JETM8SlimmingHelper.IncludeJetTriggerContent = True

# Add the jet containers to the stream
addJetOutputs(JETM8SlimmingHelper,["SmallR","LargeR","JETM8"])
# Add the MET containers to the stream
addMETOutputs(JETM8SlimmingHelper,["Diagnostic","AntiKt4LCTopo","AntiKt4EMPFlow","Track"])
# Add b-tagging containers to the stream
# since these are on-the-fly container, they need to be writen out explicitly
for JetNamePair in JetCollectionToBtagList:
    JetName = JetNamePair[1][:-4]

    JETM8SlimmingHelper.StaticContent.append("xAOD::BTaggingContainer#BTagging_" + JetName)
    JETM8SlimmingHelper.StaticContent.append("xAOD::BTaggingAuxContainer#BTagging_" + JetName + "Aux.")

    JETM8SlimmingHelper.StaticContent.append("xAOD::VertexContainer#BTagging_" + JetName + "SecVtx")
    JETM8SlimmingHelper.StaticContent.append("xAOD::VertexAuxContainer#BTagging_" + JetName + "SecVtx" + "Aux.-vxTrackAtVertex")

    JETM8SlimmingHelper.StaticContent.append("xAOD::BTagVertexContainer#BTagging_" + JetName + "JFVtx")
    JETM8SlimmingHelper.StaticContent.append("xAOD::BTagVertexAuxContainer#BTagging_" + JetName + "JFVtx" + "Aux.")


JETM8SlimmingHelper.AppendContentToStream(JETM8Stream)
JETM8Stream.RemoveItem("xAOD::TrigNavigation#*")
JETM8Stream.RemoveItem("xAOD::TrigNavigationAuxInfo#*")




