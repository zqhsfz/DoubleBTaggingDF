# echo "cleanup JetTagTools JetTagTools-01-00-54 in /afs/cern.ch/work/q/qzeng/gbb/DerivationFramework/JETM8/20.1.5.7/PhysicsAnalysis/JetTagging"

if ( $?CMTROOT == 0 ) then
  setenv CMTROOT /cvmfs/atlas.cern.ch/repo/sw/software/x86_64-slc6-gcc48-opt/20.1.5/CMT/v1r25p20140131
endif
source ${CMTROOT}/mgr/setup.csh
set cmtJetTagToolstempfile=`${CMTROOT}/${CMTBIN}/cmt.exe -quiet build temporary_name`
if $status != 0 then
  set cmtJetTagToolstempfile=/tmp/cmt.$$
endif
${CMTROOT}/${CMTBIN}/cmt.exe cleanup -csh -pack=JetTagTools -version=JetTagTools-01-00-54 -path=/afs/cern.ch/work/q/qzeng/gbb/DerivationFramework/JETM8/20.1.5.7/PhysicsAnalysis/JetTagging  $* >${cmtJetTagToolstempfile}
if ( $status != 0 ) then
  echo "${CMTROOT}/${CMTBIN}/cmt.exe cleanup -csh -pack=JetTagTools -version=JetTagTools-01-00-54 -path=/afs/cern.ch/work/q/qzeng/gbb/DerivationFramework/JETM8/20.1.5.7/PhysicsAnalysis/JetTagging  $* >${cmtJetTagToolstempfile}"
  set cmtcleanupstatus=2
  /bin/rm -f ${cmtJetTagToolstempfile}
  unset cmtJetTagToolstempfile
  exit $cmtcleanupstatus
endif
set cmtcleanupstatus=0
source ${cmtJetTagToolstempfile}
if ( $status != 0 ) then
  set cmtcleanupstatus=2
endif
/bin/rm -f ${cmtJetTagToolstempfile}
unset cmtJetTagToolstempfile
exit $cmtcleanupstatus

