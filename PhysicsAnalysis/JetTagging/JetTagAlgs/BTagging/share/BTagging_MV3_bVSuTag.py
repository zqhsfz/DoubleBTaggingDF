from JetTagTools.JetTagToolsConf import Analysis__MV3Tag
MV3_bVSuTagTool = Analysis__MV3Tag(
                              name = "MV3_bVSuTag",
                              Runmodus = BTaggingFlags.Runmodus,
                              calibrationTool = BTagCalibrationBrokerTool,
                              forceMV3CalibrationAlias = BTaggingFlags.ForceMV3CalibrationAlias,
                              MV3CalibAlias =  BTaggingFlags.MV3CalibAlias,
                              MV3Flavor = "bVSu",
                              OutputLevel = BTaggingFlags.OutputLevel
                             )
ToolSvc += MV3_bVSuTagTool
if BTaggingFlags.OutputLevel < 3:
  print MV3_bVSuTagTool
