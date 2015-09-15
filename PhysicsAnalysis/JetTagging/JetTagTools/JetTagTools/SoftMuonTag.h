#ifndef JETTAGTOOLS_SOFTMUONTAG_H
#define JETTAGTOOLS_SOFTMUONTAG_H
/********************************************************************
    @class SoftMuonTag
    PACKAGE : offline/PhysicsAnalysis/JetTagging/JetTagTools

   PURPOSE:  b-tagging based on soft muon identification
            In reference mode the significance is filled into a histogram.
   @author Henri.Bachacou@cern.ch
********************************************************************/
#include "AthenaBaseComps/AthAlgTool.h"
#include "GaudiKernel/ToolHandle.h"
#include <vector>
#include <map>
#include "JetTagTools/ITagTool.h"
#include "xAODTracking/TrackParticle.h"

namespace Trk  { class VxCandidate; }
namespace Reco { class ITrackToVertex; }
//class Jet;
namespace Analysis { class MuonContainer; }
class AnalysisTools;

namespace Analysis
{

  class SoftMuonInfo;
  class NewLikelihoodTool;
  //  class LikelihoodMultiDTool;
  class HistoHelperRoot;
  class CalibrationBroker;

  class SoftMuonTag : public AthAlgTool, virtual public ITagTool
  {
    public:
      SoftMuonTag(const std::string&,const std::string&,const IInterface*);

    /**
       Implementations of the methods defined in the abstract base class
    */
      virtual ~SoftMuonTag();
      StatusCode initialize();
      StatusCode finalize();
      
      /** Set the primary vertex. TODO: This is temporary ! The primary vertex should
	  be part of the JetTag IParticle interface implementation. The trouble with
	  ElementLink and persistency has to be solved for that. Revisit ... */
      void setOrigin(const Trk::VxCandidate* priVtx);
      
      void tagJet(xAOD::Jet& jetToTag);
      
      void finalizeHistos();
      
  private:
      
      /** TrackToVertex tool */
      ToolHandle< Reco::ITrackToVertex > m_trackToVertexTool;
      /** Likelihood tool */
      ToolHandle< NewLikelihoodTool > m_likelihoodTool;
      //      ToolHandle< LikelihoodMultiDTool > m_likelihoodTool;
      // Helpers...
      HistoHelperRoot* m_histoHelper;
      
      /** This switch is needed to indicate what to do. The algorithm can be run to produce
	  reference histograms from the given MC files (m_runModus=0) or to work in analysis mode
	  (m_runModus=1) where already made reference histograms are read.*/
      std::string    m_runModus;          // "analysis: read reference histos; reference: make reference histos
      std::string    m_refType;           // type jets (B, C, or L)
      std::string    m_algMode;           // type of algorithm (cuts, likelihood pt vs ptrel, combined, etc...)

      float m_pTjetmin;
      float m_etajetmin;

      bool m_checkOverflows;
      double m_purificationDeltaR;
      double m_muonIsolDeltaR;
      bool m_UseBinInterpol;

      /** Muon selection cuts */
      int m_alg;
      double m_d0cut;
      double m_pTcut;
      double m_DRcut;
      double m_MatchChi2cut;

      /** Storage for the primary vertex. Can be removed when JetTag provides origin(). */
      // this pointer does not need to be deleted in the destructor (because it
      // points to something in storegate)
      const Trk::VxCandidate* m_priVtx;

      /** just print some info at the beginning */
      void m_printParameterSettings();

      std::vector<std::string> m_jetCollectionList;
      std::vector<std::string> m_hypothese; // "b" or "c" or "l"
      std::vector<std::string> m_histoname; // list of histogram names

      bool m_doForcedCalib;
      std::string m_ForcedCalibName;

      bool m_writeInfoPlus;
      std::string m_originalMuCollectionName;
      std::string m_muonAssociationName;
      const MuonContainer* m_originalMuCollection;

  }; // End class
  inline void SoftMuonTag::setOrigin(const Trk::VxCandidate* priVtx) { m_priVtx=priVtx; }
} // End namespace

#endif
