#********************************************************************
# ExtendedJetCommon.py
# Schedules special jet tools
#********************************************************************

from DerivationFrameworkCore.DerivationFrameworkMaster import *
from DerivationFrameworkJetEtMiss.JetCommon import *
from JetRec.JetRecFlags import jetFlags

##################################################################

def addDefaultTrimmedJets(sequence,outputlist,dotruth=True,**extraOptions):
    if jetFlags.useTruth and dotruth:
        addTrimmedJets("AntiKt", 1.0, "Truth", rclus=0.2, ptfrac=0.05, algseq=sequence, outputGroup=outputlist,**extraOptions)
    addTrimmedJets("AntiKt", 1.0, "LCTopo", rclus=0.2, ptfrac=0.05, algseq=sequence, outputGroup=outputlist,**extraOptions)

##################################################################

def applyJetCalibration(jetalg,algname,sequence):
    if hasattr(sequence,algname):
        jetaug = getattr(sequence,algname)
    else:
        jetaug = CfgMgr.DerivationFramework__CommonAugmentation(algname)
        sequence += jetaug
    from AthenaCommon.AppMgr import ToolSvc
    calibtoolname = "DFJetCalib_"+jetalg
    jetaugtoolname = "DFJetAug_"+jetalg
    jetaugtool = None
    if hasattr(ToolSvc,jetaugtoolname):
        jetaugtool = getattr(ToolSvc,jetaugtoolname)
    else:
        jetaugtool = CfgMgr.DerivationFramework__JetAugmentationTool(jetaugtoolname,
                                                                     InputJets=jetalg+"Jets")
        ToolSvc += jetaugtool

    if hasattr(ToolSvc,calibtoolname):
        jetaugtool.JetCalibTool = getattr(ToolSvc,calibtoolname)
    else:
        isdata=False
        calibseq="JetArea_Residual_Origin_EtaJES_GSC"
        config = "JES_MC15Prerecommendation_April2015.config"
        from AthenaCommon.GlobalFlags import globalflags
        if not globalflags.DataSource()=='geant4': 
            calibseq+="Insitu"
            isdata=True
        if jetalg == "AntiKt10LCTopoTrimmedPtFrac5SmallR20":
            calibseq="EtaJES"
            config = "JES_MC15recommendation_FatJet_June2015.config"

        calibtool = CfgMgr.JetCalibrationTool(
            calibtoolname,
            JetCollection=jetalg,
            ConfigFile=config,
            CalibSequence=calibseq,
            IsData=isdata
            )
        ToolSvc += calibtool
        jetaugtool.JetCalibTool = calibtool

    print "Applying calibration to jet collection:", jetalg+"Jets"

    if not jetaugtool in jetaug.AugmentationTools:
        jetaug.AugmentationTools.append(jetaugtool)

def applyJetCalibration_xAODColl(jetalg="AntiKt4EMTopo",sequence=DerivationFrameworkJob):
    supportedJets = ["AntiKt4EMTopo"]
    if not jetalg in supportedJets:
        print "ExtendedJetCommon: *** WARNING: Calibration requested for unsupported jet collection! ***"
        return
    else:
        applyJetCalibration(jetalg,"JetCommonKernel_xAODJets",sequence)

def applyJetCalibration_CustomColl(jetalg="AntiKt10LCTopoTrimmedPtFrac5SmallR20",sequence=None):
    supportedJets = ["AntiKt10LCTopoTrimmedPtFrac5SmallR20"]
    if not jetalg in supportedJets:
        print "ExtendedJetCommon: *** WARNING: Calibration requested for unsupported jet collection! ***"
        print "ExtendedJetCommon: Supported custom jets:", supportedJets
        return
    else:
        applyJetCalibration(jetalg,"JetCommonKernel_OTFJets",sequence)

##################################################################

def replaceBuggyAntiKt4TruthWZJets(algseq,outputGroup="BugFix"):
    if jetFlags.useTruth:

        jetnamebase = "AntiKt4TruthWZ"
        jetname = jetnamebase+"Jets"
        algname = "jetalg"+jetnamebase
        OutputJets.setdefault(outputGroup , [] ).append(jetname)

        # return if the alg is already scheduled here :
        if algseq is None:
            print "No algsequence passed! Will not schedule", algname
            return
        elif algname in DFJetAlgs:
            if hasattr(algseq,algname):
                print "   Algsequence", algseq, "already has an instance of", algname
            else:
                print "   Added", algname, "to sequence", algseq
                algseq += DFJetAlgs[algname]
            return DFJetAlgs[algname]

        if not jetname in jtm.tools:

            finderTool= jtm.addJetFinder(jetname, "AntiKt", 0.4, "truthwz",ptmin=5000,
                                         overwrite=True, warnIfDuplicate=False)

            from JetRec.JetRecConf import JetAlgorithm
            alg = JetAlgorithm(algname, Tools = [finderTool])
            print "   Added", algname, "to sequence", algseq
            algseq += alg
            DFJetAlgs[algname] = alg;

def replaceBuggyAntiKt10TruthWZJets(algseq,outputGroup="BugFix"):
    if jetFlags.useTruth:

        jetnamebase = "AntiKt10TruthWZ"
        jetname = jetnamebase+"Jets"
        algname = "jetalg"+jetnamebase
        OutputJets.setdefault(outputGroup , [] ).append(jetname)

        # return if the alg is already scheduled here :
        if algseq is None:
            print "No algsequence passed! Will not schedule", algname
            return
        elif algname in DFJetAlgs:
            if hasattr(algseq,algname):
                print "   Algsequence", algseq, "already has an instance of", algname
            else:
                print "   Added", algname, "to sequence", algseq
                algseq += DFJetAlgs[algname]
            return DFJetAlgs[algname]

        if not jetname in jtm.tools:

            finderTool= jtm.addJetFinder(jetname, "AntiKt", 1.0, "truthwz",ptmin=40000,
                                         overwrite=True, warnIfDuplicate=False)

            from JetRec.JetRecConf import JetAlgorithm
            alg = JetAlgorithm(algname, Tools = [finderTool])
            print "   Added", algname, "to sequence", algseq
            algseq += alg
            DFJetAlgs[algname] = alg;

##################################################################
