# Configuration functions for MV2mTag
# Author: Wouter van den Wollenberg (2013-2014)
from BTagging.BTaggingFlags import BTaggingFlags

metaMV2mTag = { 'IsATagger'          : True,
                'xAODBaseName'       : 'MV2m',
                'DependsOn'          : ['AtlasExtrapolator',
                                        'BTagTrackToVertexTool',
                                        'BTagCalibrationBrokerTool',
                                        'IP2DTag',
                                        'IP3DTag',
                                        'JetFitterTagCOMBNN',
                                        'SV0Tag',
                                        'SV1Tag'],
                'CalibrationFolders' : ['MV2m',],
                'PassByPointer'      : {'calibrationTool' : 'BTagCalibrationBrokerTool'},
                'ToolCollection'     : 'MV2mTag' }

def toolMV2mTag(name, useBTagFlagsDefaults = True, **options):
    """Sets up a MV2mTag tool and returns it.

    The following options have BTaggingFlags defaults:

    OutputLevel                         default: BTaggingFlags.OutputLevel
    Runmodus                            default: BTaggingFlags.Runmodus
    taggerName                          default: "MV2m"
    taggerNameBase                      default: "MV2m"
    forceMV2CalibrationAlias            default: BTaggingFlags.ForceMV2CalibrationAlias
    MV2CalibAlias                       default: BTaggingFlags.MV2CalibAlias
    inputSV0SourceName                  default: "SV0"
    inputSV1SourceName                  default: "SV1"
    inputIP2DSourceName                 default: "IP2D"
    inputIP3DSourceName                 default: "IP3D"
    inputJFSourceName                   default: "JetFitter"
    inputJFProbSourceName               default: "JetFitterCombNN"
    trainingConfig                      default: BTaggingFlags.MV2mTrainingConfig

    input:             name: The name of the tool (should be unique).
      useBTagFlagsDefaults : Whether to use BTaggingFlags defaults for options that are not specified.
                  **options: Python dictionary with options for the tool.
    output: The actual tool, which can then by added to ToolSvc via ToolSvc += output."""
    if useBTagFlagsDefaults:
        defaults = { 'OutputLevel'                      : BTaggingFlags.OutputLevel,
                     'Runmodus'                         : BTaggingFlags.Runmodus,
                     'taggerName'                       : 'MV2m',
                     'taggerNameBase'                   : 'MV2m',
                     'forceMV2CalibrationAlias'         : BTaggingFlags.ForceMV2CalibrationAlias,
                     'MV2CalibAlias'                    : BTaggingFlags.MV2CalibAlias,
                     'inputSV0SourceName'               : 'SV0',
                     'inputSV1SourceName'               : 'SV1',
                     'inputIP2DSourceName'              : 'IP2D',
                     'inputIP3DSourceName'              : 'IP3D',
                     'inputJFSourceName'                : 'JetFitter',
                     'inputJFProbSourceName'            : 'JetFitterCombNN',
                     'trainingConfig'                   : BTaggingFlags.MV2mTrainingConfig,
                     }
        for option in defaults:
            options.setdefault(option, defaults[option])
    options['name'] = name
    from JetTagTools.JetTagToolsConf import Analysis__MV2Tag
    return Analysis__MV2Tag(**options)
