# Configuration functions for SoftMuonTag
# Author: Wouter van den Wollenberg (2013-2014)
from BTagging.BTaggingFlags import BTaggingFlags

metaSoftMuonTag = { 'IsATagger'            : True,
                    'NeedsMuonAssociator'  : True,
                    'DependsOn'            : ['AtlasExtrapolator',
                                              'BTagTrackToVertexTool',
                                              'BTagFullLinearizedTrackFactory',
                                              'BTagTrackToVertexIPEstimator',
                                              'SoftMuonTagNewLikelihoodTool'],
                    'PassByPointer'        : {'LikelihoodTool'    : 'SoftMuonTagNewLikelihoodTool',
                                              'TrackToVertexTool' : 'BTagTrackToVertexTool'},
                    'JetCollectionList'    : 'jetCollectionList',
                    'ToolCollection'       : 'SoftMuonTag' }

def toolSoftMuonTag(name, useBTagFlagsDefaults = True, **options):
    """Sets up a SoftMuonTag tool and returns it.

    The following options have BTaggingFlags defaults:

    OutputLevel                         default: BTaggingFlags.OutputLevel
    Runmodus                            default: BTaggingFlags.Runmodus
    jetCollectionList                   default: BTaggingFlags.Jets
    originalMuCollectionName            default: BTaggingFlags.MuonCollectionName
    BTagJetEtamin                       default: 2.5 (only if BTaggingFlags.Runmodus == 'reference')

    input:             name: The name of the tool (should be unique).
      useBTagFlagsDefaults : Whether to use BTaggingFlags defaults for options that are not specified.
                  **options: Python dictionary with options for the tool.
    output: The actual tool, which can then by added to ToolSvc via ToolSvc += output."""
    if useBTagFlagsDefaults:
        defaults = { 'OutputLevel'                      : BTaggingFlags.OutputLevel,
                     'Runmodus'                         : BTaggingFlags.Runmodus,
                     'jetCollectionList'                : BTaggingFlags.Jets,
                     'originalMuCollectionName'         : BTaggingFlags.MuonCollectionName }
        if(BTaggingFlags.Runmodus == 'reference'):
            defaults['BTagJetEtamin'] = 2.5
        for option in defaults:
            options.setdefault(option, defaults[option])
    options['name'] = name
    from JetTagTools.JetTagToolsConf import Analysis__SoftMuonTag
    return Analysis__SoftMuonTag(**options)

#----------------------------------------------------------------------

metaSoftMuonTagNewLikelihoodTool = { 'CalibrationFolders' : ['SoftMu',],
                                     'DependsOn'          : ['BTagCalibrationBrokerTool',],
                                     'PassByPointer'      : {'calibrationTool' : 'BTagCalibrationBrokerTool'},
                                     'ToolCollection'     : 'SoftMuonTag' }

def toolSoftMuonTagNewLikelihoodTool(name, useBTagFlagsDefaults = True, **options):
    """Sets up a SoftMuonTagNewLikelihoodTool tool and returns it.

    The following options have BTaggingFlags defaults:

    OutputLevel                         default: BTaggingFlags.OutputLevel
    taggerName                          default: "SoftMu"
    smoothNTimes                        default: 0 (1 if BTaggingFlags.Runmodus == 'reference')
    normalizedProb                      default: True
    interpolate                         default: True

    input:             name: The name of the tool (should be unique).
      useBTagFlagsDefaults : Whether to use BTaggingFlags defaults for options that are not specified.
                  **options: Python dictionary with options for the tool.
    output: The actual tool, which can then by added to ToolSvc via ToolSvc += output."""
    if useBTagFlagsDefaults:
        defaults = { 'OutputLevel'                         : BTaggingFlags.OutputLevel,
                     'taggerName'                          : 'SoftMu',
                     'smoothNTimes'                        : 0,
                     'normalizedProb'                      : True,
                     'interpolate'                         : True }
        if(BTaggingFlags.Runmodus == 'reference'):
            defaults['smoothNTimes'] = 1
        for option in defaults:
            options.setdefault(option, defaults[option])
    options['name'] = name
    from JetTagTools.JetTagToolsConf import Analysis__NewLikelihoodTool
    return Analysis__NewLikelihoodTool(**options)
