/***************************************************************************
                          JetVertexCharge.cxx  -  Description
                             -------------------

    created : March 2015
    authors: Luca Colasurdo (Radboud University Nijmegen and Nikhef)
    email : luca.colasurdo@cern.ch



  Look at the header file for more information.
     
 ***************************************************************************/

#include "JetTagTools/JetVertexCharge.h"

#include "CLHEP/Vector/LorentzVector.h"

#include "xAODMuon/MuonContainer.h"
#include "xAODMuon/Muon.h"


#include "JetTagTools/JetTagUtils.h"
#include "JetTagCalibration/CalibrationBroker.h"
#include "TMVA/Reader.h"
#include "TMVA/Types.h"
#include "TList.h"
#include "TObjString.h"

#include "TMVA/IMethod.h"
#include "TMVA/BinarySearchTree.h"
#include "TMVA/MethodBase.h"


#include "xAODBTagging/BTagVertex.h"

#include "ParticleJetTools/ParticleToJetAssociator.h"


namespace Analysis { 


  JetVertexCharge::JetVertexCharge(const std::string& t, const std::string& n, const IInterface*  p) :
    AthAlgTool(t,n,p),
    m_runModus("analysis"), 
    m_calibrationTool("BTagCalibrationBroker")
  { 

    declareProperty("SecVxFinderName",		m_secVxFinderName);
    declareProperty("Runmodus",                 m_runModus);

    declareProperty("calibrationTool", 		m_calibrationTool);
    declareProperty("taggerNameBase",		m_taggerNameBase = "JetVertexCharge");

    declareProperty("jetCollectionList", 	m_jetCollectionList);
    declareProperty("useForcedCalibration",  	m_doForcedCalib);

    declareProperty("muonAssociationName", 	m_muonAssociationName = "Muons");
    declareProperty("trackAssociationName", 	m_trackAssociationName = "BTagTrackToJetAssociator"); 

    declareProperty("kFactor", 			m_kappa = 0.9);
    declareProperty("kFactorSV", 		m_kappa_SV = 0.5);
    declareProperty("kFactorTV", 		m_kappa_TV = 0.5);  

    declareProperty("Trkd0Cut",           	m_Trkd0Cut=4.5);
    declareProperty("Trkz0Cut",           	m_Trkz0Cut=2.);  
    declareProperty("TrkPtCut",           	m_TrkPtCut=500.0); 
    declareProperty("TrkChi2Cut",         	m_TrkChi2Cut=5.0);  
    declareProperty("CutPrecisionHits",	  	m_CutPrecisionHits= 9 ); 
    declareProperty("CutPixHits",		m_CutPixelHits= 1  ); 
    declareProperty("CutTRTHits",		m_CutTRTHits= 9  ); 
    declareProperty("CutBLayHits",		m_CutBLayerHits= 0 ); 
    declareProperty("CutSctHits",		m_CutSCTHits= 4  ); 
    declareProperty("CutSharedHits",		m_CutSharedHits= 1  ); 


    declareInterface< ITagTool >(this);

  }
  
///////////
//Destructor
  JetVertexCharge::~JetVertexCharge() { }
  

///////////
//Initialize method
  StatusCode JetVertexCharge::initialize() {

    StatusCode sc = m_calibrationTool.retrieve();
    if ( sc.isFailure() ) {
      ATH_MSG_FATAL("#BTAG# Failed to retrieve tool " << m_calibrationTool);
      return sc;
    } else {
      ATH_MSG_DEBUG("#BTAG# Retrieved tool " << m_calibrationTool);
    }

    m_calibrationTool->registerHistogram(m_taggerNameBase, m_taggerNameBase+"Calib_cat_JC_SVC_noMu");
    m_calibrationTool->registerHistogram(m_taggerNameBase, m_taggerNameBase+"Calib_cat_JC_SVC_incMu");
    m_calibrationTool->registerHistogram(m_taggerNameBase, m_taggerNameBase+"Calib_cat_JC_SVC_TVC_noMu");
    m_calibrationTool->registerHistogram(m_taggerNameBase, m_taggerNameBase+"Calib_cat_JC_SVC_TVC_incMu");


    m_calibrationTool->registerHistogram(m_taggerNameBase, "jvc_JC_SVC_noMu_b");
    m_calibrationTool->registerHistogram(m_taggerNameBase, "jvc_JC_SVC_noMu_bbar");
    m_calibrationTool->registerHistogram(m_taggerNameBase, "jvc_JC_SVC_incMu_b");
    m_calibrationTool->registerHistogram(m_taggerNameBase, "jvc_JC_SVC_incMu_bbar");
    m_calibrationTool->registerHistogram(m_taggerNameBase, "jvc_JC_SVC_TVC_noMu_b");
    m_calibrationTool->registerHistogram(m_taggerNameBase, "jvc_JC_SVC_TVC_noMu_bbar");
    m_calibrationTool->registerHistogram(m_taggerNameBase, "jvc_JC_SVC_TVC_incMu_b");
    m_calibrationTool->registerHistogram(m_taggerNameBase, "jvc_JC_SVC_TVC_incMu_bbar");
    m_calibrationTool->registerHistogram(m_taggerNameBase, "jvc_JC_x_b");
    m_calibrationTool->registerHistogram(m_taggerNameBase, "jvc_JC_x_bbar");
    m_calibrationTool->registerHistogram(m_taggerNameBase, "jvc_SVC_x_b");
    m_calibrationTool->registerHistogram(m_taggerNameBase, "jvc_SVC_x_bbar");




    m_tmvaReaders.clear();
    m_tmvaMethod.clear();

    m_histoList_pos.clear();
    m_histoList_neg.clear();


    return StatusCode::SUCCESS;
  }
  

///////////
//Finalize method
  StatusCode JetVertexCharge::finalize() {
    

    //delete readers;
    std::map<std::string, TMVA::Reader*>::iterator pos = m_tmvaReaders.begin();
    for( ; pos != m_tmvaReaders.end(); ++pos ) delete pos->second;
    std::map<std::string, TMVA::MethodBase*>::iterator posm = m_tmvaMethod.begin();
    for( ; posm != m_tmvaMethod.end(); ++posm ) delete posm->second;
    

    msg(MSG::DEBUG)  << "Finalize successful" << endreq;
    return StatusCode::SUCCESS;
    
  } 


//////////////////////////////////////////////////////////////////  
StatusCode JetVertexCharge::tagJet( xAOD::Jet& jetToTag, xAOD::BTagging* BTag) {


   /** author to know which jet algorithm: */ 
   std::string author = JetTagUtils::getJetAuthor(jetToTag);
   if (m_doForcedCalib) author = m_ForcedCalibName;
   std::string alias = m_calibrationTool->channelAlias(author);


   //  *****    computing the JetCharge (JC)   *******
   float jetCharge = -3.;
   float ngoodtrk=0;

   std::vector<ElementLink< xAOD::TrackParticleContainer > > tracksInJet;        
   tracksInJet = BTag->auxdata< std::vector<ElementLink< xAOD::TrackParticleContainer > > >(m_trackAssociationName);
   if( tracksInJet.size() == 0 ) {
      ATH_MSG_DEBUG("#BTAG#  Could not find tracks associated with name " << m_trackAssociationName);
   } else {

      float  charge = 0, denom=0;

      for(std::vector<ElementLink< xAOD::TrackParticleContainer > >::iterator itEL = tracksInJet.begin(); itEL != tracksInJet.end(); ++itEL ) {
  	 const xAOD::TrackParticle* tp = *(*itEL);
         if( !passTrackCuts(*tp)) continue; 
	 ngoodtrk++;
         charge += ( tp->charge()) * std::pow( tp->pt(), m_kappa ); 
         denom += pow( tp->pt(), m_kappa);
      }

      if(denom != 0) charge /= denom;
      else charge = -3; 
      jetCharge = charge;

   }



   //  *****    computing the Vertex Jet Charges (SVC/TVC)   *******
  
   std::vector< myVtxInfo > *myVector = new std::vector< myVtxInfo> ();   

   float jf_svc = -3.;
   float jf_tvc = -3.;

   float ntrk_sv = -1.;
   float dist_SV = -9999.;
   float err_SV = -999.;
   float comp_SV = -1.;
   float chi2_SV = -1.;

   float ntrk_tv = -1.;
   float tot_ntrk_tv = -1; 
   float dist_TV = -9999.;
   float err_TV = -999.;
   float comp_TV = -1.;
   float chi2_TV = -1.;

   std::vector<ElementLink<xAOD::BTagVertexContainer> >  JFVerticesLinks; 
   bool ret = BTag->variable<std::vector<ElementLink<xAOD::BTagVertexContainer>>>("JetFitter", "JFvertices", JFVerticesLinks );
   if(ret) {
      if( JFVerticesLinks.size() ==0) { 
	ATH_MSG_DEBUG("#BTAG# No JF vertices ");  
      } else {  

        std::vector<float> fittedPosition;
        std::vector< float > fittedCov; 
        BTag->variable<std::vector< float > >("JetFitter", "fittedPosition", fittedPosition);
        BTag->variable<std::vector< float > >("JetFitter", "fittedCov", fittedCov);
          


        for( int ivx = 0; ivx< JFVerticesLinks.size(); ivx++) {
	   const xAOD::BTagVertex *myBTagVtx = (*JFVerticesLinks.at(ivx)); 

           //Cutting on the vertices
           float chi2 = myBTagVtx->chi2()/myBTagVtx->NDF(); 
	   if( chi2 > 5. )  continue; 
	   if( fittedPosition.at(ivx+5)<0. )  continue; 
         
	   myVtxInfo newVtx;
           newVtx.tracks.clear();
	   newVtx.chi2 = chi2;
	   newVtx.pos = fittedPosition.at(ivx+5);
	   newVtx.err = sqrt(fittedCov.at(ivx+5) );
           newVtx.compPV = myBTagVtx->pv_compatibility();
           const std::vector< ElementLink<xAOD::TrackParticleContainer> > tpLinks = myBTagVtx->track_links();

	   for( unsigned int it=0; it< tpLinks.size(); it++) {
  	     newVtx.tracks.push_back( *tpLinks.at(it)  );
	   }
	   myVector->push_back(newVtx);

        }

        //ordering the Vx according to d0
        bool changeD0 = true;
        while (changeD0) {
          changeD0 = false;
          for( int ivx=0; ivx< 1.*myVector->size() -1; ivx++) {  
            float pos1 = myVector->at(ivx).pos; 
            float pos2 = myVector->at(ivx +1).pos; 
            if( fabs(pos1) > fabs(pos2)  ) { 
	       myVtxInfo tempVtx = myVector->at(ivx);
               myVector->at(ivx) = myVector->at(ivx + 1);
               myVector->at(ivx+1) = tempVtx;  
               changeD0 = true;
            }
          }
        }

      }   //There is at least 1 vtx



      //Merge the "higher-vertices"
      if( myVector->size()>2  ) {

         double sumw = 0;
         float compmax=0;
         float chi2max=0;

         for( int ivx = 1; ivx<  (int) myVector->size(); ivx++) {  //skip SV 
           double w = 1./std::pow( myVector->at(ivx).err, 2 );
           sumw += w;
           if( ivx>1) myVector->at(1).pos += myVector->at(ivx).pos*w; 
           else if( ivx==1) myVector->at(1).pos = myVector->at(ivx).pos*w; 
	   compmax = std::max( compmax, myVector->at(ivx).compPV);        
	   chi2max = std::max( chi2max, myVector->at(ivx).chi2);	
           int size = myVector->at(ivx).tracks.size();
 	   for(int itrk=0; (itrk<size && ivx != 1); itrk++) {              //so that I don't count the TV tracks twice 
	      const xAOD::TrackParticle *tp =  myVector->at(ivx).tracks.at(itrk);
	      myVector->at(1).tracks.push_back(tp);
 	    } 
         }

         myVector->at(1).pos /= sumw;
         myVector->at(1).err = 1./sumw;
         myVector->at(1).chi2 = chi2max;
         myVector->at(1).compPV = compmax;

         for( uint i=1; i<myVector->size(); i++) {  //erase the other vertices
           myVector->erase( myVector->begin() + i);
         }
      }


      for( int ivx = 0; ivx< (int) myVector->size() ; ivx++) { 
         myVtxInfo vtx = myVector->at(ivx);
         int size = vtx.tracks.size();
         int maxTracks = size;

         if( (size % 2) == 1 ) maxTracks = size -1;  //To use only an even N tracks for the TVC 

         if(ivx==0) ntrk_sv = 1.*size; //1.*maxTracks; 
         else if(ivx==1) { ntrk_tv = 1.*maxTracks; tot_ntrk_tv = 1.*size; }

         //    pT-ordering the tracks  only for tv 
         bool change = true;
         while( change && ivx==1) {
  	   int length = size-1;
	   int limit=0;
	   change = false;
	   for( int itrk=0; itrk<length; itrk++) { 
	     double pt1 = vtx.tracks.at(itrk)->pt();  
	     double pt2 = vtx.tracks.at(itrk +1)->pt();  
	     if( pt1 < pt2  ) {
               change = true;
	       limit = itrk;
	       const xAOD::TrackParticle* temp = vtx.tracks.at(itrk+1);
	       vtx.tracks.at(itrk+1) = vtx.tracks.at(itrk); 
	       vtx.tracks.at(itrk) = temp; 
	     }
   	   }
	   length = limit;
         }


	 if( ivx == 0) {
    	    float charge = 0, denom = 0;
  	    for(int itrk=0;  itrk< ntrk_sv; itrk++) {
	       const xAOD::TrackParticle *tp =  vtx.tracks.at(itrk);
               charge += ( tp->charge()) * std::pow( tp->pt(), m_kappa_SV); 
               denom += pow( tp->pt(), m_kappa_SV);
	    }
	    if(denom != 0)  jf_svc = charge/denom;
            else jf_svc = -3; 

            dist_SV =  vtx.pos;
            err_SV =  vtx.err;
            chi2_SV =  vtx.chi2;
            comp_SV =  vtx.compPV;
         }
	 else if( ivx == 1) {
    	    float charge = 0, denom = 0;
  	    for(int itrk=0;  itrk< ntrk_tv; itrk++) {
	       const xAOD::TrackParticle *tp =  vtx.tracks.at(itrk);
               charge += ( tp->charge()) * std::pow( tp->pt(), m_kappa_TV); 
               denom += pow( tp->pt(), m_kappa_TV);
 	    }
            if(denom != 0)  jf_tvc = charge/denom;
            else jf_tvc = -3; 
            dist_TV =  vtx.pos;
            err_TV =  vtx.err;
            chi2_TV =  vtx.chi2;
            comp_TV =  vtx.compPV;
	 }
      }  //closes the loop on vertices
   } //close the if (ret)  


   //  *****    computing the Muon Variables     *******

   float mu_vtx = -1.;
   float mu_charge = 0.;
   float mu_ptRel = -99.;
   float mu_ptLong = -99.;

   std::vector<ElementLink< xAOD::MuonContainer > > muonsInJet;       
   muonsInJet = BTag->auxdata< std::vector<ElementLink< xAOD::MuonContainer > > >(m_muonAssociationName); 

   if( muonsInJet.size() == 0 ) {
      ATH_MSG_DEBUG("#BTAG#  Could not find muons associated with name " << m_muonAssociationName);
   } 
   else {
     const  xAOD::Muon * myMuon=NULL;  
     double ptmax = 1.;
     for( unsigned int mu=0; mu< muonsInJet.size(); mu++)  {
        const xAOD::Muon *m = *(muonsInJet.at(mu));
        if( m->pt() > ptmax) { myMuon = m;  ptmax = m->pt();  }
     }


     //want to see if it's close to a track 
     double deltaR = 0.07;
     double deltaPt = 0.1*myMuon->pt(); 
     for( uint ivx=0; ivx< myVector->size(); ivx++) {
        for( uint itrk=0; itrk< myVector->at(ivx).tracks.size(); itrk++) {
          const xAOD::TrackParticle *tp =  myVector->at(ivx).tracks.at(itrk);

          double rtu = myMuon->p4().DeltaR( tp->p4()  ); 
          double ptu = fabs( myMuon->pt() - tp->pt() );  
          if ( rtu < deltaR && ptu<deltaPt  )   {
             deltaR = rtu;
             deltaPt = ptu;
             mu_vtx = ivx +1.; 
          }
        }
     }

     if( mu_vtx ==-1) mu_vtx = 0.; 
     TLorentzVector muon = myMuon->p4();      
     TLorentzVector jet = jetToTag.p4();      
     mu_ptRel = muon.P()*sin( muon.Angle( jet.Vect() ) );
     mu_ptLong = muon.P()*cos( muon.Angle( jet.Vect() ) );
     const xAOD::TrackParticle *trackMuon = myMuon->primaryTrackParticle(); 
     if( trackMuon) mu_charge = trackMuon->charge(); 
        
   } //closes the  if(muonsInJet.size()==0)-else



	   /******  NOW THE MVA PART   *****/
   int mvaCat = category( jetCharge, jf_svc, jf_tvc, fabs(mu_charge) ); 

   if( m_runModus == "reference") {
      BTag->setVariable<float>(m_taggerNameBase, "JetCharge", jetCharge);
      BTag->setVariable<float>(m_taggerNameBase, "nJCtracks", ngoodtrk);

      BTag->setVariable<float>(m_taggerNameBase, "SVC", jf_svc);
      BTag->setVariable<float>(m_taggerNameBase, "ntrk_sv", ntrk_sv);
      BTag->setVariable<float>(m_taggerNameBase, "dist_SV", dist_SV);
      BTag->setVariable<float>(m_taggerNameBase, "err_SV", err_SV);
      BTag->setVariable<float>(m_taggerNameBase, "comp_SV", comp_SV);
      BTag->setVariable<float>(m_taggerNameBase, "chi2_SV", chi2_SV);
    
      BTag->setVariable<float>(m_taggerNameBase, "TVC", jf_tvc);
      BTag->setVariable<float>(m_taggerNameBase, "ntrk_tv", tot_ntrk_tv);
      BTag->setVariable<float>(m_taggerNameBase, "dist_TV", dist_TV);
      BTag->setVariable<float>(m_taggerNameBase, "err_TV", err_TV);
      BTag->setVariable<float>(m_taggerNameBase, "comp_TV", comp_TV);
      BTag->setVariable<float>(m_taggerNameBase, "chi2_TV", chi2_TV);
    
      BTag->setVariable<float>(m_taggerNameBase, "mu_charge", mu_charge);
      BTag->setVariable<float>(m_taggerNameBase, "mu_vtx", mu_vtx);
      BTag->setVariable<float>(m_taggerNameBase, "mu_ptRel", mu_ptRel);
      BTag->setVariable<float>(m_taggerNameBase, "mu_ptLong", mu_ptLong);

      BTag->setVariable<int>(m_taggerNameBase, "category", mvaCat );
      BTag->setVariable<float>(m_taggerNameBase, "discriminant", -3. );
   } 
   else if( m_runModus == "analysis") { 


   TMVA::Reader* tmvaReader;
   std::map<std::string, TMVA::Reader*>::iterator pos;




   // check if calibration (neural net structure or weights) has to be updated: 
   std::pair<TList*, bool> calib;
   if(mvaCat == JC ) {  //ordered in order of probability 
      float prob = probability( JC, jetCharge , author, alias);
      BTag->setVariable<float>(m_taggerNameBase, "discriminant", prob );
      return StatusCode::SUCCESS;
   } 
   else if(mvaCat==-1) { 
      BTag->setVariable<float>(m_taggerNameBase, "discriminant", -3 );
      return StatusCode::SUCCESS;
   } 
   else if( mvaCat == JC_SVC_0mu ) calib = m_calibrationTool->retrieveTObject<TList>(m_taggerNameBase, author, m_taggerNameBase+"Calib_cat_JC_SVC_noMu");
   else if(mvaCat == JC_SVC_1mu ) calib = m_calibrationTool->retrieveTObject<TList>(m_taggerNameBase, author, m_taggerNameBase+"Calib_cat_JC_SVC_incMu");
   else if(mvaCat == JC_SVC_TVC_0mu ) calib = m_calibrationTool->retrieveTObject<TList>(m_taggerNameBase, author, m_taggerNameBase+"Calib_cat_JC_SVC_TVC_noMu");
   else if(mvaCat == JC_SVC_TVC_1mu ) calib = m_calibrationTool->retrieveTObject<TList>(m_taggerNameBase, author, m_taggerNameBase+"Calib_cat_JC_SVC_TVC_incMu");
   else if(mvaCat == SVC ) { 
      float prob = probability( SVC, jf_svc , author, alias);
      BTag->setVariable<float>(m_taggerNameBase, "discriminant", prob );
      return StatusCode::SUCCESS;
   } 


   std::ostringstream iss;
   TMVA::MethodBase * kl=0; 
   std::map<std::string, TMVA::MethodBase*>::iterator itmap;

   bool calibHasChanged = calib.second;
   if(calibHasChanged) { 
      ATH_MSG_DEBUG("#BTAG# " << m_taggerNameBase << " calib updated -> try to retrieve");
  
      if(!calib.first) {
        ATH_MSG_WARNING("#BTAG# Tlist can't be retrieved -> no calibration for "<< m_taggerNameBase );
        BTag->setVariable<float>(m_taggerNameBase, "discriminant", -3 );
        return StatusCode::SUCCESS;
      }

      if( mvaCat == JC_SVC_0mu) m_calibrationTool->updateHistogramStatus(m_taggerNameBase, alias, m_taggerNameBase+"Calib_cat_JC_SVC_noMu", false);
      else if( mvaCat == JC_SVC_1mu) m_calibrationTool->updateHistogramStatus(m_taggerNameBase, alias, m_taggerNameBase+"Calib_cat_JC_SVC_incMu", false);
      else if( mvaCat == JC_SVC_TVC_0mu) m_calibrationTool->updateHistogramStatus(m_taggerNameBase, alias, m_taggerNameBase+"Calib_cat_JC_SVC_TVC_noMu", false);
      else if( mvaCat == JC_SVC_TVC_1mu) m_calibrationTool->updateHistogramStatus(m_taggerNameBase, alias, m_taggerNameBase+"Calib_cat_JC_SVC_TVC_incMu", false);

      //now the new part istringstream
      TList* list = calib.first; 

      for(int i=0; i<list->GetSize(); ++i) {
        TObjString* ss = (TObjString*)list->At(i);
        std::string sss = ss->String().Data();
        //KM: if it doesn't find "<" in the string, it starts from non-space character
        int posi = sss.find('<')!=-1 ? sss.find('<') : sss.find_first_not_of(" ");
        std::string tmp = sss.erase(0,posi);
        iss << tmp.data(); 
      }

    
      // now configure the TMVAReaders:
      tmvaReader = new TMVA::Reader();

      if( mvaCat == JC_SVC_0mu ) { 
        tmvaReader->AddVariable( "jet_jc",	&m_jc_mva );
        tmvaReader->AddVariable( "jet_svc", 	&m_svc_mva );
        tmvaReader->AddVariable( "trk_ngood", 	&m_ngoodtrk_mva );
        tmvaReader->AddVariable( "sv_ntrk",	&m_sv_trk_mva );
        tmvaReader->AddVariable( "sv_compPV", 	&m_sv_comp_mva );
        tmvaReader->AddVariable( "sv_distPV",  	&m_sv_dist_mva );
        tmvaReader->AddVariable( "sv_err", 	&m_sv_err_mva );
        tmvaReader->AddVariable( "sv_chi2", 	&m_sv_chi2_mva );
      }
      else if( mvaCat == JC_SVC_1mu ) {
        tmvaReader->AddVariable( "jet_jc",	&m_jc_mva );
        tmvaReader->AddVariable( "jet_svc", 	&m_svc_mva );
        tmvaReader->AddVariable( "trk_ngood", 	&m_ngoodtrk_mva );
        tmvaReader->AddVariable( "sv_ntrk", 	&m_sv_trk_mva );
        tmvaReader->AddVariable( "sv_compPV", 	&m_sv_comp_mva );
        tmvaReader->AddVariable( "sv_distPV", 	&m_sv_dist_mva );
        tmvaReader->AddVariable( "sv_err",  	&m_sv_err_mva );
        tmvaReader->AddVariable( "sv_chi2",  	&m_sv_chi2_mva );
        tmvaReader->AddVariable( "mu1_charge",  	&m_mu_charge_mva );
        tmvaReader->AddVariable( "mu1_vtx",  	&m_mu_vtx_mva );
        tmvaReader->AddVariable( "mu1_ptRel/1000.",	&m_mu_ptRel_mva );
        tmvaReader->AddVariable( "mu1_ptLong/1000.", 	&m_mu_ptLong_mva );
      }
      else if( mvaCat == JC_SVC_TVC_0mu ) {
        tmvaReader->AddVariable( "jet_jc",	&m_jc_mva );
        tmvaReader->AddVariable( "jet_svc+jet_tvc",    &m_sum_mva );
        tmvaReader->AddVariable( "jet_svc-jet_tvc",    &m_diff_mva );  
        tmvaReader->AddVariable( "trk_ngood",	&m_ngoodtrk_mva );
        tmvaReader->AddVariable( "sv_ntrk",  	&m_sv_trk_mva );
        tmvaReader->AddVariable( "sv_compPV", 	&m_sv_comp_mva );
        tmvaReader->AddVariable( "sv_distPV", 	&m_sv_dist_mva );
        tmvaReader->AddVariable( "sv_err", 	&m_sv_err_mva );
        tmvaReader->AddVariable( "sv_chi2",  	&m_sv_chi2_mva );
        tmvaReader->AddVariable( "tv_ntrk",  	&m_tv_trk_mva );
        tmvaReader->AddVariable( "tv_compPV", 	&m_tv_comp_mva );
        tmvaReader->AddVariable( "tv_distPV",  	&m_tv_dist_mva );
        tmvaReader->AddVariable( "tv_err", 	&m_tv_err_mva );
        tmvaReader->AddVariable( "tv_chi2",  	&m_tv_chi2_mva );
      }
      else if(mvaCat == JC_SVC_TVC_1mu) {	
        tmvaReader->AddVariable( "jet_jc",	&m_jc_mva );
        tmvaReader->AddVariable( "jet_svc+jet_tvc",    &m_sum_mva );
        tmvaReader->AddVariable( "jet_svc-jet_tvc",    &m_diff_mva );
        tmvaReader->AddVariable( "trk_ngood", 	&m_ngoodtrk_mva );
        tmvaReader->AddVariable( "sv_ntrk",  	&m_sv_trk_mva );
        tmvaReader->AddVariable( "sv_compPV",  	&m_sv_comp_mva );
        tmvaReader->AddVariable( "sv_distPV",  	&m_sv_dist_mva );
        tmvaReader->AddVariable( "sv_err",  	&m_sv_err_mva );
        tmvaReader->AddVariable( "sv_chi2",  	&m_sv_chi2_mva );
        tmvaReader->AddVariable( "tv_ntrk",  	&m_tv_trk_mva );
        tmvaReader->AddVariable( "tv_compPV",  	&m_tv_comp_mva );
        tmvaReader->AddVariable( "tv_distPV",  	&m_tv_dist_mva );
        tmvaReader->AddVariable( "tv_err",  	&m_tv_err_mva );
        tmvaReader->AddVariable( "tv_chi2",  	&m_tv_chi2_mva );
        tmvaReader->AddVariable( "mu1_charge",  	&m_mu_charge_mva );
        tmvaReader->AddVariable( "mu1_vtx",  	&m_mu_vtx_mva );
        tmvaReader->AddVariable( "mu1_ptRel/1000.",    &m_mu_ptRel_mva );
        tmvaReader->AddVariable( "mu1_ptLong/1000.",   &m_mu_ptLong_mva );
      }


      TMVA::IMethod* method= tmvaReader->BookMVA(TMVA::Types::kMLP, iss.str().data());  
      kl = dynamic_cast<TMVA::MethodBase*>(method);

      // add it or overwrite it in the map of readers:
      pos = m_tmvaReaders.find(alias);
      if(pos!=m_tmvaReaders.end()) {
        delete pos->second;
        m_tmvaReaders.erase(pos);
      }
      itmap = m_tmvaMethod.find(alias);
      if(itmap!=m_tmvaMethod.end()) {
        delete itmap->second;
        m_tmvaMethod.erase(itmap);
      }

      m_tmvaReaders.insert( std::make_pair( alias, tmvaReader ) );
      m_tmvaMethod.insert( std::make_pair( alias, kl ) ); 

   }


    //Now assign the value at the variables

    m_jc_mva = jetCharge;
    m_svc_mva = jf_svc;
    m_tvc_mva = jf_tvc;
    m_sum_mva = jf_svc + jf_tvc;
    m_diff_mva = jf_svc - jf_tvc;

    m_ngoodtrk_mva = ngoodtrk;

    m_sv_trk_mva = ntrk_sv;
    m_sv_comp_mva = comp_SV;
    m_sv_dist_mva = dist_SV;
    m_sv_err_mva = err_SV;
    m_sv_chi2_mva = chi2_SV;

    m_tv_trk_mva = ntrk_tv;
    m_tv_comp_mva = comp_TV;
    m_tv_dist_mva = dist_TV;
    m_tv_err_mva = err_TV;
    m_tv_chi2_mva = chi2_TV;

    m_mu_charge_mva = mu_charge;
    m_mu_vtx_mva = mu_vtx;
    m_mu_ptRel_mva = mu_ptRel/1000.;
    m_mu_ptLong_mva = mu_ptLong/1000.;



    //Finally compute the weight 
    float mvaWeight = -9.;
    std::map<std::string, TMVA::Reader*>::iterator pos2 = m_tmvaReaders.find(alias);
    if(pos2==m_tmvaReaders.end()) {
       int alreadyWarned = std::count(m_undefinedReaders.begin(),m_undefinedReaders.end(),alias);
       if(0==alreadyWarned) {
         ATH_MSG_WARNING("#BTAG# no TMVAReader defined for jet collection " << alias);
         m_undefinedReaders.push_back(alias);
       }
    }
    else {
       std::map<std::string, TMVA::MethodBase*>::iterator itmap2 = m_tmvaMethod.find(alias);
       if((itmap2->second)!=0){
         mvaWeight = pos2->second->EvaluateMVA( itmap2->second ); 
       } else ATH_MSG_WARNING("#BTAG#  kl==0"); 
    }


      //Now I compute the probability
      float prob  = probability( mvaCat, mvaWeight , author, alias);
      BTag->setVariable<float>(m_taggerNameBase, "discriminant", prob );

    }


    return StatusCode::SUCCESS;

}

/************    Helper functions   **********************/

bool JetVertexCharge::passTrackCuts( const xAOD::TrackParticle &track) const {


   double m_d0 = track.d0();
   double m_z0 = track.z0();
   double m_theta = track.theta();
   double chi2 = track.chiSquared() / track.numberDoF();
   double deltaZ0 = fabs( m_z0 - m_primVtx->z() + track.vz() );


   if( fabs(m_d0) > m_Trkd0Cut)  return false;
   if( deltaZ0*sin(m_theta) > m_Trkz0Cut) return false; 
   if( track.pt() < m_TrkPtCut) return false;
   if( fabs(track.eta()) > 2.5 ) return false;
   if( chi2 > m_TrkChi2Cut) return false;

 

   uint8_t PixelHits = 0;
   if( !(track.summaryValue( PixelHits, xAOD::numberOfPixelHits)) || (PixelHits < m_CutPixelHits)  )  return false;  
   uint8_t SCTHits = 0;
   if( !(track.summaryValue( SCTHits, xAOD::numberOfSCTHits)) || (SCTHits < m_CutSCTHits)  )  return false; 

   if( (PixelHits + SCTHits) < m_CutPrecisionHits) return false; 

   uint8_t TRTHits = 0;
   if( !(track.summaryValue( TRTHits, xAOD::numberOfTRTHits)) || (TRTHits < m_CutTRTHits)  )  return false; 

   uint8_t BLayerHits = 0; 
   if( !(track.summaryValue( BLayerHits, xAOD::numberOfBLayerHits)) || (BLayerHits < m_CutBLayerHits)  )  return false;

   uint8_t BLayerSharedHits = 0;
   if( !(track.summaryValue( BLayerSharedHits, xAOD::numberOfBLayerSharedHits))) return false;
   uint8_t PixelSharedHits = 0;
   if( !(track.summaryValue( PixelSharedHits, xAOD::numberOfPixelSharedHits)))  return false;
   uint8_t SCTSharedHits = 0;
   if( !(track.summaryValue( SCTSharedHits, xAOD::numberOfSCTSharedHits)))  return false; 
      
   if( ( BLayerSharedHits + PixelSharedHits + SCTSharedHits )  > m_CutSharedHits) return false;


   return true;

}

//////////////////////////////////////////////// 

int JetVertexCharge::category( float jc, float svc, float tvc, int mu ) {

   if( jc > -2 && svc > -2 && tvc <-2 && mu <0.5 ) return JC_SVC_0mu; 
   else if( jc > -2 && svc > -2 && tvc < -2 && mu >0.5 ) return JC_SVC_1mu;  
   else if( jc > -2 && svc > -2 && tvc > -2 && mu < 0.5 ) return JC_SVC_TVC_0mu;  
   else if( jc > -2 && svc > -2 && tvc > -2 && mu > 0.5 ) return JC_SVC_TVC_1mu;  
   else if( jc < -2 && svc > -2 ) return SVC;  
   else if( jc > -2 && svc < -2 ) return JC;  
   else return -1;  

}

//////////////////////////////////////////////////////
float  JetVertexCharge::probability( int mvaCat, float mvaWeight, std::string author, std::string alias ) {

  std::pair<TH1*,bool> histo_pos;
  std::pair<TH1*,bool> histo_neg;
  //The order takes into accont the population of each cateogory, to speed up the running time 
  if( mvaCat == JC) {
    histo_pos = m_calibrationTool->retrieveHistogram(m_taggerNameBase, author, "jvc_JC_x_bbar"); 
    histo_neg = m_calibrationTool->retrieveHistogram(m_taggerNameBase, author, "jvc_JC_x_b"); 
  }
  else if(mvaCat == -1) {
    return -3; 
  }
  else if( mvaCat == JC_SVC_0mu) { 
    histo_pos = m_calibrationTool->retrieveHistogram(m_taggerNameBase, author, "jvc_JC_SVC_noMu_bbar"); 
    histo_neg = m_calibrationTool->retrieveHistogram(m_taggerNameBase, author, "jvc_JC_SVC_noMu_b"); 
  }
  else if( mvaCat == JC_SVC_1mu) {
    histo_pos = m_calibrationTool->retrieveHistogram(m_taggerNameBase, author, "jvc_JC_SVC_incMu_bbar"); 
    histo_neg = m_calibrationTool->retrieveHistogram(m_taggerNameBase, author, "jvc_JC_SVC_incMu_b"); 
  }
  else if( mvaCat == JC_SVC_TVC_0mu) {
    histo_pos = m_calibrationTool->retrieveHistogram(m_taggerNameBase, author, "jvc_JC_SVC_TVC_noMu_bbar"); 
    histo_neg = m_calibrationTool->retrieveHistogram(m_taggerNameBase, author, "jvc_JC_SVC_TVC_noMu_b"); 
  }
  else if( mvaCat == JC_SVC_TVC_1mu) {
    histo_pos = m_calibrationTool->retrieveHistogram(m_taggerNameBase, author, "jvc_JC_SVC_TVC_incMu_bbar"); 
    histo_neg = m_calibrationTool->retrieveHistogram(m_taggerNameBase, author, "jvc_JC_SVC_TVC_incMu_b"); 
  }
  else if( mvaCat == SVC) {
    histo_pos = m_calibrationTool->retrieveHistogram(m_taggerNameBase, author, "jvc_SVC_x_bbar"); 
    histo_neg = m_calibrationTool->retrieveHistogram(m_taggerNameBase, author, "jvc_SVC_x_b"); 
  }

  bool histosHaveChanged = (histo_pos.second || histo_neg.second); 
  if(histosHaveChanged) {

    if( histo_pos.first ==NULL ) {
      ATH_MSG_WARNING("#BTAG# HISTO POS can't be retrieved -> no calibration for "<< m_taggerNameBase );
      return -3.; 
    }
    if(  histo_neg.first==NULL) {
      ATH_MSG_WARNING("#BTAG# HISTO NEG can't be retrieved -> no calibration for "<< m_taggerNameBase );
      return -3;
    }

    if( mvaCat == JC) {
      m_calibrationTool->updateHistogramStatus(m_taggerNameBase, alias, "jvc_JC_x_bbar", false);
      m_calibrationTool->updateHistogramStatus(m_taggerNameBase, alias, "jvc_JC_x_noMu", false);
    }
    else if( mvaCat == JC_SVC_0mu) {
      m_calibrationTool->updateHistogramStatus(m_taggerNameBase, alias, "jvc_JC_SVC_noMu_bbar", false);
      m_calibrationTool->updateHistogramStatus(m_taggerNameBase, alias, "jvc_JC_SVC_noMu_b", false);
    }
    else if( mvaCat == JC_SVC_1mu) {
      m_calibrationTool->updateHistogramStatus(m_taggerNameBase, alias, "jvc_JC_SVC_incMu_bbar", false);
      m_calibrationTool->updateHistogramStatus(m_taggerNameBase, alias, "jvc_JC_SVC_incMu_b", false);
    }
    else if( mvaCat == JC_SVC_TVC_0mu) {	
      m_calibrationTool->updateHistogramStatus(m_taggerNameBase, alias, "jvc_JC_SVC_TVC_noMu_bbar", false);
      m_calibrationTool->updateHistogramStatus(m_taggerNameBase, alias, "jvc_JC_SVC_TVC_noMu_b", false);
    }
    else if( mvaCat == JC_SVC_TVC_1mu) {
      m_calibrationTool->updateHistogramStatus(m_taggerNameBase, alias, "jvc_JC_SVC_TVC_incMu_bbar", false);
      m_calibrationTool->updateHistogramStatus(m_taggerNameBase, alias, "jvc_JC_SVC_TVC_incMu_b", false);
    }
    else if( mvaCat == SVC) {	
      m_calibrationTool->updateHistogramStatus(m_taggerNameBase, alias, "jvc_SVC_x_bbar", false);
      m_calibrationTool->updateHistogramStatus(m_taggerNameBase, alias, "jvc_SVC_x_b", false);
    }


    TH1F* hp = (TH1F*) histo_pos.first; 
    TH1F* hn = (TH1F*) histo_neg.first; 

    std::map<int, TH1F*>::iterator pos;
    std::map<int, TH1F*>::iterator neg;

    pos = m_histoList_pos.find(mvaCat); 
    if(pos!=m_histoList_pos.end()) {
      m_histoList_pos.erase(pos);
    }
    neg = m_histoList_neg.find(mvaCat); 
    if(neg!=m_histoList_neg.end()) {
      m_histoList_neg.erase(neg);
    }

    m_histoList_pos.insert( std::make_pair( mvaCat, hp ) ); 
    m_histoList_neg.insert( std::make_pair( mvaCat, hn ) );

  }  //if something changed


  float posProb = 0.;
  float negProb = 0.;

  std::map<int, TH1F*>::iterator itmap_pos = m_histoList_pos.find(mvaCat); 
  if (itmap_pos != m_histoList_pos.end() && itmap_pos->second != 0) {
    TH1F * hhh  = (TH1F*) itmap_pos->second; 
    int bin = hhh->FindBin( mvaWeight );
    posProb = hhh->Integral( 0, bin) ; 
  } 

  std::map<int, TH1F*>::iterator itmap_neg = m_histoList_neg.find(mvaCat);
  if (itmap_neg != m_histoList_neg.end() && itmap_neg->second != 0) {
    TH1F * hhh  = (TH1F*) itmap_neg->second; 
    int bin = hhh->FindBin( mvaWeight );
    negProb = 1 - hhh->Integral( 0, bin) ; 
  }

  return (posProb + negProb > 0) ? posProb/(posProb + negProb) : -1;
}

}  //End of namespace
