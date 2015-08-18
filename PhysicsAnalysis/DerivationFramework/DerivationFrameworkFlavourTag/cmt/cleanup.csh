# echo "cleanup DerivationFrameworkFlavourTag DerivationFrameworkFlavourTag-00-01-26 in /afs/cern.ch/work/q/qzeng/gbb/DerivationFramework/JETM8/20.1.5.7/PhysicsAnalysis/DerivationFramework"

if ( $?CMTROOT == 0 ) then
  setenv CMTROOT /cvmfs/atlas.cern.ch/repo/sw/software/x86_64-slc6-gcc48-opt/20.1.5/CMT/v1r25p20140131
endif
source ${CMTROOT}/mgr/setup.csh
set cmtDerivationFrameworkFlavourTagtempfile=`${CMTROOT}/${CMTBIN}/cmt.exe -quiet build temporary_name`
if $status != 0 then
  set cmtDerivationFrameworkFlavourTagtempfile=/tmp/cmt.$$
endif
${CMTROOT}/${CMTBIN}/cmt.exe cleanup -csh -pack=DerivationFrameworkFlavourTag -version=DerivationFrameworkFlavourTag-00-01-26 -path=/afs/cern.ch/work/q/qzeng/gbb/DerivationFramework/JETM8/20.1.5.7/PhysicsAnalysis/DerivationFramework  $* >${cmtDerivationFrameworkFlavourTagtempfile}
if ( $status != 0 ) then
  echo "${CMTROOT}/${CMTBIN}/cmt.exe cleanup -csh -pack=DerivationFrameworkFlavourTag -version=DerivationFrameworkFlavourTag-00-01-26 -path=/afs/cern.ch/work/q/qzeng/gbb/DerivationFramework/JETM8/20.1.5.7/PhysicsAnalysis/DerivationFramework  $* >${cmtDerivationFrameworkFlavourTagtempfile}"
  set cmtcleanupstatus=2
  /bin/rm -f ${cmtDerivationFrameworkFlavourTagtempfile}
  unset cmtDerivationFrameworkFlavourTagtempfile
  exit $cmtcleanupstatus
endif
set cmtcleanupstatus=0
source ${cmtDerivationFrameworkFlavourTagtempfile}
if ( $status != 0 ) then
  set cmtcleanupstatus=2
endif
/bin/rm -f ${cmtDerivationFrameworkFlavourTagtempfile}
unset cmtDerivationFrameworkFlavourTagtempfile
exit $cmtcleanupstatus

