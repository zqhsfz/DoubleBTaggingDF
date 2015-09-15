# Configuration functions for ExKtbbTag
# Author: Qi Zeng (2015)

from BTagging.BTaggingFlags import BTaggingFlags

metaExKtbbTag     = { 'IsATagger'         : True,
                      'xAODBaseName'      : 'ExKtbb',
                      'DependsOn'         : ['MV2c20Tag'],
                      'CalibrationFolders' :[],  # ['ExKtbbTag',],
                      'PassByPointer'     : {},  # {'calibrationTool' : 'BTagCalibrationBrokerTool'},
                      'ToolCollection'    : 'ExKtbbTag',
                    }

def toolExKtbbTag(name, useBTagFlagsDefaults = True, **options):
    """Sets up a ExKtbbTag tool and returns it.

    The following options have BTaggingFlags defaults:

    see below

    input:             name: The name of the tool (should be unique).
      useBTagFlagsDefaults : Whether to use BTaggingFlags defaults for options that are not specified.
                  **options: Python dictionary with options for the tool.
    output: The actual tool, which can then by added to ToolSvc via ToolSvc += output."""
    if useBTagFlagsDefaults:
        defaults = { 'OutputLevel'                      : BTaggingFlags.OutputLevel,
                     'Runmodus'                         : BTaggingFlags.Runmodus,
                     'tagMode'                          : 'H->bb',
                     'taggerName'                       : 'ExKtbb',
                     'taggerNameBase'                   : 'ExKtbb',
                     'debug'                            : False,

                     'SubJetLabel'                      : 'ExKt2SubJets',
                     'JFOnlyVtx'                        : False,
                   }
        for option in defaults:
            options.setdefault(option, defaults[option])
    options['name'] = name
    from JetTagTools.JetTagToolsConf import Analysis__ExKtbbTag
    return Analysis__ExKtbbTag(**options)

