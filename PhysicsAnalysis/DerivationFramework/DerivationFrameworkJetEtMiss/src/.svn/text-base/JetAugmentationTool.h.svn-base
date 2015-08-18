///////////////////////////////////////////////////////////////////
// JetAugmentationTool.h, (c) ATLAS Detector software
///////////////////////////////////////////////////////////////////

#ifndef DERIVATIONFRAMEWORK_JETAUGMENTATIONTOOL_H
#define DERIVATIONFRAMEWORK_JETAUGMENTATIONTOOL_H

#include <string>

#include "AthenaBaseComps/AthAlgTool.h"
#include "DerivationFrameworkInterfaces/IAugmentationTool.h"
#include "GaudiKernel/ToolHandle.h"

#include "JetInterface/IJetModifier.h"
#include "xAODJet/JetContainer.h"

namespace DerivationFramework {

  class JetAugmentationTool : public AthAlgTool, public IAugmentationTool {
  public: 
    JetAugmentationTool(const std::string& t, const std::string& n, const IInterface* p);

    StatusCode initialize();
    StatusCode finalize();
    virtual StatusCode addBranches() const;

  private:
    std::string m_momentPrefix;
    std::string m_containerName;
    //
    // implement augmentations explicitly to avoid need to parse lists of moments to copy
    //
    // calibration
    SG::AuxElement::Decorator<float>* dec_calibpt;
    SG::AuxElement::Decorator<float>* dec_calibeta;
    SG::AuxElement::Decorator<float>* dec_calibphi;
    SG::AuxElement::Decorator<float>* dec_calibm;
    ToolHandle<IJetModifier> m_jetCalibTool;
    std::string m_calibMomentKey;
    bool m_docalib;
  }; 
}

#endif // DERIVATIONFRAMEWORK_JETAUGMENTATIONTOOL_H
