# echo "setup DerivationFrameworkFlavourTag DerivationFrameworkFlavourTag-00-01-26 in /afs/cern.ch/work/q/qzeng/gbb/DerivationFramework/JETM8/20.1.5.7/PhysicsAnalysis/DerivationFramework"

if test "${CMTROOT}" = ""; then
  CMTROOT=/cvmfs/atlas.cern.ch/repo/sw/software/x86_64-slc6-gcc48-opt/20.1.5/CMT/v1r25p20140131; export CMTROOT
fi
. ${CMTROOT}/mgr/setup.sh
cmtDerivationFrameworkFlavourTagtempfile=`${CMTROOT}/${CMTBIN}/cmt.exe -quiet build temporary_name`
if test ! $? = 0 ; then cmtDerivationFrameworkFlavourTagtempfile=/tmp/cmt.$$; fi
${CMTROOT}/${CMTBIN}/cmt.exe setup -sh -pack=DerivationFrameworkFlavourTag -version=DerivationFrameworkFlavourTag-00-01-26 -path=/afs/cern.ch/work/q/qzeng/gbb/DerivationFramework/JETM8/20.1.5.7/PhysicsAnalysis/DerivationFramework  -no_cleanup $* >${cmtDerivationFrameworkFlavourTagtempfile}
if test $? != 0 ; then
  echo >&2 "${CMTROOT}/${CMTBIN}/cmt.exe setup -sh -pack=DerivationFrameworkFlavourTag -version=DerivationFrameworkFlavourTag-00-01-26 -path=/afs/cern.ch/work/q/qzeng/gbb/DerivationFramework/JETM8/20.1.5.7/PhysicsAnalysis/DerivationFramework  -no_cleanup $* >${cmtDerivationFrameworkFlavourTagtempfile}"
  cmtsetupstatus=2
  /bin/rm -f ${cmtDerivationFrameworkFlavourTagtempfile}
  unset cmtDerivationFrameworkFlavourTagtempfile
  return $cmtsetupstatus
fi
cmtsetupstatus=0
. ${cmtDerivationFrameworkFlavourTagtempfile}
if test $? != 0 ; then
  cmtsetupstatus=2
fi
/bin/rm -f ${cmtDerivationFrameworkFlavourTagtempfile}
unset cmtDerivationFrameworkFlavourTagtempfile
return $cmtsetupstatus

