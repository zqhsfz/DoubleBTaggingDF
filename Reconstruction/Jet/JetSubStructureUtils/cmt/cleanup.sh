# echo "cleanup JetSubStructureUtils JetSubStructureUtils-00-02-12 in /afs/cern.ch/work/q/qzeng/gbb/DerivationFramework/JETM8/20.1.5.7/Reconstruction/Jet"

if test "${CMTROOT}" = ""; then
  CMTROOT=/cvmfs/atlas.cern.ch/repo/sw/software/x86_64-slc6-gcc48-opt/20.1.5/CMT/v1r25p20140131; export CMTROOT
fi
. ${CMTROOT}/mgr/setup.sh
cmtJetSubStructureUtilstempfile=`${CMTROOT}/${CMTBIN}/cmt.exe -quiet build temporary_name`
if test ! $? = 0 ; then cmtJetSubStructureUtilstempfile=/tmp/cmt.$$; fi
${CMTROOT}/${CMTBIN}/cmt.exe cleanup -sh -pack=JetSubStructureUtils -version=JetSubStructureUtils-00-02-12 -path=/afs/cern.ch/work/q/qzeng/gbb/DerivationFramework/JETM8/20.1.5.7/Reconstruction/Jet  $* >${cmtJetSubStructureUtilstempfile}
if test $? != 0 ; then
  echo >&2 "${CMTROOT}/${CMTBIN}/cmt.exe cleanup -sh -pack=JetSubStructureUtils -version=JetSubStructureUtils-00-02-12 -path=/afs/cern.ch/work/q/qzeng/gbb/DerivationFramework/JETM8/20.1.5.7/Reconstruction/Jet  $* >${cmtJetSubStructureUtilstempfile}"
  cmtcleanupstatus=2
  /bin/rm -f ${cmtJetSubStructureUtilstempfile}
  unset cmtJetSubStructureUtilstempfile
  return $cmtcleanupstatus
fi
cmtcleanupstatus=0
. ${cmtJetSubStructureUtilstempfile}
if test $? != 0 ; then
  cmtcleanupstatus=2
fi
/bin/rm -f ${cmtJetSubStructureUtilstempfile}
unset cmtJetSubStructureUtilstempfile
return $cmtcleanupstatus

