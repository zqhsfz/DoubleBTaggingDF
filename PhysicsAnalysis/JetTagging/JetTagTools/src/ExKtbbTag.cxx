#include "JetTagTools/ExKtbbTag.h"

#include "GaudiKernel/IToolSvc.h"
#include "JetTagTools/JetTagUtils.h"     // get jet author
#include "PathResolver/PathResolver.h"   // to get the correct path of local calib file
#include "xAODBTagging/SecVtxHelper.h"   // extract SV information
#include "xAODTracking/TrackParticleContainer.h"

#include <algorithm>
#include "TVector3.h"
#include "TMath.h"


namespace Analysis {

/** 
    @class ExKtbbTag 
    Identification of double b-hadron jets ( g->bb or H->bb jets) through exclusive kt subjet b-tagging
    @author Qi. Zeng
*/

ExKtbbTag::ExKtbbTag(const std::string& t, const std::string& n, const IInterface* p)
  : AthAlgTool(t,n,p),
    m_runModus("analysis"),
    m_tagMode("H->bb"),
    m_taggerName("ExKtbb"),
    m_taggerNameBase("ExKtbb"),
    m_xAODBaseName("ExKtbb"),
    m_debug(false),
    m_SubJetLabel("ExKt2SubJets"),
    m_JFOnlyVtx(false)
{
  declareInterface<ITagTool>(this);

  // global configuration
  declareProperty("Runmodus",                 m_runModus);
  declareProperty("tagMode",                  m_tagMode);
  declareProperty("taggerName",               m_taggerName);
  declareProperty("taggerNameBase",           m_taggerNameBase);
  declareProperty("xAODBaseName",             m_xAODBaseName);
  declareProperty("debug",                    m_debug);

  // variables for tagger
  declareProperty("SubJetLabel",              m_SubJetLabel);
  declareProperty("JFOnlyVtx",                m_JFOnlyVtx);
}


ExKtbbTag::~ExKtbbTag() {
  // empty for now //
}


StatusCode ExKtbbTag::initialize() {

  // empty for now //

  return StatusCode::SUCCESS;
}


StatusCode ExKtbbTag::finalize() {
  
  // empty for now //
  
  return StatusCode::SUCCESS;
}

StatusCode ExKtbbTag::tagJet(xAOD::Jet& jetToTag, xAOD::BTagging* BTag) {
  
  if(!CalculateInputVariables(jetToTag, BTag)){
    ATH_MSG_ERROR("Error in CalculateInputVariables()!");
    return StatusCode::FAILURE;
  }

  if(m_runModus == "reference"){
    if(!JetTagReferenceMode(jetToTag, BTag)){
      ATH_MSG_ERROR("Error in JetTagReferenceMode()!");
      return StatusCode::FAILURE;
    }
  }
  else if(m_runModus == "analysis"){
    if(!JetTagAnalysisMode(jetToTag, BTag)){
      ATH_MSG_ERROR("Error in JetTagAnalysisMode()!");
      return StatusCode::FAILURE;
    }
  }
  else{
    ATH_MSG_ERROR("Unidentified run mode: " << m_runModus.c_str());
    return StatusCode::FAILURE;
  }

  return StatusCode::SUCCESS;
}

///////////////////////////////////////////////////////////////////////////////////////////////

bool ExKtbbTag::CalculateInputVariables(xAOD::Jet& jetToTag, xAOD::BTagging* BTag){
  if(m_debug) ATH_MSG_INFO("Entering CalculateInputVariables");

  // Initialization
  BTag->setVariable<double>(m_taggerNameBase, "DoubleMV2c20", -1.1);
  
  BTag->setVariable<int>(m_taggerNameBase, "SV1NtrksDiff", -20);
  BTag->setVariable<int>(m_taggerNameBase, "JFNtrksDiff", -20);
  
  BTag->setVariable<double>(m_taggerNameBase, "SV1CombMass", -1.);
  BTag->setVariable<double>(m_taggerNameBase, "JFCombMass", -1.);

  BTag->setVariable<double>(m_taggerNameBase, "SV1DR", -1.);
  BTag->setVariable<double>(m_taggerNameBase, "SV1DRError", -1.);
  BTag->setVariable<double>(m_taggerNameBase, "SV1DRSignificance", -1.);

  BTag->setVariable<double>(m_taggerNameBase, "JFDR", -1.);
  BTag->setVariable<double>(m_taggerNameBase, "JFDRError", -1.);
  BTag->setVariable<double>(m_taggerNameBase, "JFDRSignificance", -1.);

  BTag->setVariable<double>(m_taggerNameBase, "SV1DR3D", -1.);
  BTag->setVariable<double>(m_taggerNameBase, "SV1DR3DError", -1.);
  BTag->setVariable<double>(m_taggerNameBase, "SV1DR3DSignificance", -1.);

  BTag->setVariable<double>(m_taggerNameBase, "SV1DL", -1.);
  BTag->setVariable<double>(m_taggerNameBase, "SV1DLError", -1.);
  BTag->setVariable<double>(m_taggerNameBase, "SV1DLSignificance", -1.);

  BTag->setVariable<double>(m_taggerNameBase, "JFDL", -1.);
  BTag->setVariable<double>(m_taggerNameBase, "JFDLError", -1.);
  BTag->setVariable<double>(m_taggerNameBase, "JFDLSignificance", -1.);

  // fetch subjets and sort by pT
  std::vector<const xAOD::Jet*> ExKtSubJets;
  if(!jetToTag.getAssociatedObjects<xAOD::Jet>(m_SubJetLabel.c_str(), ExKtSubJets)){
    ATH_MSG_ERROR("Unable to fetch subjet collection " << m_SubJetLabel.c_str());
    return false;
  }
  std::sort(ExKtSubJets.begin(), ExKtSubJets.end(), ExKtbbTag::SortPt);

  // validity check
  if(ExKtSubJets.size() == 2){
    const xAOD::BTagging* bjet_LeadExKtSubJet = ExKtSubJets[0]->btagging();
    const xAOD::BTagging* bjet_SubLeadExKtSubJet = ExKtSubJets[1]->btagging();

    if( (!bjet_LeadExKtSubJet) || (!bjet_SubLeadExKtSubJet) ){
      ATH_MSG_ERROR("Exclusive kt subjet is not well b-tagged!");
      return false;
    }

    BTag->setVariable<double>(m_taggerNameBase, "DoubleMV2c20", GetDoubleMV2c20(bjet_LeadExKtSubJet, bjet_SubLeadExKtSubJet));
  
    BTag->setVariable<int>(m_taggerNameBase, "SV1NtrksDiff", GetSV1NtrksDiff(BTag, bjet_LeadExKtSubJet, bjet_SubLeadExKtSubJet, true));
    BTag->setVariable<int>(m_taggerNameBase, "JFNtrksDiff", GetJFNtrksDiff(BTag, bjet_LeadExKtSubJet, bjet_SubLeadExKtSubJet, true, m_JFOnlyVtx));
    
    BTag->setVariable<double>(m_taggerNameBase, "SV1CombMass", GetSV1CombMass(bjet_LeadExKtSubJet, bjet_SubLeadExKtSubJet, true));
    BTag->setVariable<double>(m_taggerNameBase, "JFCombMass", GetJFCombMass(bjet_LeadExKtSubJet, bjet_SubLeadExKtSubJet, true, m_JFOnlyVtx, true));

    double SV1DR, SV1DRError;
    BTag->setVariable<double>(m_taggerNameBase, "SV1DRSignificance", GetSV1DRSignificance(bjet_LeadExKtSubJet, bjet_SubLeadExKtSubJet, SV1DR, SV1DRError));
    BTag->setVariable<double>(m_taggerNameBase, "SV1DR", SV1DR);
    BTag->setVariable<double>(m_taggerNameBase, "SV1DRError", SV1DRError);

    double JFDR, JFDRError;
    BTag->setVariable<double>(m_taggerNameBase, "JFDRSignificance", GetJFDRSignificance(bjet_LeadExKtSubJet, bjet_SubLeadExKtSubJet, m_JFOnlyVtx, JFDR, JFDRError));
    BTag->setVariable<double>(m_taggerNameBase, "JFDR", JFDR);
    BTag->setVariable<double>(m_taggerNameBase, "JFDRError", JFDRError);

    double SV1DR3D, SV1DR3DError;
    BTag->setVariable<double>(m_taggerNameBase, "SV1DR3DSignificance", GetSV1DR3DSignificance(bjet_LeadExKtSubJet, bjet_SubLeadExKtSubJet, SV1DR3D, SV1DR3DError));
    BTag->setVariable<double>(m_taggerNameBase, "SV1DR3D", SV1DR3D);
    BTag->setVariable<double>(m_taggerNameBase, "SV1DR3DError", SV1DR3DError);

    double SV1DL, SV1DLError;
    BTag->setVariable<double>(m_taggerNameBase, "SV1DLSignificance", GetSV1DLSignificance(bjet_LeadExKtSubJet, bjet_SubLeadExKtSubJet, SV1DL, SV1DLError));
    BTag->setVariable<double>(m_taggerNameBase, "SV1DL", SV1DL);
    BTag->setVariable<double>(m_taggerNameBase, "SV1DLError", SV1DLError);

    double JFDL, JFDLError;
    BTag->setVariable<double>(m_taggerNameBase, "JFDLSignificance", GetJFDLSignificance(bjet_LeadExKtSubJet, bjet_SubLeadExKtSubJet, m_JFOnlyVtx, JFDL, JFDLError));
    BTag->setVariable<double>(m_taggerNameBase, "JFDL", JFDL);
    BTag->setVariable<double>(m_taggerNameBase, "JFDLError", JFDLError);
  }
  else if(ExKtSubJets.size() == 3){
    ATH_MSG_WARNING("Exclusive kt with N=3 is not supported yet! Jet will be skipped");
    return true;
  }
  else{
    ATH_MSG_WARNING("Unable to process Exclusive kt with N=" << ExKtSubJets.size() <<". Jet will be skipped");
    return true;
  }


  if(m_debug) ATH_MSG_INFO("Leaving CalculateInputVariables");

  return true;
}

bool ExKtbbTag::JetTagAnalysisMode(xAOD::Jet& jetToTag, xAOD::BTagging* BTag){
  if(m_debug) ATH_MSG_INFO("Entering JetTagAnalysisMode");

  // emtpy // 

  if(m_debug) ATH_MSG_INFO("Leaving JetTagAnalysisMode");

  return true;
}

bool ExKtbbTag::JetTagReferenceMode(xAOD::Jet& jetToTag, xAOD::BTagging* BTag){
  if(m_debug) ATH_MSG_INFO("Entering JetTagReferenceMode");

  // empty // 

  if(m_debug) ATH_MSG_INFO("Leaving JetTagReferenceMode");

  return true;
}

//////////////////////////////////////////////////////////////////////////////////////////////////////

double ExKtbbTag::GetDoubleMV2c20(const xAOD::BTagging* bjet1, const xAOD::BTagging* bjet2){
  double FirstMV2c20 = bjet1->auxdata<double>("MV2c20_discriminant");
  double SecondMV2c20 = bjet2->auxdata<double>("MV2c20_discriminant");

  return std::min(FirstMV2c20, SecondMV2c20);  
}

int ExKtbbTag::GetSV1NtrksDiff(const xAOD::BTagging* bjet, const xAOD::BTagging* bjet1, const xAOD::BTagging* bjet2, bool doValidDualSV1){
  auto SV1vertices_bjet = GetSV1vertices(bjet);
  auto SV1vertices_bjet1 = GetSV1vertices(bjet1);
  auto SV1vertices_bjet2 = GetSV1vertices(bjet2);

  bool isValidDualSV1 = SV1DualValid(SV1vertices_bjet1, SV1vertices_bjet2);

  if( (doValidDualSV1) && (!isValidDualSV1) ) return -20;

  return (IsValidSV1(SV1vertices_bjet1) ? SV1vertices_bjet1[0]->nTrackParticles() : 0) + (IsValidSV1(SV1vertices_bjet2) ? SV1vertices_bjet2[0]->nTrackParticles() : 0) - (IsValidSV1(SV1vertices_bjet) ? SV1vertices_bjet[0]->nTrackParticles() : 0);
}

int ExKtbbTag::GetJFNtrksDiff(const xAOD::BTagging* bjet, const xAOD::BTagging* bjet1, const xAOD::BTagging* bjet2, bool doValidDualJF, bool onlyVtx){
  bool isValidDualJF = JFDualValid(bjet1, bjet2, onlyVtx);

  if( (doValidDualJF) && (!isValidDualJF) ) return -20;

  return IsValidJF(bjet1, onlyVtx) * JFntrk(bjet1, onlyVtx) + IsValidJF(bjet2, onlyVtx) * JFntrk(bjet2, onlyVtx) - IsValidJF(bjet, onlyVtx) * JFntrk(bjet, onlyVtx);
}

double ExKtbbTag::GetSV1CombMass(const xAOD::BTagging* bjet1, const xAOD::BTagging* bjet2, bool doValidDualSV1){
  auto SV1vertices_bjet1 = GetSV1vertices(bjet1);
  auto SV1vertices_bjet2 = GetSV1vertices(bjet2);

  bool isValidDualSV1 = SV1DualValid(SV1vertices_bjet1, SV1vertices_bjet2);

  if( (doValidDualSV1) && (!isValidDualSV1) ) return -1.;

  std::vector<ElementLink<xAOD::TrackParticleContainer> > SV1Tracks_bjet1 = bjet1->SV1_TrackParticleLinks();
  std::vector<ElementLink<xAOD::TrackParticleContainer> > SV1Tracks_bjet2 = bjet2->SV1_TrackParticleLinks();

  std::vector<ElementLink<xAOD::TrackParticleContainer> > SV1Tracks_Comb = SV1Tracks_bjet1;
  SV1Tracks_Comb.insert(SV1Tracks_Comb.end(), SV1Tracks_bjet2.begin(), SV1Tracks_bjet2.end());

  TLorentzVector SumSV1TracksP4;
  for(auto el_track : SV1Tracks_Comb){
    if(!el_track.isValid()){
      ATH_MSG_WARNING("Invalid element link to SV1_TrackParticles. It will be skipped");
      continue;
    }

    if(*el_track == 0){
      ATH_MSG_WARNING("Null ptr returned for SV1_TrackParticles. It will be skipped");
      continue;
    }

    SumSV1TracksP4 += ((*el_track)->p4());
  }

  return SumSV1TracksP4.M()/1000.;    // MeV->GeV
}

double ExKtbbTag::GetJFCombMass(const xAOD::BTagging* bjet1, const xAOD::BTagging* bjet2, bool doValidDualJF, bool onlyVtx, bool doNeutralCorrection){
  bool isValidDualJF = JFDualValid(bjet1, bjet2, onlyVtx);

  if( (doValidDualJF) && (!isValidDualJF) ) return -1.;

  TLorentzVector SumP4 = JFMomentum(bjet1, onlyVtx, doNeutralCorrection) + JFMomentum(bjet2, onlyVtx, doNeutralCorrection);
  return SumP4.M()/1000.;    // MeV->GeV
}

double ExKtbbTag::GetSV1DRSignificance(const xAOD::BTagging* bjet1, const xAOD::BTagging* bjet2, double& DR, double& DR_error){
  DR = -1.;
  DR_error = -1.;

  auto SV1vertices_bjet1 = GetSV1vertices(bjet1);
  auto SV1vertices_bjet2 = GetSV1vertices(bjet2);

  if(!SV1DualValid(SV1vertices_bjet1, SV1vertices_bjet2)) return -1.;

  auto FirstSV1 = SV1vertices_bjet1[0];
  auto SecondSV1 = SV1vertices_bjet2[0];

  // calculate DR
  auto function_SV1DR = [](Amg::Vector3D vtx1, Amg::Vector3D vtx2, Amg::Vector3D PV)->double{
    TVector3 vtx1_pv(vtx1(0) - PV(0), vtx1(1) - PV(1), vtx1(2) - PV(2));
    TVector3 vtx2_pv(vtx2(0) - PV(0), vtx2(1) - PV(1), vtx2(2) - PV(2));

    return vtx1_pv.DeltaR(vtx2_pv);
  };

  DR = function_SV1DR(FirstSV1->position(), SecondSV1->position(), m_priVtx->position());

  // calculate error on DR
  auto FirstSV1_variations  = GetVtxEigenVariation(FirstSV1->position(), FirstSV1->covariancePosition());
  auto SecondSV1_variations = GetVtxEigenVariation(SecondSV1->position(), SecondSV1->covariancePosition());
  auto PV_variations = GetVtxEigenVariation(m_priVtx->position(), m_priVtx->covariancePosition());

  double sumerror2_FirstSV1 = 0.;
  double sumerror2_SecondSV1 = 0.;
  double sumerror2_PV = 0.;
  for(unsigned int index = 0; index < 3; index++){
    double error_FirstSV1 = std::max( fabs(function_SV1DR(FirstSV1_variations[2*index], SecondSV1->position(), m_priVtx->position()) - DR), fabs(function_SV1DR(FirstSV1_variations[2*index+1], SecondSV1->position(), m_priVtx->position()) - DR) );
    sumerror2_FirstSV1 += (error_FirstSV1 * error_FirstSV1);

    double error_SecondSV1 = std::max( fabs(function_SV1DR(FirstSV1->position(), SecondSV1_variations[2*index], m_priVtx->position()) - DR), fabs(function_SV1DR(FirstSV1->position(), SecondSV1_variations[2*index+1], m_priVtx->position()) - DR) );
    sumerror2_SecondSV1 += (error_SecondSV1 * error_SecondSV1);

    double error_PV = std::max( fabs(function_SV1DR(FirstSV1->position(), SecondSV1->position(), PV_variations[2*index]) - DR), fabs(function_SV1DR(FirstSV1->position(), SecondSV1->position(), PV_variations[2*index+1]) - DR) );
    sumerror2_PV += (error_PV * error_PV);
  }

  DR_error = TMath::Sqrt(sumerror2_FirstSV1 + sumerror2_SecondSV1 + sumerror2_PV);

  double output = 0.;
  if(DR_error == 0.){
    ATH_MSG_WARNING("Zero error obtained in GetSV1DRSignificance, which is very unlikely");
    output = 999.;
  }
  else{
    output = DR/DR_error;
  }

  return LimitUpperBound(output, 50, 100);
}

double ExKtbbTag::GetJFDRSignificance(const xAOD::BTagging* bjet1, const xAOD::BTagging* bjet2, bool onlyVtx, double& DR, double& DR_error){
  DR = -1.;
  DR_error = -1.;

  if(!JFDualValid(bjet1, bjet2, onlyVtx)) return -1.;

  std::vector<float> fittedPosition_bjet1;
  std::vector<float> fittedCov_bjet1;
  fittedPosition_bjet1 = GetJFfittedPosition(bjet1, fittedCov_bjet1);

  std::vector<float> fittedPosition_bjet2;
  std::vector<float> fittedCov_bjet2;
  fittedPosition_bjet2 = GetJFfittedPosition(bjet2, fittedCov_bjet2);

  // get DR
  auto function_JFAxis3D = [](double theta, double phi)->TVector3{
    TVector3 axis;
    axis.SetMagThetaPhi(1., theta, phi);
    return axis;
  };

  auto function_JFDR = [](TVector3 axis1, TVector3 axis2)->double{
    return axis1.DeltaR(axis2);
  };

  double theta_bjet1 = fittedPosition_bjet1[4];
  double phi_bjet1 = fittedPosition_bjet1[3];
  double theta_bjet2 = fittedPosition_bjet2[4];
  double phi_bjet2 = fittedPosition_bjet2[3];
  DR = function_JFDR(function_JFAxis3D(theta_bjet1, phi_bjet1), function_JFAxis3D(theta_bjet2, phi_bjet2));

  // get error
  double Error_theta_bjet1 = std::max( fabs(function_JFDR(function_JFAxis3D(theta_bjet1 + TMath::Sqrt(fittedCov_bjet1[4]), phi_bjet1), function_JFAxis3D(theta_bjet2, phi_bjet2)) - DR),  fabs(function_JFDR(function_JFAxis3D(theta_bjet1 - TMath::Sqrt(fittedCov_bjet1[4]), phi_bjet1), function_JFAxis3D(theta_bjet2, phi_bjet2)) - DR) );
  double Error_phi_bjet1 = std::max( fabs(function_JFDR(function_JFAxis3D(theta_bjet1, phi_bjet1 + TMath::Sqrt(fittedCov_bjet1[3])), function_JFAxis3D(theta_bjet2, phi_bjet2)) - DR),  fabs(function_JFDR(function_JFAxis3D(theta_bjet1, phi_bjet1 - TMath::Sqrt(fittedCov_bjet1[3])), function_JFAxis3D(theta_bjet2, phi_bjet2)) - DR) );
  double Error_theta_bjet2 = std::max( fabs(function_JFDR(function_JFAxis3D(theta_bjet1, phi_bjet1), function_JFAxis3D(theta_bjet2 + TMath::Sqrt(fittedCov_bjet2[4]), phi_bjet2)) - DR),  fabs(function_JFDR(function_JFAxis3D(theta_bjet1, phi_bjet1), function_JFAxis3D(theta_bjet2 - TMath::Sqrt(fittedCov_bjet2[4]), phi_bjet2)) - DR) );
  double Error_phi_bjet2 = std::max( fabs(function_JFDR(function_JFAxis3D(theta_bjet1, phi_bjet1), function_JFAxis3D(theta_bjet2, phi_bjet2 + TMath::Sqrt(fittedCov_bjet2[3]))) - DR),  fabs(function_JFDR(function_JFAxis3D(theta_bjet1, phi_bjet1), function_JFAxis3D(theta_bjet2, phi_bjet2 - TMath::Sqrt(fittedCov_bjet2[3]))) - DR) );

  DR_error = TMath::Sqrt( Error_theta_bjet1*Error_theta_bjet1 + Error_phi_bjet1*Error_phi_bjet1 + Error_theta_bjet2*Error_theta_bjet2 + Error_phi_bjet2*Error_phi_bjet2 );

  double output = 0.;
  if(DR_error == 0.){
    ATH_MSG_WARNING("Zero error obtained in GetJFDRSignificance, which is very unlikely");
    output = 999.;
  }
  else{
    output = DR/DR_error;
  }

  return LimitUpperBound(output, 50, 100);
}

double ExKtbbTag::GetSV1DR3DSignificance(const xAOD::BTagging* bjet1, const xAOD::BTagging* bjet2, double& dR3D, double& dR3D_error){
  dR3D = -1.;
  dR3D_error = -1;

  auto SV1vertices_bjet1 = GetSV1vertices(bjet1);
  auto SV1vertices_bjet2 = GetSV1vertices(bjet2);

  if(!SV1DualValid(SV1vertices_bjet1, SV1vertices_bjet2)) return -1.;

  auto FirstSV1 = SV1vertices_bjet1[0];
  auto SecondSV1 = SV1vertices_bjet2[0];

  return GeneralDRSignificance3D(FirstSV1->position(), FirstSV1->covariancePosition(), SecondSV1->position(), SecondSV1->covariancePosition(), dR3D, dR3D_error);
}

double ExKtbbTag::GetSV1DLSignificance(const xAOD::BTagging* bjet1, const xAOD::BTagging* bjet2, double& dL, double& dL_error){
  dL = -1.;
  dL_error = -1.;

  auto SV1vertices_bjet1 = GetSV1vertices(bjet1);
  auto SV1vertices_bjet2 = GetSV1vertices(bjet2);

  if(!SV1DualValid(SV1vertices_bjet1, SV1vertices_bjet2)) return -1.;

  auto FirstSV1 = SV1vertices_bjet1[0];
  auto SecondSV1 = SV1vertices_bjet2[0];

  // calculate dL
  auto function_GetDL = [](Amg::Vector3D vtx1, Amg::Vector3D vtx2, Amg::Vector3D pv)->double{
    double l1 = TMath::Sqrt((vtx1 - pv).dot(vtx1 - pv));
    double l2 = TMath::Sqrt((vtx2 - pv).dot(vtx2 - pv));

    return fabs(l1-l2);
  };

  dL = function_GetDL(FirstSV1->position(), SecondSV1->position(), m_priVtx->position());

  // Calculate Error
  std::vector<Amg::Vector3D> FirstSV1_variations = GetVtxEigenVariation(FirstSV1->position(), FirstSV1->covariancePosition());
  std::vector<Amg::Vector3D> SecondSV1_variations = GetVtxEigenVariation(SecondSV1->position(), SecondSV1->covariancePosition());
  std::vector<Amg::Vector3D> PV_variations = GetVtxEigenVariation(m_priVtx->position(), m_priVtx->covariancePosition());

  double sumerror2_FirstSV1 = 0.;
  double sumerror2_SecondSV1 = 0.;
  double sumerror2_PV = 0.;

  for(unsigned int index = 0; index < 3; index++){
    double error_FirstSV1 = std::max(fabs(function_GetDL(FirstSV1_variations[2*index], SecondSV1->position(), m_priVtx->position()) - dL), fabs(function_GetDL(FirstSV1_variations[2*index+1], SecondSV1->position(), m_priVtx->position()) - dL));
    sumerror2_FirstSV1 += (error_FirstSV1 * error_FirstSV1);

    double error_SecondSV1 = std::max(fabs(function_GetDL(FirstSV1->position(), SecondSV1_variations[2*index], m_priVtx->position()) - dL), fabs(function_GetDL(FirstSV1->position(), SecondSV1_variations[2*index+1], m_priVtx->position()) - dL));
    sumerror2_SecondSV1 += (error_SecondSV1 * error_SecondSV1);

    double error_PV = std::max(fabs(function_GetDL(FirstSV1->position(), SecondSV1->position(), PV_variations[2*index]) - dL), fabs(function_GetDL(FirstSV1->position(), SecondSV1->position(), PV_variations[2*index+1]) - dL));
    sumerror2_PV += (error_PV * error_PV); 
  }

  dL_error = TMath::Sqrt(sumerror2_FirstSV1 + sumerror2_SecondSV1 + sumerror2_PV);

  double output = 0.;
  if(dL_error == 0.){
    ATH_MSG_WARNING("Zero error obtained in GetSV1DLSignificance, which is very unlikely");
    output = 999.;
  }
  else{
    output = dL/dL_error;
  }

  return LimitUpperBound(output, 50, 100);
}

double ExKtbbTag::GetJFDLSignificance(const xAOD::BTagging* bjet1, const xAOD::BTagging* bjet2, bool onlyVtx, double& dL, double& dL_error){
  dL = -1.;
  dL_error = -1.;

  if(!JFDualValid(bjet1, bjet2, onlyVtx)) return -1.;

  std::vector<float> fittedPosition_bjet1;
  std::vector<float> fittedCov_bjet1;
  fittedPosition_bjet1 = GetJFfittedPosition(bjet1, fittedCov_bjet1);

  std::vector<float> fittedPosition_bjet2;
  std::vector<float> fittedCov_bjet2;
  fittedPosition_bjet2 = GetJFfittedPosition(bjet2, fittedCov_bjet2);

  // get dL
  auto function_GetDL = [](double l1, double l2)->double{
    return fabs(l1-l2);
  };

  double l1,l1_error;
  l1 = JFEffectiveDecayLength(bjet1, onlyVtx, l1_error);

  double l2,l2_error;
  l2 = JFEffectiveDecayLength(bjet2, onlyVtx, l2_error);

  dL = function_GetDL(l1, l2);

  double error_l1 = std::max(fabs(function_GetDL(l1 + l1_error, l2) - dL), fabs(function_GetDL(l1 - l1_error, l2) - dL));
  double error_l2 = std::max(fabs(function_GetDL(l1, l2 + l2_error) - dL), fabs(function_GetDL(l1, l2 - l2_error) - dL));

  dL_error = TMath::Sqrt(error_l1*error_l1 + error_l2*error_l2);

  double output = 0.;
  if(dL_error == 0.){
    ATH_MSG_WARNING("Zero error obtained in GetJFDLSignificance, which is very unlikely");
    output = 999.;
  }
  else{
    output = dL/dL_error;
  }

  return LimitUpperBound(output, 50, 100);
}


/////////////////////////////////////////////////////////////////////////////////////////////////////

std::vector<const xAOD::Vertex*> ExKtbbTag::GetSV1vertices(const xAOD::BTagging* bjet){
  std::vector<ElementLink<xAOD::VertexContainer> > SV1vertices;
  try{
    SV1vertices = bjet->auxdata<std::vector<ElementLink<xAOD::VertexContainer> > >("SV1_vertices");
  }
  catch(...){
    ATH_MSG_WARNING("Unable to get \"SV1_vertices\" from bjet");
  }

  std::vector<const xAOD::Vertex*> output;
  for(auto el_vtx : SV1vertices){
    if(!el_vtx.isValid()){
      ATH_MSG_WARNING("Invalid element link to SV1 vtx. It will be skipped");
      continue;
    }

    const xAOD::Vertex* vtx = (*el_vtx);
    if(vtx == 0){
      ATH_MSG_WARNING("Null ptr returned for SV1 vtx. It will be skipped");
      continue;
    }

    output.push_back(vtx);
  }

  return output;
}

bool ExKtbbTag::IsValidSV1(std::vector<const xAOD::Vertex*> input){
  if(input.size() > 1){
    ATH_MSG_WARNING("Get more than 1 SV1 vtx! Only first one will be used.");
  }

  return input.size() > 0;
}

bool ExKtbbTag::SV1DualValid(std::vector<const xAOD::Vertex*> vtx1, std::vector<const xAOD::Vertex*> vtx2){
  return IsValidSV1(vtx1) && IsValidSV1(vtx2);
}

std::vector<const xAOD::BTagVertex*> ExKtbbTag::GetJFVertices(const xAOD::BTagging* bjet){
  std::vector<ElementLink<xAOD::BTagVertexContainer> > jfvertices;
  try{
    jfvertices = bjet->auxdata<std::vector<ElementLink<xAOD::BTagVertexContainer> > >("JetFitter_JFvertices");
  } catch(...){
    ATH_MSG_WARNING("Unable to get \"JetFitter_JFvertices\"");
  }

  std::vector<const xAOD::BTagVertex*> output;
  for(auto el_vtx : jfvertices){
    if(!el_vtx.isValid()){
      ATH_MSG_WARNING("Invalid element link to JF vertices. It will be skipped");
      continue;
    }

    const xAOD::BTagVertex* vtx = (*el_vtx);
    if(vtx == 0){
      ATH_MSG_WARNING("Null ptr returned for JF vertices. It will be skipped");
      continue;
    }

    output.push_back(vtx);
  }

  return output;
}

std::vector<float> ExKtbbTag::GetJFfittedPosition(const xAOD::BTagging* bjet, std::vector<float>& JFfittedCov){
  std::vector<float> JFfittedPosition;
  JFfittedCov.clear();

  try{
    JFfittedPosition = bjet->auxdata<std::vector<float> >("JetFitter_fittedPosition");
    JFfittedCov      = bjet->auxdata<std::vector<float> >("JetFitter_fittedCov");
  }
  catch(...){
    ATH_MSG_WARNING("Unable to get \"JetFitter_fittedCov\" and/or \"JetFitter_fittedCov\"");
  }

  return JFfittedPosition;
}

bool ExKtbbTag::IsValidJF(const xAOD::BTagging* bjet, bool onlyVtx){
  int JFnvtx = 0;         bjet->taggerInfo(JFnvtx, xAOD::JetFitter_nVTX);
  int JFnsingletrks = 0;  bjet->taggerInfo(JFnsingletrks, xAOD::JetFitter_nSingleTracks);

  if(onlyVtx) return JFnvtx > 0;
  else        return (JFnvtx > 0) || (JFnsingletrks > 0); 
}

bool ExKtbbTag::JFDualValid(const xAOD::BTagging* bjet1, const xAOD::BTagging* bjet2, bool onlyVtx){
  return IsValidJF(bjet1, onlyVtx) && IsValidJF(bjet2, onlyVtx);
}

int ExKtbbTag::JFntrk(const xAOD::BTagging* bjet, bool onlyVtx){
  if(!IsValidJF(bjet, onlyVtx)){
    return -1;
  }
  else{
    int JFnvtxtrk = 0;     bjet->taggerInfo(JFnvtxtrk, xAOD::JetFitter_nTracksAtVtx);
    int JFnsingletrks = 0; bjet->taggerInfo(JFnsingletrks, xAOD::JetFitter_nSingleTracks);

    if(onlyVtx) return JFnvtxtrk;
    else        return JFnvtxtrk + JFnsingletrks;
  }
}

TLorentzVector ExKtbbTag::JFMomentum(const xAOD::BTagging* bjet, bool onlyVtx, bool doNeutralCorrection){
  // Initialization
  TLorentzVector SumChargeP4(0., 0., 0., 0.);
  TLorentzVector SumNeutralP4(0., 0., 0., 0.);
  double SumPtAdd = 0.;

  // quit for invalid jF
  if(!IsValidJF(bjet, onlyVtx)) return SumChargeP4;

  // get necessary ingredient
  std::vector<const xAOD::BTagVertex*> jfvertices = GetJFVertices(bjet);
  
  std::vector<float> fittedPosition; std::vector<float> fittedCov;
  fittedPosition = GetJFfittedPosition(bjet, fittedCov);

  // fitted direction
  TVector3 JFDir(1., 1., 1.);
  JFDir.SetMagThetaPhi(1., fittedPosition[4], fittedPosition[3]);

  // number of vtx (with at least 2 tracks)
  int nVtx = 0;
  bjet->taggerInfo(nVtx, xAOD::JetFitter_nVTX);

  // loop over vertices
  for(unsigned int ivtx = 0; ivtx < jfvertices.size(); ivtx++){
    auto JFVtx = jfvertices[ivtx];

    // reject negative vtx
    if(fittedPosition[5+ivtx] < 0) continue;

    // loop over tracks on vtx
    TLorentzVector TrackOnVtxP4(0., 0., 0., 0.);
    for(auto el_track : JFVtx->track_links()){
      if(!el_track.isValid()){
        ATH_MSG_WARNING("Missing link to tracks associated to JF vtx. It will be skipped");
        continue;
      }

      auto track = (*el_track);

      TrackOnVtxP4 += track->p4();
    }

    // get neutral momentum
    TVector3 JFDir_scale; JFDir_scale.SetMagThetaPhi(TrackOnVtxP4.Vect().Dot(JFDir), JFDir.Theta(), JFDir.Phi());
    TVector3 NeutralOnVtxP3 = JFDir_scale - TrackOnVtxP4.Vect();
    TLorentzVector NeutralOnVtxP4; NeutralOnVtxP4.SetVectM(NeutralOnVtxP3, 0.);

    // summation
    if(!onlyVtx){
      SumChargeP4 += TrackOnVtxP4;
      SumNeutralP4 += NeutralOnVtxP4;
      SumPtAdd += TrackOnVtxP4.Perp(JFDir);
    }
    else{
      if( (nVtx > 0 && JFVtx->track_links().size() > 1) || (nVtx == 0) ){ 
        SumChargeP4 += TrackOnVtxP4;
        SumNeutralP4 += NeutralOnVtxP4;
        SumPtAdd += TrackOnVtxP4.Perp(JFDir);
      }
    }
    
  }

  if(doNeutralCorrection){
    return SumChargeP4 + SumNeutralP4;
  }
  else{
    return SumChargeP4;
  }
}

double ExKtbbTag::JFEffectiveDecayLength(const xAOD::BTagging* bjet, bool onlyVtx, double& error){
  double decaylength = -1.;
  error = -1.;

  if(!IsValidJF(bjet, onlyVtx)) return decaylength;

  auto jfvertices = GetJFVertices(bjet);
  std::vector<float> fittedPosition;
  std::vector<float> fittedCov;
  fittedPosition = GetJFfittedPosition(bjet, fittedCov);

  // number of vtx (with at least 2 tracks)
  int nVtx = 0;
  bjet->taggerInfo(nVtx, xAOD::JetFitter_nVTX);

  // loop over vertices
  double sum_l = 0.;
  double sum_inverror2 = 0.;
  for(unsigned int ivtx = 0; ivtx < jfvertices.size(); ivtx++){
    auto JFVtx = jfvertices[ivtx];

    // reject negative vtx
    if(fittedPosition[5+ivtx] < 0) continue;

    double l = fittedPosition[5+ivtx];
    double error2 = fittedCov[5+ivtx];

    if(error2 == 0.){
      ATH_MSG_WARNING("Get 0 error for a fitted vtx decay length");
      continue;
    }

    if(!onlyVtx){
      sum_l += (l/error2);
      sum_inverror2 += (1./error2);
    }
    else{
      if( (nVtx > 0 && JFVtx->track_links().size() > 1) || (nVtx == 0) ){
        sum_l += (l/error2);
        sum_inverror2 += (1./error2);
      }
    }
  }

  // get result
  decaylength = sum_l/sum_inverror2;
  error = 1./TMath::Sqrt(sum_inverror2);

  return decaylength;
}

// calculate all eigen variation of vtx position
std::vector<Amg::Vector3D> ExKtbbTag::GetVtxEigenVariation(Amg::Vector3D vtxPosition, AmgSymMatrix3D vtxCovMatrix){
  std::vector<Amg::Vector3D> output;

  // solve eigen system
  Eigen::SelfAdjointEigenSolver<AmgSymMatrix3D> EigenSolver(vtxCovMatrix);
  if(EigenSolver.info() != Eigen::Success){
    ATH_MSG_WARNING("Input matrix is not Hermitian, which should be impossible for covariant matrix!");
    return output;
  }

  auto EigenValues = EigenSolver.eigenvalues();
  auto EigenVectors = EigenSolver.eigenvectors();

  // get variation
  for(unsigned int index = 0; index < 3; index++){
    Amg::Vector3D vtxPositionVariation_Up;
    vtxPositionVariation_Up(0) = vtxPosition(0) + TMath::Sqrt(EigenValues(index)) * EigenVectors(0, index);
    vtxPositionVariation_Up(1) = vtxPosition(1) + TMath::Sqrt(EigenValues(index)) * EigenVectors(1, index);
    vtxPositionVariation_Up(2) = vtxPosition(2) + TMath::Sqrt(EigenValues(index)) * EigenVectors(2, index);

    Amg::Vector3D vtxPositionVariation_Down;
    vtxPositionVariation_Down(0) = vtxPosition(0) - TMath::Sqrt(EigenValues(index)) * EigenVectors(0, index);
    vtxPositionVariation_Down(1) = vtxPosition(1) - TMath::Sqrt(EigenValues(index)) * EigenVectors(1, index);
    vtxPositionVariation_Down(2) = vtxPosition(2) - TMath::Sqrt(EigenValues(index)) * EigenVectors(2, index);

    output.push_back(vtxPositionVariation_Up);
    output.push_back(vtxPositionVariation_Down);
  }          

  return output;
}

double ExKtbbTag::GeneralDRSignificance3D(Amg::Vector3D vtx1, AmgSymMatrix3D vtx1_CovMatrix, Amg::Vector3D vtx2, AmgSymMatrix3D vtx2_CovMatrix, double& dR3D, double& dR3D_error){
  dR3D = -1.;
  dR3D_error = -1.;

  std::vector<Amg::Vector3D> vtx1_variations = GetVtxEigenVariation(vtx1, vtx1_CovMatrix);
  std::vector<Amg::Vector3D> vtx2_variations = GetVtxEigenVariation(vtx2, vtx2_CovMatrix);

  auto function_GetdR3D = [](Amg::Vector3D input1, Amg::Vector3D input2)->double{
    return TMath::Sqrt((input1 - input2).dot(input1 - input2));
  };

  dR3D = function_GetdR3D(vtx1, vtx2);

  double sumerror_vtx1 = 0.;
  double sumerror_vtx2 = 0.;
  for(unsigned int index = 0; index < 3; index++){
    double error_vtx1 = std::max(fabs(function_GetdR3D(vtx1_variations[2*index], vtx2) - dR3D), fabs(function_GetdR3D(vtx1_variations[2*index+1], vtx2) - dR3D));
    sumerror_vtx1 += (error_vtx1 * error_vtx1);

    double error_vtx2 = std::max(fabs(function_GetdR3D(vtx1, vtx2_variations[2*index]) - dR3D), fabs(function_GetdR3D(vtx1, vtx2_variations[2*index+1]) - dR3D));
    sumerror_vtx2 += (error_vtx2 * error_vtx2);
  }

  double sumerror = sumerror_vtx1 + sumerror_vtx2;
  dR3D_error = TMath::Sqrt(sumerror);

  double significance = 0.;
  if(dR3D_error == 0.){
    ATH_MSG_WARNING("Zero error obtained in GeneralDRSignificance3D, which is very unlikely.");
    significance = 999.;
  }
  else{
    significance = dR3D/dR3D_error;
  }

  significance = LimitUpperBound(significance, 50, 100);
  return significance;
}

}//end namespace



