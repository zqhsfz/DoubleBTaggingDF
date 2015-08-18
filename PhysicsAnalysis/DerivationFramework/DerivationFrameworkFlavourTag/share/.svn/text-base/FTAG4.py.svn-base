#====================================================================
# FTAG4.py
# It requires the reductionConf flag FTAG4 in Reco_tf.py
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
offlineExpression = '((count((Electrons.pt > 20*GeV) && (Electrons.Medium)) >= 1) || (count( (Muons.pt > 20*GeV) && (Muons.DFCommonGoodMuon) )>=1))'

if globalflags.DataSource()=='data':
    triggers=[
        # primay triggers suggested for periodC
        "HLT_e24_lhmedium_L1EM18VH",
        "HLT_e60_lhmedium",
        "HLT_e120_lhloose",
        "HLT_e24_lhmedium_iloose_L1EM18VH",
        "HLT_e60_lhmedium",
        "HLT_e120_lhloose",
        "HLT_mu20_iloose_L1MU15",
        "HLT_mu40",
        # other single lepton triggers
        "HLT_e24_lhtight_iloose_L1EM20VH",
        "HLT_e24_tight_iloose_L1EM20VH",
        "HLT_mu14_iloose",
        "HLT_e17_loose"
        ]

    ORStr=" || "
    triggerStr=ORStr.join(triggers)
    triggerExpression = "((EventInfo.eventTypeBitmask==1) || (" + triggerStr +" ))"
    expression = offlineExpression+' && '+triggerExpression

else:
    triggers = []
    expression = offlineExpression

from DerivationFrameworkTools.DerivationFrameworkToolsConf import DerivationFramework__xAODStringSkimmingTool
FTAG4StringSkimmingTool = DerivationFramework__xAODStringSkimmingTool(name = "FTAG4StringSkimmingTool",
                                                                      expression = expression)

ToolSvc += FTAG4StringSkimmingTool
print FTAG4StringSkimmingTool

#====================================================================
# CREATE THE DERIVATION KERNEL ALGORITHM AND PASS THE ABOVE TOOLS
#====================================================================

# The name of the kernel (LooseSkimKernel in this case) must be unique to this derivation
from DerivationFrameworkCore.DerivationFrameworkCoreConf import DerivationFramework__DerivationKernel
DerivationFrameworkJob += CfgMgr.DerivationFramework__DerivationKernel("FTAG4Kernel",
                                                                       SkimmingTools = [FTAG4StringSkimmingTool]
                                                                       )


#====================================================================
# SET UP STREAM
#====================================================================

# The base name (DAOD_FTAG4 here) must match the string in
streamName = derivationFlags.WriteDAOD_FTAG4Stream.StreamName
fileName   = buildFileName( derivationFlags.WriteDAOD_FTAG4Stream )
FTAG4Stream = MSMgr.NewPoolRootStream( streamName, fileName )
# Only events that pass the filters listed below are written out.
# Name must match that of the kernel above
# AcceptAlgs  = logical OR of filters
# RequireAlgs = logical AND of filters
FTAG4Stream.AcceptAlgs(["FTAG4Kernel"])

from DerivationFrameworkCore.SlimmingHelper import SlimmingHelper
FTAG4SlimmingHelper = SlimmingHelper("FTAG4SlimmingHelper")

# nb: BTagging_AntiKt4EMTopo smart collection includes both AntiKt4EMTopoJets and BTagging_AntiKt4EMTopo
# container variables. Thus BTagging_AntiKt4EMTopo is needed in SmartCollections as well as AllVariables
FTAG4SlimmingHelper.SmartCollections = ["Electrons","Muons",
                                        "MET_Reference_AntiKt4EMTopo",
                                        "AntiKt4EMTopoJets",
                                        "BTagging_AntiKt4EMTopo"]

FTAG4SlimmingHelper.AllVariables = ["AntiKt3PV0TrackJets",
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

FTAG4SlimmingHelper.ExtraVariables.append(AntiKt4EMTopoJetsCPContent[1].replace("AntiKt4EMTopoJetsAux","AntiKt10LCTopoJets"))

FTAG4SlimmingHelper.IncludeMuonTriggerContent = True
FTAG4SlimmingHelper.IncludeEGammaTriggerContent = True
FTAG4SlimmingHelper.IncludeJetTriggerContent = True
FTAG4SlimmingHelper.IncludeEtMissTriggerContent = True
FTAG4SlimmingHelper.IncludeBJetTriggerContent = True

FTAG4SlimmingHelper.AppendContentToStream(FTAG4Stream)

