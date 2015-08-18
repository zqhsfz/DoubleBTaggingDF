#====================================================================
# FTAG2.py
# It requires the reductionConf flag FTAG2 in Reco_tf.py
#====================================================================

# Set up common services and job object.
# This should appear in ALL derivation job options
from DerivationFrameworkCore.DerivationFrameworkMaster import *
from DerivationFrameworkInDet.InDetCommon import *
from DerivationFrameworkJetEtMiss.JetCommon import *
#from DerivationFrameworkJetEtMiss.ExtendedJetCommon import *
from DerivationFrameworkJetEtMiss.METCommon import *
from DerivationFrameworkEGamma.EGammaCommon import *
from DerivationFrameworkMuons.MuonsCommon import *
#from DerivationFrameworkFlavourTag.FlavourTagCommon import FlavorTagInit
#FlavorTagInit()


#====================================================================
# SKIMMING TOOLS
#====================================================================
from DerivationFrameworkTools.DerivationFrameworkToolsConf import DerivationFramework__xAODStringSkimmingTool
FTAG2StringSkimmingTool = DerivationFramework__xAODStringSkimmingTool(name = "FTAG2StringSkimmingTool",
                                                                            expression = 'count( (Muons.pt > 18*GeV) && (Muons.DFCommonGoodMuon) ) + count(( Electrons.pt > 18*GeV) && ((Electrons.Loose) || (Electrons.DFCommonElectronsLHLoose))) >= 2 ')

ToolSvc += FTAG2StringSkimmingTool
print FTAG2StringSkimmingTool

#====================================================================
# CREATE THE DERIVATION KERNEL ALGORITHM AND PASS THE ABOVE TOOLS
#====================================================================

# The name of the kernel (LooseSkimKernel in this case) must be unique to this derivation
from DerivationFrameworkCore.DerivationFrameworkCoreConf import DerivationFramework__DerivationKernel
DerivationFrameworkJob += CfgMgr.DerivationFramework__DerivationKernel("FTAG2Kernel",
                                                                       SkimmingTools = [FTAG2StringSkimmingTool]
                                                                       )


#====================================================================
# SET UP STREAM
#====================================================================

# The base name (DAOD_FTAG2 here) must match the string in
streamName = derivationFlags.WriteDAOD_FTAG2Stream.StreamName
fileName   = buildFileName( derivationFlags.WriteDAOD_FTAG2Stream )
FTAG2Stream = MSMgr.NewPoolRootStream( streamName, fileName )
# Only events that pass the filters listed below are written out.
# Name must match that of the kernel above
# AcceptAlgs  = logical OR of filters
# RequireAlgs = logical AND of filters
FTAG2Stream.AcceptAlgs(["FTAG2Kernel"])

from DerivationFrameworkCore.SlimmingHelper import SlimmingHelper
FTAG2SlimmingHelper = SlimmingHelper("FTAG2SlimmingHelper")

# nb: BTagging_AntiKt4EMTopo smart collection includes both AntiKt4EMTopoJets and BTagging_AntiKt4EMTopo 
# container variables. Thus BTagging_AntiKt4EMTopo is needed in SmartCollections as well as AllVariables
FTAG2SlimmingHelper.SmartCollections = ["Electrons","Muons",
                                        "MET_Reference_AntiKt4EMTopo",
                                        "AntiKt4EMTopoJets",
                                        "BTagging_AntiKt4EMTopo"] 

FTAG2SlimmingHelper.AllVariables = ["AntiKt3PV0TrackJets",
                                    "AntiKt2PV0TrackJets",
                                    "AntiKt4TruthJets",
                                    "BTagging_AntiKt4EMTopo",
                                    "BTagging_AntiKt2Track",
                                    "BTagging_AntiKt3Track",
                                    "BTagging_AntiKt4EMTopoJFVtx",
                                    "BTagging_AntiKt2TrackJFVtx",
                                    "BTagging_AntiKt3TrackJFVtx",
                                    "BTagging_AntiKt4EMTopoSecVtx",
                                    "BTagging_AntiKt2TrackSecVtx",
                                    "BTagging_AntiKt3TrackSecVtx",
                                    "TruthVertices",
                                    "TruthParticles",
                                    "TruthEvents",
                                    "MET_Truth",
                                    "MET_TruthRegions",
                                    "InDetTrackParticles",
                                    "PrimaryVertices"
                                    ]



from DerivationFrameworkCore.AntiKt4EMTopoJetsCPContent import AntiKt4EMTopoJetsCPContent

FTAG2SlimmingHelper.ExtraVariables.append(AntiKt4EMTopoJetsCPContent[1].replace("AntiKt4EMTopoJetsAux","AntiKt10LCTopoJets"))

FTAG2SlimmingHelper.IncludeMuonTriggerContent = True
FTAG2SlimmingHelper.IncludeEGammaTriggerContent = True
FTAG2SlimmingHelper.IncludeJetTriggerContent = True
FTAG2SlimmingHelper.IncludeEtMissTriggerContent = True
FTAG2SlimmingHelper.IncludeBJetTriggerContent = True

FTAG2SlimmingHelper.AppendContentToStream(FTAG2Stream)
