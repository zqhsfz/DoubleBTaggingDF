/***************************************************************************
                          JetVertexCharge.h  -  Description
                             -------------------

    created : March 2015
    authors: Luca Colasurdo (Radboud Universiteit van Nijmegen/Nikhef)
    email : luca.colasurdo@cern.ch
    changes: final version
 

  This class implements the tool to tag a b-jet as b-/bbar-jet.
     
 ***************************************************************************/

#ifndef JetVertexCharge_H
#define JetVertexCharge_H

#include "AthenaBaseComps/AthAlgTool.h"
#include "GaudiKernel/ToolHandle.h"

#include "JetTagTools/ITagTool.h"

#include "xAODTracking/TrackParticle.h"

//#include "xAODTruth/TruthEventContainer.h"

#include "TMVA/IMethod.h"
#include "TMVA/MethodBase.h"
namespace TMVA { class Reader; }
namespace Analysis { class CalibrationBroker; }


namespace Analysis { 


  class ParticleToJetAssociator;  


  class JetVertexCharge : public AthAlgTool, virtual public ITagTool
  {

    public:

 

    JetVertexCharge(const std::string& t, const std::string& n, const IInterface*  p);

    virtual ~JetVertexCharge();  

    StatusCode initialize();
    StatusCode finalize();
    
    void setOrigin( const xAOD::Vertex*); 
    void finalizeHistos(); 
    

    StatusCode tagJet(xAOD::Jet& jetToTag, xAOD::BTagging* BTag); 


  private:



//      data members
//------------------------------------------------------------------------            

   std::string m_secVxFinderName;
   ToolHandle<CalibrationBroker> m_calibrationTool;
   const xAOD::Vertex *m_primVtx; 


   enum MVAcat {
     JC_SVC_0mu = 1,
     JC_SVC_1mu,
     JC_SVC_TVC_0mu,
     JC_SVC_TVC_1mu,
     SVC,  
     JC,  
   }; 




    
//      configurable data members
//------------------------------------------------------------------------


   std::string m_runModus;  
   std::string m_trackAssociationName;
   std::string m_muonAssociationName;

   std::vector<std::string> m_jetCollectionList; 

   std::string m_taggerNameBase;   
   bool m_doForcedCalib;
   std::string m_ForcedCalibName;

   double m_kappa;
   double m_kappa_SV;
   double m_kappa_TV;

   double m_Trkd0Cut;
   double m_Trkz0Cut;
   double m_TrkPtCut;
   double m_TrkChi2Cut;
   int m_CutPrecisionHits;
   int m_CutPixelHits;
   int m_CutTRTHits;
   int m_CutBLayerHits;
   int m_CutSCTHits;
   int m_CutSharedHits;


   std::map<std::string, TMVA::Reader*> m_tmvaReaders;
   std::map<std::string, TMVA::MethodBase*> m_tmvaMethod;
   std::list<std::string> m_undefinedReaders;

   std::map< int, TH1F* > m_histoList_pos;
   std::map< int, TH1F* > m_histoList_neg;

   float m_jc_mva;
   float m_svc_mva;
   float m_tvc_mva;
   float m_sum_mva;
   float m_diff_mva;

   float m_ngoodtrk_mva;

   float m_sv_trk_mva;
   float m_sv_comp_mva;
   float m_sv_dist_mva;
   float m_sv_err_mva;
   float m_sv_chi2_mva;

   float m_tv_trk_mva;
   float m_tv_comp_mva;
   float m_tv_dist_mva;
   float m_tv_err_mva;
   float m_tv_chi2_mva;

   float m_mu_charge_mva;
   float m_mu_vtx_mva;
   float m_mu_ptRel_mva;
   float m_mu_ptLong_mva;


//      methods
//------------------------------------------------------------------------

   bool passTrackCuts( const xAOD::TrackParticle &track ) const; 

   int category( float, float, float, int); 
   float probability( int cat , float w, std::string author, std::string alias); 

   struct myVtxInfo{ 
        float chi2;
        float pos;
        float err;
        float compPV;
	std::vector< const xAOD::TrackParticle*> tracks;
   };





};//end class declaration

  inline void JetVertexCharge::setOrigin(const xAOD::Vertex* vtx) { m_primVtx = vtx; }
  inline void JetVertexCharge::finalizeHistos( ) {  return; }

}  //End namespace

#endif

