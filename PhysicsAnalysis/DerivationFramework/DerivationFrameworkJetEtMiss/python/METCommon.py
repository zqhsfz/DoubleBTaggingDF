#********************************************************************
# METCommon.py
# Schedules default DF MET content building tools and writes the
# results into SG. These may then be accessed along the train  
#********************************************************************
from DerivationFrameworkCore.DerivationFrameworkMaster import *

##########################################################################################
# MET
##########################################################################################

# Set up custom MET reconstruction algorithms
from METReconstruction.METRecoFlags import metFlags
from METReconstruction.METRecoConfig import BuildConfig, RefConfig, METConfig, getMETRecoAlg

METLists = {}

#simplelist = ['EMTopo','LocHadTopo','Truth','Track','EMTopoRegions','LocHadTopoRegions','TruthRegions',
#	      'Core_AntiKt4EMPFlow', 'Core_AntiKt4EMTopo', 'Core_AntiKt4LCTopo',
#	      'Reference_AntiKt4EMPFlow', 'Reference_AntiKt4EMTopo', 'Reference_AntiKt4LCTopo',]
xaodlist = ['Calo', 'EMTopo', 'EMTopoRegions', 'LocHadTopo', 'LocHadTopoRegions',
	    'Track', 'Truth', 'TruthRegions']
maplist = ['AntiKt4LCTopo','AntiKt4EMTopo','AntiKt4EMPFlow']
METLists['Diagnostic'] = ['Calo','EMTopo','EMTopoRegions','LocHadTopo','LocHadTopoRegions','TruthRegions']

def addMETOutputs(slimhelper, contentlist=[], slimlist=[]):
	suffixlist = ['Truth','AntiKt4EMTopo']
	for content in contentlist:
		if content in METLists.keys():
			suffixlist += METLists[content]
		else:
			suffixlist.append(content)
	for suffix in suffixlist:
		print "DFMissingET -- Add containers for MET_"+suffix+" to output"
		if suffix in maplist:
			if suffix in slimlist:
				slimhelper.SmartCollections.append("MET_Reference_"+suffix)
			else:
				slimhelper.AllVariables.append("METAssoc_"+suffix)
				slimhelper.AllVariables.append("MET_Core_"+suffix)
				slimhelper.AllVariables.append("MET_Reference_"+suffix)
		# if (suffix in simplelist):
		if suffix in xaodlist:
			if suffix in slimlist:
				slimhelper.SmartCollections.append("MET_"+suffix)
			else:
				slimhelper.AllVariables.append("MET_"+suffix)
		else:
			slimhelper.StaticContent.append("xAOD::MissingETContainer#MET_"+suffix)
			slimhelper.StaticContent.append("xAOD::MissingETAuxContainer#MET_"+suffix+"Aux.")
		# else:
		# 	slimhelper.StaticContent.append("xAOD::MissingETContainer#MET_"+suffix)
		# 	slimhelper.StaticContent.append("xAOD::MissingETAuxContainer#MET_"+suffix+"Aux.")
		# 	slimhelper.StaticContent.append("xAOD::MissingETComponentMap#METMap_"+suffix)
		# 	slimhelper.StaticContent.append("xAOD::MissingETAuxComponentMap#METMap_"+suffix+"Aux.")
