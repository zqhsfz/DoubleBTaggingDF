# Configuration functions for MultiSVbb2 (adapted from the Royer's original code)
# Author: Wouter van den Wollenberg (2013-2014)
from BTagging.BTaggingFlags import BTaggingFlags

metaMultiSVbb2Tag = { 'IsATagger'         : True,
                      'xAODBaseName'      : 'MSV',
                      'DependsOn'         : ['AtlasExtrapolator',
                                             'BTagTrackToVertexTool',
                                             'BTagCalibrationBrokerTool',
                                             'InDetVKalMultiVxInJetTool',],
                      'CalibrationFolders' : ['MultiSVbb2',],
                      'PassByPointer'     : {'calibrationTool' : 'BTagCalibrationBrokerTool'},
                      'JetCollectionList' : 'jetCollectionList',
                      'DefaultTracks'     : 'BTagTrackToJetAssociatorBB',
                      'ToolCollection'    : 'MultiSVbb2Tag' }

def toolMultiSVbb2Tag(name, useBTagFlagsDefaults = True, **options):
    """Sets up a MultiSVTag tool and returns it.

    The following options have BTaggingFlags defaults:

    OutputLevel                         default: BTaggingFlags.OutputLevel
    Runmodus                            default: BTaggingFlags.Runmodus
    taggerNameBase                      default: "MultiSVbb2"
    SecVxFinderName                     default: "MSV"

    input:             name: The name of the tool (should be unique).
      useBTagFlagsDefaults : Whether to use BTaggingFlags defaults for options that are not specified.
                  **options: Python dictionary with options for the tool.
    output: The actual tool, which can then by added to ToolSvc via ToolSvc += output."""
    if useBTagFlagsDefaults:
        defaults = { 'OutputLevel'                      : BTaggingFlags.OutputLevel,
                     'Runmodus'                         : BTaggingFlags.Runmodus,
                     'taggerNameBase'                   : 'MultiSVbb2',
                     'SecVxFinderName'                  : 'MSV' }
        for option in defaults:
            options.setdefault(option, defaults[option])
    options['name'] = name
    from JetTagTools.JetTagToolsConf import Analysis__MultiSVTag
    return Analysis__MultiSVTag(**options)

