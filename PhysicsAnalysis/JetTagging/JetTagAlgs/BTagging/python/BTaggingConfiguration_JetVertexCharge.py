# Configuration functions for JetVertexCharge
# Author: Wouter van den Wollenberg (2013-2014)
from BTagging.BTaggingFlags import BTaggingFlags

metaJetVertexCharge = { 'IsATagger'           : True,
                       'NeedsMuonAssociator'  : True,
                       'DependsOn'            : ['AtlasExtrapolator',
                                                 'BTagTrackToVertexTool',
#                                               'NewJetFitterVxFinder',
                                                 'BTagCalibrationBrokerTool',
                                                 ],
                        'CalibrationFolders'  : ['JetVertexCharge',], 
                        'PassByPointer'       : {'calibrationTool' : 'BTagCalibrationBrokerTool'},
#                        'PassByName'        : {'SecVxFinderName' : 'NewJetFitterVxFinder'}, 
#                        'JetCollectionList' : 'jetCollectionList',
                        'ToolCollection'      : 'JetVertexCharge' }

def toolJetVertexCharge(name, useBTagFlagsDefaults = True, **options):
    """Sets up a JetVertexCharge tool and returns it.

    The following options have BTaggingFlags defaults:

    OutputLevel                         default: BTaggingFlags.OutputLevel
    Runmodus                            default: BTaggingFlags.Runmodus
    jetCollectionList                   default: BTaggingFlags.Jets
    taggerNameBase                      default: "JetVertexCharge"

    input:             name: The name of the tool (should be unique).
      useBTagFlagsDefaults : Whether to use BTaggingFlags defaults for options that are not specified.
                  **options: Python dictionary with options for the tool.
    output: The actual tool, which can then by added to ToolSvc via ToolSvc += output."""
    if useBTagFlagsDefaults:
        defaults = { 'OutputLevel'                      : BTaggingFlags.OutputLevel,
                     'Runmodus'                         : BTaggingFlags.Runmodus,
                     'jetCollectionList'                : BTaggingFlags.Jets,
#                     'SecVxFinderName'                  : 'NewJetFitterVxFinder',
                     'taggerNameBase'                   : 'JetVertexCharge',
                    }
        if(BTaggingFlags.Runmodus == 'reference'): 
            defaults['BTagJetEtamin'] = 2.5  
        for option in defaults:
            options.setdefault(option, defaults[option])
    options['name'] = name
    from JetTagTools.JetTagToolsConf import Analysis__JetVertexCharge
    return Analysis__JetVertexCharge(**options)

