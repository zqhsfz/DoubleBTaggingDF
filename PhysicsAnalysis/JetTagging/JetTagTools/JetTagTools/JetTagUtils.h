#ifndef JETTAGTOOLS_JETTAGUTILS
#define JETTAGTOOLS_JETTAGUTILS
#include "xAODJet/Jet.h"
#include <string>

namespace JetTagUtils{

  std::string getJetAuthor(xAOD::Jet& jetToTag);

}
#endif
