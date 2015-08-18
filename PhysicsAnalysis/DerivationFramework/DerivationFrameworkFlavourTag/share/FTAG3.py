#====================================================================
# FTAG3.py
# It requires the reductionConf flag FTAG3 in Reco_tf.py
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

print "AACC test"

#====================================================================
# SKIMMING TOOLS BASED ON THE TRIGGER DECISION TOOL
#====================================================================
if globalflags.DataSource()=='data':
    triggerRegEx = ['HLT_mu[4-6]_j.*[0-9][0-9]_dr05', 'HLT_mu[4-6]_j.*[0-9][0-9]_bperf.*', ]
else:
    triggerRegEx = ['HLT_.*']

from DerivationFrameworkTools.DerivationFrameworkToolsConf import DerivationFramework__TriggerSkimmingTool
FTAG3TriggerSkimmingTool = DerivationFramework__TriggerSkimmingTool(name = "FATG3TriggerSkimmingTool",
                                                                    TriggerListOR  = triggerRegEx)
    
ToolSvc += FTAG3TriggerSkimmingTool
print FTAG3TriggerSkimmingTool

#====================================================================
# CREATE THE DERIVATION KERNEL ALGORITHM AND PASS THE ABOVE TOOLS
#====================================================================

# The name of the kernel (LooseSkimKernel in this case) must be unique to this derivation
from DerivationFrameworkCore.DerivationFrameworkCoreConf import DerivationFramework__DerivationKernel
DerivationFrameworkJob += CfgMgr.DerivationFramework__DerivationKernel("FTAG3Kernel",
                                                                       SkimmingTools = [FTAG3TriggerSkimmingTool]
                                                                       )


#====================================================================
# SET UP STREAM
#====================================================================

# The base name (DAOD_FTAG3 here) must match the string in
streamName = derivationFlags.WriteDAOD_FTAG3Stream.StreamName
fileName   = buildFileName( derivationFlags.WriteDAOD_FTAG3Stream )
FTAG3Stream = MSMgr.NewPoolRootStream( streamName, fileName )
# Only events that pass the filters listed below are written out.
# Name must match that of the kernel above
# AcceptAlgs  = logical OR of filters
# RequireAlgs = logical AND of filters
FTAG3Stream.AcceptAlgs(["FTAG3Kernel"])

from DerivationFrameworkCore.SlimmingHelper import SlimmingHelper
FTAG3SlimmingHelper = SlimmingHelper("FTAG3SlimmingHelper")

# nb: BTagging_AntiKt4EMTopo smart collection includes both AntiKt4EMTopoJets and BTagging_AntiKt4EMTopo
# container variables. Thus BTagging_AntiKt4EMTopo is needed in SmartCollections as well as AllVariables 
FTAG3SlimmingHelper.SmartCollections = ["Electrons","Muons",
                                        "MET_Reference_AntiKt4EMTopo",
                                        "AntiKt4EMTopoJets",
                                        "BTagging_AntiKt4EMTopo"]

FTAG3SlimmingHelper.AllVariables =  ["AntiKt3PV0TrackJets",
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

FTAG3SlimmingHelper.ExtraVariables.append(AntiKt4EMTopoJetsCPContent[1].replace("AntiKt4EMTopoJetsAux","AntiKt10LCTopoJets"))

FTAG3SlimmingHelper.IncludeMuonTriggerContent = True
FTAG3SlimmingHelper.IncludeEGammaTriggerContent = True
FTAG3SlimmingHelper.IncludeJetTriggerContent = True
FTAG3SlimmingHelper.IncludeEtMissTriggerContent = True
FTAG3SlimmingHelper.IncludeBJetTriggerContent = True

FTAG3SlimmingHelper.AppendContentToStream(FTAG3Stream)


