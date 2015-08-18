#====================================================================
# FTAG1.py
# It requires the reductionConf flag FTAG1 in Reco_tf.py
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
from DerivationFrameworkFlavourTag.FlavourTagCommon import FlavorTagInit
FlavorTagInit(isFTAG1=True)


#====================================================================
# SKIMMING TOOLS 
#====================================================================
from DerivationFrameworkTools.DerivationFrameworkToolsConf import DerivationFramework__xAODStringSkimmingTool

if globalflags.DataSource()=='data':
    triggers=[
        #single jet triggers with online b-tagging information (online taggers)
        "HLT_j15_bperf",
        "HLT_j25_bperf",
        "HLT_j35_bperf",
        "HLT_j45_bperf",
        "HLT_j55_bperf",
        "HLT_j85_bperf",
        "HLT_j110_bperf",
        "HLT_j150_bperf",
        "HLT_j260_bperf",
        "HLT_j320_bperf",
        "HLT_j400_bperf",
        "HLT_j45_bperf_3j45_L14J20",
        "HLT_j45_bperf_3j45_L13J15.0ETA25",
        "HLT_j45_bperf_3j45_L13J20",
        #single jet triggers with online b-tagging information (online taggers - split version)
        "HLT_j15_bperf_split",
        "HLT_j25_bperf_split",
        "HLT_j35_bperf_split",
        "HLT_j45_bperf_split",
        "HLT_j55_bperf_split",
        "HLT_j85_bperf_split",
        "HLT_j110_bperf_split",
        "HLT_j150_bperf_split",
        "HLT_j260_bperf_split",
        "HLT_j320_bperf_split",
        "HLT_j400_bperf_split",
        "HLT_j45_bperf_split_3j45_L14J20",
        "HLT_j45_bperf_split_3j45_L13J15.0ETA25",
        "HLT_j45_bperf_split_3j45_L13J20",
        #single jet triggers with online b-tagging information (offline taggers)
        "HLT_j15_boffperf",
        "HLT_j25_boffperf",
        "HLT_j35_boffperf",
        "HLT_j45_boffperf",
        "HLT_j55_boffperf",
        "HLT_j85_boffperf",
        "HLT_j110_boffperf",
        "HLT_j150_boffperf",
        "HLT_j260_boffperf",
        "HLT_j320_boffperf",
        "HLT_j400_boffperf",
        "HLT_j45_boffperf_3j45",
        "HLT_j45_boffperf_3j45_L13J15.0ETA25",
        "HLT_j45_boffperf_3j45_L13J20",
        #single jet triggers with online b-tagging information (offline taggers - split version)
        "HLT_j15_boffperf_split",
        "HLT_j25_boffperf_split",
        "HLT_j35_boffperf_split",
        "HLT_j45_boffperf_split",
        "HLT_j55_boffperf_split",
        "HLT_j85_boffperf_split",
        "HLT_j110_boffperf_split",
        "HLT_j150_boffperf_split",
        "HLT_j260_boffperf_split",
        "HLT_j320_boffperf_split",
        "HLT_j400_boffperf_split",
        "HLT_j45_boffperf_split_3j45",
        "HLT_j45_boffperf_split_3j45_L13J15.0ETA25",
        "HLT_j45_boffperf_split_3j45_L13J20",
        #single jet triggers
        "HLT_j15",
        "HLT_j25",
        "HLT_j35",
        "HLT_j45",
        "HLT_j55",
        "HLT_j60",
        "HLT_j85",
        "HLT_j100",
        "HLT_j110",
        "HLT_j150",
        "HLT_j175",
        "HLT_j200",
        "HLT_j260",
        "HLT_j300",
        "HLT_j320",
        "HLT_j360",
        "HLT_j380",
        "HLT_j400",
        "HLT_j420",
        "HLT_j440",
        "HLT_j460"
        ]
    
    ORStr=" || "
    triggerStr=ORStr.join(triggers)
    triggerExpression = "(EventInfo.eventTypeBitmask==1) || (" + triggerStr +" )"
    
else:
    triggers = []
    triggerExpression = "(EventInfo.eventTypeBitmask==1)"

FTAG1StringSkimmingTool = DerivationFramework__xAODStringSkimmingTool(name = "FTAG1StringSkimmingTool",
                                                                      expression = triggerExpression)

ToolSvc += FTAG1StringSkimmingTool
print FTAG1StringSkimmingTool

#====================================================================
# CREATE THE DERIVATION KERNEL ALGORITHM AND PASS THE ABOVE TOOLS
#====================================================================

# The name of the kernel (LooseSkimKernel in this case) must be unique to this derivation
from DerivationFrameworkCore.DerivationFrameworkCoreConf import DerivationFramework__DerivationKernel
DerivationFrameworkJob += CfgMgr.DerivationFramework__DerivationKernel("FTAG1Kernel",
                                                                        SkimmingTools = [FTAG1StringSkimmingTool]
                                                                      )


#====================================================================
# SET UP STREAM   
#====================================================================

# The base name (DAOD_FTAG1 here) must match the string in
streamName = derivationFlags.WriteDAOD_FTAG1Stream.StreamName
fileName   = buildFileName( derivationFlags.WriteDAOD_FTAG1Stream )
FTAG1Stream = MSMgr.NewPoolRootStream( streamName, fileName )
# Only events that pass the filters listed below are written out.
# Name must match that of the kernel above
# AcceptAlgs  = logical OR of filters
# RequireAlgs = logical AND of filters
FTAG1Stream.AcceptAlgs(["FTAG1Kernel"])

from DerivationFrameworkCore.SlimmingHelper import SlimmingHelper
FTAG1SlimmingHelper = SlimmingHelper("FTAG1SlimmingHelper")

#Need to add explicitely then new container names and types to the Slimming dictionary
FTAG1SlimmingHelper.AppendToDictionary = {
"BTagging_AntiKt4EMTopoNT":"xAOD::BTaggingContainer",
"BTagging_AntiKt4EMTopoNTAux":"xAOD::BTaggingAuxContainer",
"BTagging_AntiKt4EMTopoNTJFVtx":"xAOD::BTagVertexContainer",
"BTagging_AntiKt4EMTopoNTJFVtxAux":"xAOD::BTagVertexAuxContainer"
}


# nb: BTagging_AntiKt4EMTopo smart collection includes both AntiKt4EMTopoJets and BTagging_AntiKt4EMTopo
# container variables. Thus BTagging_AntiKt4EMTopo is needed in SmartCollections as well as AllVariables
FTAG1SlimmingHelper.SmartCollections = ["Electrons","Muons",
                                        "MET_Reference_AntiKt4EMTopo",
                                        "AntiKt4EMTopoJets",
                                        "BTagging_AntiKt4EMTopo"]

FTAG1SlimmingHelper.AllVariables = ["AntiKt3PV0TrackJets",
                                    "AntiKt2PV0TrackJets",
                                    "AntiKt4TruthJets",
                                    "BTagging_AntiKt4EMTopo",
                                    "BTagging_AntiKt4EMTopoNT",
                                    "BTagging_AntiKt4EMTopoSecVtx",
                                    "BTagging_AntiKt2Track",
                                    "BTagging_AntiKt3Track",
                                    "BTagging_AntiKt4EMTopoJFVtx",
                                    "BTagging_AntiKt4EMTopoNTJFVtx",
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

FTAG1SlimmingHelper.ExtraVariables.append(AntiKt4EMTopoJetsCPContent[1].replace("AntiKt4EMTopoJetsAux","AntiKt10LCTopoJets"))

FTAG1SlimmingHelper.IncludeMuonTriggerContent = True
FTAG1SlimmingHelper.IncludeEGammaTriggerContent = True
FTAG1SlimmingHelper.IncludeJetTriggerContent = True
FTAG1SlimmingHelper.IncludeEtMissTriggerContent = True
FTAG1SlimmingHelper.IncludeBJetTriggerContent = True

FTAG1SlimmingHelper.AppendContentToStream(FTAG1Stream)
