#====================================================================
# JETM4.py 
# reductionConf flag JETM4 in Reco_tf.py   
#====================================================================

from DerivationFrameworkCore.DerivationFrameworkMaster import *
from DerivationFrameworkJetEtMiss.JetCommon import *
#from DerivationFrameworkJetEtMiss.ExtendedJetCommon import *
#
from DerivationFrameworkJetEtMiss.METCommon import *

#====================================================================
# SKIMMING TOOL 
#====================================================================
# NOTE: need to add isSimulation as OR with trigger
triggers = 'HLT_g10_loose || HLT_g20_loose || HLT_g40_loose || HLT_g60_loose || HLT_g80_loose || HLT_g100_loose || HLT_g120_loose || HLT_g140_loose'
expression = '( (EventInfo.eventTypeBitmask==1) || ('+triggers+') )'

from DerivationFrameworkTools.DerivationFrameworkToolsConf import DerivationFramework__xAODStringSkimmingTool
JETM4SkimmingTool = DerivationFramework__xAODStringSkimmingTool( name = "JETM4SkimmingTool1",
                                                                    expression = expression)
ToolSvc += JETM4SkimmingTool

#====================================================================
# SET UP STREAM   
#====================================================================
streamName = derivationFlags.WriteDAOD_JETM4Stream.StreamName
fileName   = buildFileName( derivationFlags.WriteDAOD_JETM4Stream )
JETM4Stream = MSMgr.NewPoolRootStream( streamName, fileName )
JETM4Stream.AcceptAlgs(["JETM4Kernel"])

#=======================================
# ESTABLISH THE THINNING HELPER
#=======================================

from DerivationFrameworkCore.ThinningHelper import ThinningHelper
JETM4ThinningHelper = ThinningHelper( "JETM4ThinningHelper" )
JETM4ThinningHelper.TriggerChains = triggers
JETM4ThinningHelper.AppendToStream( JETM4Stream )

#====================================================================
# THINNING TOOLS 
#====================================================================
thinningTools = []

# TrackParticles associated with Muons
from DerivationFrameworkInDet.DerivationFrameworkInDetConf import DerivationFramework__MuonTrackParticleThinning
JETM4MuonTPThinningTool = DerivationFramework__MuonTrackParticleThinning(name     = "JETM4MuonTPThinningTool",
                                                                    ThinningService         = JETM4ThinningHelper.ThinningSvc(),
                                                                    MuonKey                 = "Muons",
                                                                    InDetTrackParticlesKey  = "InDetTrackParticles")
ToolSvc += JETM4MuonTPThinningTool
thinningTools.append(JETM4MuonTPThinningTool)

# TrackParticles associated with electrons
from DerivationFrameworkInDet.DerivationFrameworkInDetConf import DerivationFramework__EgammaTrackParticleThinning
JETM4ElectronTPThinningTool = DerivationFramework__EgammaTrackParticleThinning(name                    = "JETM4ElectronTPThinningTool",
                                                                               ThinningService         = JETM4ThinningHelper.ThinningSvc(),
                                                                               SGKey                   = "Electrons",
                                                                               InDetTrackParticlesKey  = "InDetTrackParticles")
ToolSvc += JETM4ElectronTPThinningTool
thinningTools.append(JETM4ElectronTPThinningTool)

# # TrackParticles associated with taus
# from DerivationFrameworkInDet.DerivationFrameworkInDetConf import DerivationFramework__TauTrackParticleThinning
# JETM4TauTPThinningTool = DerivationFramework__TauTrackParticleThinning( name            = "JETM4TauTPThinningTool",
#                                                                         ThinningService = JETM4ThinningHelper.ThinningSvc(),
#                                                                         TauKey          = "TauJets",
#                                                                         InDetTrackParticlesKey  = "InDetTrackParticles")
# ToolSvc += JETM4TauTPThinningTool
# thinningTools.append(JETM4TauTPThinningTool)

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
    
    truth_expression = '('+truth_cond_WZH+' || '+truth_cond_Lepton +' || '+truth_cond_Quark+'||'+truth_cond_Gluon+' || '+truth_cond_Photon+')'
    
    from DerivationFrameworkMCTruth.DerivationFrameworkMCTruthConf import DerivationFramework__GenericTruthThinning
    JETM4TruthThinningTool = DerivationFramework__GenericTruthThinning( name = "JETM4TruthThinningTool",
                                                                        ThinningService        = JETM4ThinningHelper.ThinningSvc(),
                                                                        ParticleSelectionString = truth_expression,
                                                                        PreserveDescendants     = preserveAllDescendants,
                                                                        PreserveGeneratorDescendants = not preserveAllDescendants,
                                                                        PreserveAncestors = True)
    
    ToolSvc += JETM4TruthThinningTool
    thinningTools.append(JETM4TruthThinningTool)    

#=======================================
# CREATE THE DERIVATION KERNEL ALGORITHM   
#=======================================

from DerivationFrameworkCore.DerivationFrameworkCoreConf import DerivationFramework__DerivationKernel
DerivationFrameworkJob += CfgMgr.DerivationFramework__DerivationKernel(	name = "JETM4Kernel",
									SkimmingTools = [JETM4SkimmingTool],
									ThinningTools = thinningTools)

#====================================================================
# Add the containers to the output stream - slimming done here
#====================================================================
from DerivationFrameworkCore.SlimmingHelper import SlimmingHelper
JETM4SlimmingHelper = SlimmingHelper("JETM4SlimmingHelper")
JETM4SlimmingHelper.SmartCollections = ["Electrons", "Photons", "Muons", "TauJets",
                                        "InDetTrackParticles", "PrimaryVertices"]
JETM4SlimmingHelper.AllVariables = ["BTagging_AntiKt4LCTopo", "BTagging_AntiKt4EMTopo", "CaloCalTopoClusters",
                                    "MuonTruthParticles", "egammaTruthParticles",
                                    "TruthParticles", "TruthEvents", "TruthVertices",
                                    "MuonSegments"
                                    ]
#JETM4SlimmingHelper.ExtraVariables = []

# Trigger content
JETM4SlimmingHelper.IncludeEGammaTriggerContent = True

# Add the jet containers to the stream
addJetOutputs(JETM4SlimmingHelper,["SmallR"])
# Add the MET containers to the stream
addMETOutputs(JETM4SlimmingHelper,["Diagnostic","AntiKt4LCTopo","AntiKt4EMPFlow","Track"])

JETM4SlimmingHelper.AppendContentToStream(JETM4Stream)
