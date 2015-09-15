#ifndef JETTAGTOOLS_MV2TAG_H
#define JETTAGTOOLS_MV2TAG_H

/******************************************************
    @class MV2Tag
    Neural-net tagger combining weights of IP3D, SV1 and 
    JetFitterCombNN
    @ author L. Vacavant
********************************************************/

#include "AthenaBaseComps/AthAlgTool.h"
#include "GaudiKernel/ToolHandle.h"
#include "JetTagTools/ITagTool.h"
#include <string>
#include <map>
#include <list>
#include "egammaMVACalib/egammaMVACalib.h"
#include "egammaMVACalib/BDT.h"
#include "egammaMVACalib/Node.h"
#include "TMVA/MethodBase.h"
#include "TMVA/IMethod.h"

namespace TMVA { class Reader; }
namespace Analysis { class CalibrationBroker; }

namespace Analysis { 

  class MV2Tag : public AthAlgTool , virtual public ITagTool {
   
  public:
    MV2Tag(const std::string&,const std::string&,const IInterface*);
      
    /**
       Implementations of the methods defined in the abstract base class
    */
    virtual ~MV2Tag();
    StatusCode initialize();
    StatusCode finalize();
      
    /** Set the primary vertex. TODO: This is temporary ! The primary vertex should
	be part of the JetTag IParticle interface implementation. The trouble with 
	ElementLink and persistency has to be solved for that. Revisit ... */
    void setOrigin(const xAOD::Vertex* priVtx);

    StatusCode tagJet(xAOD::Jet& jetToTag, xAOD::BTagging* BTag);

    void finalizeHistos() {};

  private:      

    std::string m_taggerName;
    std::string m_taggerNameBase; // unique name for regular and flip versions
    std::string m_treeName;
    std::string m_varStrName;

    /** pointer to calibration in COOL: */
    ToolHandle<CalibrationBroker> m_calibrationTool;
    bool m_forceMV2CalibrationAlias;
    bool m_useEgammaMethodMV2;
    bool m_decorateBTaggingObj;
    std::string m_decTagName;
    std::string m_MV2CalibAlias;
    std::string m_MV2cXX;
    std::string m_xAODBaseName;
    
    const unsigned m_nClasses=3;//b,u,c probabilities. It might be better to read from calib file for future
    const bool m_writeRootFile=false;//Developper option
    bool m_disableAlgo;
    int  m_warnCounter;

    /** This switch is needed to indicate what to do. The algorithm can be run to produce
	reference histograms from the given MC files (m_runModus=0) or to work in analysis mode
	(m_runModus=1) where already made reference histograms are read.*/ 
    std::string    m_runModus;          //!< 0=Do not read histos, 1=Read referece histos (analysis mode)

    /** Storage for the primary vertex. Can be removed when JetTag provides origin(). */
    // this pointer does not need to be deleted in the destructor (because it
    // points to something in storegate)
    const xAOD::Vertex* m_priVtx;

    /** reader to define the TMVA algorithms */
    float m_pt;
    float m_absEta;

    float m_trkSum_ntrk;
    float m_trkSum_sPt;
    float m_trkSum_vPt;
    float m_trkSum_vAbsEta;

    //more ip2 variables
    float m_ip2;
    float m_ip2_c;
    float m_ip2_cu;
    //more ip3 variables
    float m_ip3;
    float m_ip3_c;
    float m_ip3_cu;
    //more sv1 variables
    float m_sv1;
    float m_sv1_c;
    float m_sv1_cu;
    float m_sv1_ntkv; 
    float m_sv1_mass; 
    float m_sv1_efrc; 
    float m_sv1_n2t; 
    float m_sv1_Lxy;
    float m_sv1_L3d;
    float m_sv1_sig3;
    float m_sv1_dR;
    //more jf variables
    float m_jf_dR;

    /////////////////////////////////////////////////////////////////////
    //IP2D posteriors
    float m_ip2_pu; 
    float m_ip2_pb; 
    float m_ip2_pc; 
    //IP3D posteriors
    float m_ip3_pu; 
    float m_ip3_pb; 
    float m_ip3_pc; 
    //SV1 posteriors
    float m_sv1_pu; 
    float m_sv1_pb; 
    float m_sv1_pc; 
    //JetFitterCombNN posteriors
    float m_jfc_pu; 
    float m_jfc_pb; 
    float m_jfc_pc; 
    //SV0 informations
    float m_sv0; 
    float m_sv0_ntkv; 
    float m_sv0_mass; 
    float m_sv0_efrc; 
    float m_sv0_n2t; 
    float m_sv0_radius; 
    //JetFitter informations
    float m_jf_mass; 
    float m_jf_efrc; 
    float m_jf_n2tv; 
    float m_jf_ntrkv; 
    float m_jf_nvtx; 
    float m_jf_nvtx1t; 
    float m_jf_dphi; 
    float m_jf_deta; 
    //float m_chi2Ondof;
    float m_jf_sig3;

    //mvb variables
    float m_width;//width of b-tag tracks
    float m_n_trk_sigd0cut;
    float m_trk3_d0sig;
    float m_trk3_z0sig;
    float m_sv_scaled_efc;
    float m_jf_scaled_efc;

    std::map<std::string, TMVA::Reader*> m_tmvaReaders;
    std::map<std::string, TMVA::MethodBase*> m_tmvaMethod; 
    std::map<std::string, egammaMVACalibNmsp::BDT*> m_egammaBDTs;
    std::list<std::string> m_undefinedReaders; // keep track of undefined readers to prevent too many warnings.


    std::string m_ip2d_infosource;
    std::string m_ip3d_infosource;
    std::string m_sv1_infosource;
    std::string m_sv0_infosource;
    std::string m_jftNN_infosource;
    std::string m_jfprob_infosource;

    std::string m_trainingConfig;
    float d0sgn_wrtJet(const TLorentzVector& jet, const TLorentzVector& trk, float d0sig);
    float z0sgn_wrtJet(float trackTheta, float trackZ0, float jetEta);
    //void setInputVariables(xAOD::Jet& jetToTag, xAOD::BTagging* BTag);//for future
    void ClearInputs();
    void PrintInputs();
    void SetVariableRefs(const std::vector<std::string> inputVars, TMVA::Reader* tmvaReader, 
			  unsigned &nConfgVar, bool &badVariableFound, std::vector<float*> &inputPointers);
    //KM: The fuctions below will be migrated to the new class, somewhere in common btwn egamma/b-tagging
    std::vector<float> GetMulticlassResponse(egammaMVACalibNmsp::BDT* bdt,const std::vector<float>& values   ) const;
    std::vector<float> GetMulticlassResponse(egammaMVACalibNmsp::BDT* bdt,const std::vector<float*>& pointers) const;
    std::vector<float> GetMulticlassResponse(egammaMVACalibNmsp::BDT* bdt) const {
      std::vector<float> v(m_nClasses,-1);
      return (bdt->GetPointers().size() ? GetMulticlassResponse(bdt,bdt->GetPointers()) : v); 
    }
    double GetClassResponse (egammaMVACalibNmsp::BDT* bdt,const std::vector<float>& values   ) const;
    double GetClassResponse (egammaMVACalibNmsp::BDT* bdt,const std::vector<float*>& pointers) const;
    double GetClassResponse (egammaMVACalibNmsp::BDT* bdt) const { return (bdt->GetPointers().size() ? GetClassResponse(bdt,bdt->GetPointers()) : -9.); }
  }; // End class


  inline void MV2Tag::setOrigin(const xAOD::Vertex* priVtx) { m_priVtx=priVtx; }

} // End namespace 

#endif
