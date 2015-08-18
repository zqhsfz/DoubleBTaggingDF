import os

#####################################################################################################################################################
# RSG sample
#####################################################################################################################################################
MClist = [
           "mc15_13TeV.301495.MadGraphPythia8EvtGen_A14NNPDF23LO_RS_G_hh_bbbb_c10_M1000.merge.AOD.e3820_s2608_s2183_r6630_r6264/",
           # "mc15_13TeV.301497.MadGraphPythia8EvtGen_A14NNPDF23LO_RS_G_hh_bbbb_c10_M1200.merge.AOD.e3820_s2608_s2183_r6630_r6264/",
           # "mc15_13TeV.301498.MadGraphPythia8EvtGen_A14NNPDF23LO_RS_G_hh_bbbb_c10_M1300.merge.AOD.e3820_s2608_s2183_r6630_r6264/",
           # "mc15_13TeV.301499.MadGraphPythia8EvtGen_A14NNPDF23LO_RS_G_hh_bbbb_c10_M1400.merge.AOD.e3820_s2608_s2183_r6630_r6264/",
           "mc15_13TeV.301500.MadGraphPythia8EvtGen_A14NNPDF23LO_RS_G_hh_bbbb_c10_M1500.merge.AOD.e3820_s2608_s2183_r6630_r6264/",
           # "mc15_13TeV.301501.MadGraphPythia8EvtGen_A14NNPDF23LO_RS_G_hh_bbbb_c10_M1600.merge.AOD.e3820_s2608_s2183_r6630_r6264/",
           # "mc15_13TeV.301502.MadGraphPythia8EvtGen_A14NNPDF23LO_RS_G_hh_bbbb_c10_M1800.merge.AOD.e3820_s2608_s2183_r6630_r6264/",
           "mc15_13TeV.301503.MadGraphPythia8EvtGen_A14NNPDF23LO_RS_G_hh_bbbb_c10_M2000.merge.AOD.e3820_s2608_s2183_r6630_r6264/",
           # "mc15_13TeV.301504.MadGraphPythia8EvtGen_A14NNPDF23LO_RS_G_hh_bbbb_c10_M2250.merge.AOD.e3820_s2608_s2183_r6630_r6264/",
           "mc15_13TeV.301505.MadGraphPythia8EvtGen_A14NNPDF23LO_RS_G_hh_bbbb_c10_M2500.merge.AOD.e3820_s2608_s2183_r6630_r6264/",
           # "mc15_13TeV.301506.MadGraphPythia8EvtGen_A14NNPDF23LO_RS_G_hh_bbbb_c10_M2750.merge.AOD.e3820_s2608_s2183_r6630_r6264/",
           "mc15_13TeV.301507.MadGraphPythia8EvtGen_A14NNPDF23LO_RS_G_hh_bbbb_c10_M3000.merge.AOD.e3820_s2608_s2183_r6630_r6264/",
         ]
nFilesPerJob = 1
#####################################################################################################################################################

#####################################################################################################################################################
# JZXW sample
#####################################################################################################################################################
# MClist = [
#           "mc15_13TeV.361023.Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ3W.merge.AOD.e3668_s2576_s2132_r6630_r6264/",    # 399 files, 1990500 events
#           "mc15_13TeV.361024.Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ4W.merge.AOD.e3668_s2576_s2132_r6630_r6264/",    # 396 files, 1977200 events
#           "mc15_13TeV.361025.Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ5W.merge.AOD.e3668_s2576_s2132_r6630_r6264/",    # 391 files, 1951200 events
#           "mc15_13TeV.361026.Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ6W.merge.AOD.e3569_s2608_s2183_r6630_r6264/",    # 377 files, 1882400 events
#           "mc15_13TeV.361027.Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ7W.merge.AOD.e3668_s2608_s2183_r6630_r6264/",    # 357 files, 1783200 events
#           "mc15_13TeV.361028.Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ8W.merge.AOD.e3569_s2576_s2132_r6630_r6264/",    # 349 files, 1743200 events
#           "mc15_13TeV.361029.Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ9W.merge.AOD.e3569_s2576_s2132_r6630_r6264/",    # 364 files, 1817195 events
#           "mc15_13TeV.361030.Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ10W.merge.AOD.e3569_s2576_s2132_r6630_r6264/",   # 386 files, 1923500 events
#           "mc15_13TeV.361031.Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ11W.merge.AOD.e3569_s2608_s2183_r6630_r6264/",   # 400 files, 1997200 events (? -- not sure if this is the correct sample to use)
#           "mc15_13TeV.361032.Pythia8EvtGen_A14NNPDF23LO_jetjet_JZ12W.merge.AOD.e3668_s2608_s2183_r6630_r6264/",   # 395 files, 1974600 events
#          ]
# nFilesPerJob = 4
#####################################################################################################################################################

# vabc: "a" is main version number, "b" is sub-version number and "c" is debug number
version = "v102"

for MC in MClist:
	print "#####################################################################################"
	print "#####################################################################################"

	outputname = "user.qzeng.%s.DAOD_JETM8_bb.%s/" % (MC.replace("/", ""), version)

	if len(outputname) > 115:
		print "output is too long. Get slimmed down"
		outputname_split = outputname.split(".")
		outputname_split.pop(4)
		outputname = ".".join(outputname_split)

	cmd = "pathena --cmtConfig=x86_64-slc6-gcc48-opt --useNewTRF --trf 'Reco_tf.py --inputAODFile %%IN --outputDAODFile pool.root --reductionConf JETM8' --extOutFile DAOD_JETM8.pool.root --nFilesPerJob %i --individualOutDS --inDS %s --outDS %s --skipScout" % (nFilesPerJob, MC, outputname)

	print cmd
	os.system(cmd)







