/***************************************************************************
    @class MultiSVTag
 ***************************************************************************/

#ifndef JETTAGTOOLS_MULTISVTAG_H
#define JETTAGTOOLS_MULTISVTAG_H

#include "AthenaBaseComps/AthAlgTool.h"
#include "GaudiKernel/ToolHandle.h"
#include "JetTagTools/ITagTool.h"
#include "GeoPrimitives/GeoPrimitives.h"
#include "xAODTracking/TrackParticle.h"
#include "xAODTracking/TrackParticleContainer.h"
#include <string>
#include <vector>
#include <map>
#include <list>
#include "TMVA/IMethod.h"
#include "TMVA/MethodBase.h"
namespace TMVA { class Reader; }
namespace Analysis { class CalibrationBroker; }

//namespace xAOD { class TrackParticle; class TrackParticleContainer; }
//namespace Trk { class VxCandidate; class RecVertex;}
//class Jet;
//class StoreGateSvc;

namespace Analysis
{  
  
  class MultiSVTag : public AthAlgTool , virtual public ITagTool
    {
    public:
      MultiSVTag(const std::string&,const std::string&,const IInterface*);
      virtual ~MultiSVTag();
      StatusCode initialize();
      StatusCode finalize();      

      StatusCode tagJet(xAOD::Jet& jetToTag, xAOD::BTagging * BTag);
      void setOrigin(const xAOD::Vertex* priVtx);
      void finalizeHistos();
      
    private:      
      std::string m_taggerName; 
      std::string m_taggerNameBase;      
      //
      ToolHandle<CalibrationBroker> m_calibrationTool;
      std::string m_MultiSV;
      //
      std::string m_runModus; 
      std::string m_refType;
      const xAOD::Vertex* m_priVtx;
   
      std::vector<std::string> m_jetCollectionList;
      std::vector<std::string> m_hypotheses;
      bool m_doForcedCalib;
      std::string m_ForcedCalibName;
      std::string m_secVxFinderName;
      std::string m_xAODBaseName;
      //...
      //variables for bb tag
      float m_jetpt;
      float m_nvtx;
      float m_maxefrc;
      float m_summass;
      float m_totalntrk;
      float m_diffntrkSV0;
    
      float m_normDist;
      //properties of vertex with maximum (and 2nd max) mass:
      float m_mmax_mass ;
      float m_mmax_efrc ;
      
      float m_mmax_DRjet;
      float m_mmax_dist ;
      float m_mmx2_mass ; 
      float m_mmx2_efrc ;
     
      float m_mmx2_DRjet;
      float m_mmx2_dist ;
       // distances: max mass vertex to PV, and mx2 to max vertex
      float m_mx12_2d12 ; 
      float m_mx12_DR   ;
      float m_mx12_Angle;
      //...
      std::map<std::string, TMVA::Reader*> m_tmvaReaders;
      std::map<std::string, TMVA::MethodBase*> m_tmvaMethod; 
      std::list<std::string> m_undefinedReaders;
      std::string m_sv0_infosource;
    }; // End class


  inline void MultiSVTag::setOrigin(const xAOD::Vertex* priVtx) { m_priVtx = priVtx; }

} // End namespace 

#endif
