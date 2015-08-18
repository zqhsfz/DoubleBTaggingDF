# echo "cleanup DerivationFrameworkJetEtMiss DerivationFrameworkJetEtMiss-00-02-56 in /afs/cern.ch/work/q/qzeng/gbb/DerivationFramework/JETM8/20.1.5.7/PhysicsAnalysis/DerivationFramework"

if ( $?CMTROOT == 0 ) then
  setenv CMTROOT /cvmfs/atlas.cern.ch/repo/sw/software/x86_64-slc6-gcc48-opt/20.1.5/CMT/v1r25p20140131
endif
source ${CMTROOT}/mgr/setup.csh
set cmtDerivationFrameworkJetEtMisstempfile=`${CMTROOT}/${CMTBIN}/cmt.exe -quiet build temporary_name`
if $status != 0 then
  set cmtDerivationFrameworkJetEtMisstempfile=/tmp/cmt.$$
endif
${CMTROOT}/${CMTBIN}/cmt.exe cleanup -csh -pack=DerivationFrameworkJetEtMiss -version=DerivationFrameworkJetEtMiss-00-02-56 -path=/afs/cern.ch/work/q/qzeng/gbb/DerivationFramework/JETM8/20.1.5.7/PhysicsAnalysis/DerivationFramework  $* >${cmtDerivationFrameworkJetEtMisstempfile}
if ( $status != 0 ) then
  echo "${CMTROOT}/${CMTBIN}/cmt.exe cleanup -csh -pack=DerivationFrameworkJetEtMiss -version=DerivationFrameworkJetEtMiss-00-02-56 -path=/afs/cern.ch/work/q/qzeng/gbb/DerivationFramework/JETM8/20.1.5.7/PhysicsAnalysis/DerivationFramework  $* >${cmtDerivationFrameworkJetEtMisstempfile}"
  set cmtcleanupstatus=2
  /bin/rm -f ${cmtDerivationFrameworkJetEtMisstempfile}
  unset cmtDerivationFrameworkJetEtMisstempfile
  exit $cmtcleanupstatus
endif
set cmtcleanupstatus=0
source ${cmtDerivationFrameworkJetEtMisstempfile}
if ( $status != 0 ) then
  set cmtcleanupstatus=2
endif
/bin/rm -f ${cmtDerivationFrameworkJetEtMisstempfile}
unset cmtDerivationFrameworkJetEtMisstempfile
exit $cmtcleanupstatus

