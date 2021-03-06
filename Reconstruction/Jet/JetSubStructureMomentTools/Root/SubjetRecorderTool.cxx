#include <iostream>
#include <math.h>
#include <float.h>
#include "JetSubStructureMomentTools/SubjetRecorderTool.h"
#include "fastjet/PseudoJet.hh"
#include "xAODJet/JetContainer.h"
#include "xAODJet/JetAuxContainer.h"
#include "JetEDM/JetConstituentFiller.h"

using namespace std;
using fastjet::PseudoJet;

SubjetRecorderTool::SubjetRecorderTool(std::string name) : 
  AsgTool(name), m_subjetlabel(""), m_subjetcontainername(""), m_subjetalg(""), m_subjetrad(0.), m_subjetParentLink(false)
{
  declareProperty("SubjetLabel", m_subjetlabel);
  declareProperty("SubjetContainerName", m_subjetcontainername);
  declareProperty("SubjetAlgorithm_BTAG", m_subjetalg);
  declareProperty("SubjetRadius_BTAG", m_subjetrad);
  declareProperty("SubjetParentLink_BTAG", m_subjetParentLink);
}

std::vector<xAOD::Jet *> SubjetRecorderTool::recordSubjets(std::vector<fastjet::PseudoJet> subjets, xAOD::Jet &jet) const
{
  // Retrieve or set up subjet container
  string subjet_name = m_subjetlabel;
  string subjet_container_name = m_subjetcontainername;
  if(subjet_name == "" || subjet_container_name == "") {
    ATH_MSG_ERROR("Invalid subjet label or container name");
    return vector<xAOD::Jet *>();
  }
  xAOD::JetContainer *subjet_container = 0;
#ifdef ROOTCORE
  subjet_container = evtStore()->retrieve<xAOD::JetContainer>(subjet_container_name);
#else
  // Need tryRetrieve to supress some Athena warning. Unfortuantely tryRetrieve isn't in RootCore
  subjet_container = evtStore()->tryRetrieve<xAOD::JetContainer>(subjet_container_name);
#endif
  if(subjet_container == 0) {
    StatusCode sc;
    subjet_container = new xAOD::JetContainer;
    subjet_container->setStore(new xAOD::JetAuxContainer);
    sc = evtStore()->record(subjet_container, subjet_container_name);
    if(sc.isFailure()) {
      ATH_MSG_ERROR("Error recording subjet container (" << subjet_container_name << ")");
      return vector<xAOD::Jet *>();
    }
    sc = evtStore()->record(dynamic_cast<xAOD::JetAuxContainer*>(subjet_container->getStore()), subjet_container_name + "Aux.");
    if(sc.isFailure()) {
      ATH_MSG_ERROR("Error recording subjet aux container (" << subjet_container_name << "Aux.)");
      return vector<xAOD::Jet *>();
    }
  }

  // Create xAOD::Jet's
  vector<const xAOD::Jet *> subj_ptrs_const;
  vector<xAOD::Jet *> subj_ptrs;
  for(auto it = subjets.begin(); it != subjets.end(); it++) {
    xAOD::Jet *subj = new xAOD::Jet();
    subjet_container->push_back(subj);
    subj_ptrs.push_back(subj);
    subj_ptrs_const.push_back(subj);
    
    // Set 4-mom
    subj->setJetP4(xAOD::JetFourMom_t(it->pt(), it->eta(), it->phi(), it->m()));
    subj->setJetP4(xAOD::JetConstitScaleMomentum, subj->jetP4());

    // Set constituents
    jet::JetConstituentFiller confiller;
    confiller.extractConstituents(*subj, &(*it));

    // Set association to parent
    if(m_subjetParentLink){
      const xAOD::JetContainer *parent_container = dynamic_cast<const xAOD::JetContainer*>(jet.container());
      ElementLink<xAOD::JetContainer> el_parent(*parent_container, jet.index());
      subj->setAttribute("Parent", el_parent);
    }

    // additional information (partially) for b-tagging purpose
    xAOD::JetAlgorithmType::ID ialg = xAOD::JetAlgorithmType::algId(m_subjetalg);
    subj->setAlgorithmType(ialg);
    subj->setSizeParameter(m_subjetrad);
    subj->setInputType(jet.getInputType());
    subj->setConstituentsSignalState(jet.getConstituentsSignalState());
  }
  
  // Set association to subjets
  jet.setAssociatedObjects(subjet_name, subj_ptrs_const);

  return subj_ptrs;
}
