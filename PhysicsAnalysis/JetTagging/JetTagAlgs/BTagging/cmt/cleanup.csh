# echo "cleanup BTagging BTagging-00-07-43 in /afs/cern.ch/work/q/qzeng/gbb/DerivationFramework/JETM8/20.1.5.7/PhysicsAnalysis/JetTagging/JetTagAlgs"

if ( $?CMTROOT == 0 ) then
  setenv CMTROOT /cvmfs/atlas.cern.ch/repo/sw/software/x86_64-slc6-gcc48-opt/20.1.5/CMT/v1r25p20140131
endif
source ${CMTROOT}/mgr/setup.csh
set cmtBTaggingtempfile=`${CMTROOT}/${CMTBIN}/cmt.exe -quiet build temporary_name`
if $status != 0 then
  set cmtBTaggingtempfile=/tmp/cmt.$$
endif
${CMTROOT}/${CMTBIN}/cmt.exe cleanup -csh -pack=BTagging -version=BTagging-00-07-43 -path=/afs/cern.ch/work/q/qzeng/gbb/DerivationFramework/JETM8/20.1.5.7/PhysicsAnalysis/JetTagging/JetTagAlgs  $* >${cmtBTaggingtempfile}
if ( $status != 0 ) then
  echo "${CMTROOT}/${CMTBIN}/cmt.exe cleanup -csh -pack=BTagging -version=BTagging-00-07-43 -path=/afs/cern.ch/work/q/qzeng/gbb/DerivationFramework/JETM8/20.1.5.7/PhysicsAnalysis/JetTagging/JetTagAlgs  $* >${cmtBTaggingtempfile}"
  set cmtcleanupstatus=2
  /bin/rm -f ${cmtBTaggingtempfile}
  unset cmtBTaggingtempfile
  exit $cmtcleanupstatus
endif
set cmtcleanupstatus=0
source ${cmtBTaggingtempfile}
if ( $status != 0 ) then
  set cmtcleanupstatus=2
endif
/bin/rm -f ${cmtBTaggingtempfile}
unset cmtBTaggingtempfile
exit $cmtcleanupstatus

