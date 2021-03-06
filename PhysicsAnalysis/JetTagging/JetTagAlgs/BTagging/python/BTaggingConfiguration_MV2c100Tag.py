# Configuration functions for MV2c100Tag
# Author: Wouter van den Wollenberg (2013-2014)
from BTagging.BTaggingFlags import BTaggingFlags

metaMV2c100Tag = { 'IsATagger'          : True,
                   'xAODBaseName'       : 'MV2c100',
                   'DependsOn'          : ['AtlasExtrapolator',
                                           'BTagTrackToVertexTool',
                                           'BTagCalibrationBrokerTool',
                                           'IP2DTag',
                                           'IP3DTag',
#                                           'JetFitterTagCOMBNN',
                                           'NewJetFitterVxFinder',
                                           'SV0Tag',
                                           'SV1Tag'],
                   'CalibrationFolders' : ['MV2c100',],
                   'PassByPointer'      : {'calibrationTool' : 'BTagCalibrationBrokerTool'},
                   'ToolCollection'     : 'MV2c100Tag' }

def toolMV2c100Tag(name, useBTagFlagsDefaults = True, **options):
    """Sets up a MV2c100Tag tool and returns it.

    The following options have BTaggingFlags defaults:

    OutputLevel                         default: BTaggingFlags.OutputLevel
    Runmodus                            default: BTaggingFlags.Runmodus
    taggerName                          default: "MV2c100"
    taggerNameBase                      default: "MV2c100"
    forceMV2CalibrationAlias            default: BTaggingFlags.ForceMV2CalibrationAlias
    MV2CalibAlias                       default: BTaggingFlags.MV2CalibAlias
    inputSV0SourceName                  default: "SV0"
    inputSV1SourceName                  default: "SV1"
    inputIP2DSourceName                 default: "IP2D"
    inputIP3DSourceName                 default: "IP3D"
    inputJFSourceName                   default: "JetFitter"
    inputJFProbSourceName               default: "JetFitterCombNN"
    trainingConfig                      default: BTaggingFlags.MV2cTrainingConfig

    input:             name: The name of the tool (should be unique).
      useBTagFlagsDefaults : Whether to use BTaggingFlags defaults for options that are not specified.
                  **options: Python dictionary with options for the tool.
    output: The actual tool, which can then by added to ToolSvc via ToolSvc += output."""
    if useBTagFlagsDefaults:
        defaults = { 'OutputLevel'                      : BTaggingFlags.OutputLevel,
                     'Runmodus'                         : BTaggingFlags.Runmodus,
                     'taggerName'                       : 'MV2c100',
                     'taggerNameBase'                   : 'MV2c100',
                     'forceMV2CalibrationAlias'         : BTaggingFlags.ForceMV2CalibrationAlias,
                     'MV2CalibAlias'                    : BTaggingFlags.MV2CalibAlias,
                     'inputSV0SourceName'               : 'SV0',
                     'inputSV1SourceName'               : 'SV1',
                     'inputIP2DSourceName'              : 'IP2D',
                     'inputIP3DSourceName'              : 'IP3D',
                     'inputJFSourceName'                : 'JetFitter',
                     'inputJFProbSourceName'            : 'JetFitterCombNN',
                     'trainingConfig'                   : BTaggingFlags.MV2cTrainingConfig,
                     }
        for option in defaults:
            options.setdefault(option, defaults[option])
    options['name'] = name
    from JetTagTools.JetTagToolsConf import Analysis__MV2Tag
    return Analysis__MV2Tag(**options)
