///////////////////////////////////////////////////////////////////
// JetAugmentationTool.cxx, (c) ATLAS Detector software
///////////////////////////////////////////////////////////////////
// Author: Teng Jian Khoo (teng.jian.khoo@cern.ch)
//

#include "JetAugmentationTool.h"
#include "xAODCore/ShallowCopy.h"

namespace DerivationFramework {

  JetAugmentationTool::JetAugmentationTool(const std::string& t,
      const std::string& n,
      const IInterface* p) : 
    AthAlgTool(t,n,p),
    m_jetCalibTool(""),
    m_docalib(false)
  {
    declareInterface<DerivationFramework::IAugmentationTool>(this);
    declareProperty("MomentPrefix",   m_momentPrefix = "DFCommonJets_");
    declareProperty("InputJets",      m_containerName = "AntiKt4EMTopoJets");
    // declareProperty("CalibScale",     m_calibScale = "JetGSCScaleMomentum");
    declareProperty("CalibMomentKey", m_calibMomentKey = "Calib");
    declareProperty("JetCalibTool",   m_jetCalibTool);
  }

  StatusCode JetAugmentationTool::initialize()
  {
    if(!m_jetCalibTool.empty()) {
      CHECK(m_jetCalibTool.retrieve());
      ATH_MSG_INFO("Augmenting jets with calibration \"" << m_momentPrefix+m_calibMomentKey << "\"");
      m_docalib = true;

      dec_calibpt  = new SG::AuxElement::Decorator<float> (m_momentPrefix+m_calibMomentKey+"_pt");
      dec_calibeta = new SG::AuxElement::Decorator<float> (m_momentPrefix+m_calibMomentKey+"_eta");
      dec_calibphi = new SG::AuxElement::Decorator<float> (m_momentPrefix+m_calibMomentKey+"_phi");
      dec_calibm   = new SG::AuxElement::Decorator<float> (m_momentPrefix+m_calibMomentKey+"_m");
    }
    return StatusCode::SUCCESS;
  }
    
  StatusCode JetAugmentationTool::finalize()
  {

    if(!m_jetCalibTool.empty()) {
      delete dec_calibpt;
      delete dec_calibeta;
      delete dec_calibphi;
      delete dec_calibm;
    }
    return StatusCode::SUCCESS;
  }

  StatusCode JetAugmentationTool::addBranches() const
  {
    // retrieve container
    const xAOD::JetContainer* jets(0);
    if( evtStore()->retrieve( jets, m_containerName ).isFailure() ) {
      ATH_MSG_WARNING ("Couldn't retrieve jets with key: " << m_containerName );
      return StatusCode::FAILURE;
    }

    // make a shallow copy of the jets
    std::pair<xAOD::JetContainer*,xAOD::ShallowAuxContainer*> shallowcopy = xAOD::shallowCopyContainer(*jets);
    std::unique_ptr<xAOD::JetContainer> jets_copy(shallowcopy.first);
    std::unique_ptr<xAOD::ShallowAuxContainer> jets_copyaux(shallowcopy.second);

      // if we have a calibration tool, apply the calibration
    if(m_docalib) {
      if(m_jetCalibTool->modify(*jets_copy) ) {
	ATH_MSG_WARNING("Problem applying jet calibration");
	return StatusCode::FAILURE;
      }
    }

    // loop over the copies
    for(const auto& jet : *jets_copy) {
      // get the original jet so we can decorate it
      const xAOD::Jet& jet_orig( *(*jets)[jet->index()] );

      if(m_docalib) {
	// generate static decorators to avoid multiple lookups	
	(*dec_calibpt)(jet_orig)  = jet->pt();
	(*dec_calibeta)(jet_orig) = jet->eta();
	(*dec_calibphi)(jet_orig) = jet->phi();
	(*dec_calibm)(jet_orig)   = jet->m();
      }
    }
    
    return StatusCode::SUCCESS;
  }
}
