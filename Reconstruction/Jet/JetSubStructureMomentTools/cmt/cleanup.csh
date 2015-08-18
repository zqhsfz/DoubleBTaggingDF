# echo "cleanup JetSubStructureMomentTools JetSubStructureMomentTools-00-01-21 in /afs/cern.ch/work/q/qzeng/gbb/DerivationFramework/JETM8/20.1.5.7/Reconstruction/Jet"

if ( $?CMTROOT == 0 ) then
  setenv CMTROOT /cvmfs/atlas.cern.ch/repo/sw/software/x86_64-slc6-gcc48-opt/20.1.5/CMT/v1r25p20140131
endif
source ${CMTROOT}/mgr/setup.csh
set cmtJetSubStructureMomentToolstempfile=`${CMTROOT}/${CMTBIN}/cmt.exe -quiet build temporary_name`
if $status != 0 then
  set cmtJetSubStructureMomentToolstempfile=/tmp/cmt.$$
endif
${CMTROOT}/${CMTBIN}/cmt.exe cleanup -csh -pack=JetSubStructureMomentTools -version=JetSubStructureMomentTools-00-01-21 -path=/afs/cern.ch/work/q/qzeng/gbb/DerivationFramework/JETM8/20.1.5.7/Reconstruction/Jet  $* >${cmtJetSubStructureMomentToolstempfile}
if ( $status != 0 ) then
  echo "${CMTROOT}/${CMTBIN}/cmt.exe cleanup -csh -pack=JetSubStructureMomentTools -version=JetSubStructureMomentTools-00-01-21 -path=/afs/cern.ch/work/q/qzeng/gbb/DerivationFramework/JETM8/20.1.5.7/Reconstruction/Jet  $* >${cmtJetSubStructureMomentToolstempfile}"
  set cmtcleanupstatus=2
  /bin/rm -f ${cmtJetSubStructureMomentToolstempfile}
  unset cmtJetSubStructureMomentToolstempfile
  exit $cmtcleanupstatus
endif
set cmtcleanupstatus=0
source ${cmtJetSubStructureMomentToolstempfile}
if ( $status != 0 ) then
  set cmtcleanupstatus=2
endif
/bin/rm -f ${cmtJetSubStructureMomentToolstempfile}
unset cmtJetSubStructureMomentToolstempfile
exit $cmtcleanupstatus

