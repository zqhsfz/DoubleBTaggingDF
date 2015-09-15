# echo "setup BTagging BTagging-00-07-43 in /afs/cern.ch/work/q/qzeng/gbb/DerivationFramework/JETM8/20.1.5.7/PhysicsAnalysis/JetTagging/JetTagAlgs"

if test "${CMTROOT}" = ""; then
  CMTROOT=/cvmfs/atlas.cern.ch/repo/sw/software/x86_64-slc6-gcc48-opt/20.1.5/CMT/v1r25p20140131; export CMTROOT
fi
. ${CMTROOT}/mgr/setup.sh
cmtBTaggingtempfile=`${CMTROOT}/${CMTBIN}/cmt.exe -quiet build temporary_name`
if test ! $? = 0 ; then cmtBTaggingtempfile=/tmp/cmt.$$; fi
${CMTROOT}/${CMTBIN}/cmt.exe setup -sh -pack=BTagging -version=BTagging-00-07-43 -path=/afs/cern.ch/work/q/qzeng/gbb/DerivationFramework/JETM8/20.1.5.7/PhysicsAnalysis/JetTagging/JetTagAlgs  -no_cleanup $* >${cmtBTaggingtempfile}
if test $? != 0 ; then
  echo >&2 "${CMTROOT}/${CMTBIN}/cmt.exe setup -sh -pack=BTagging -version=BTagging-00-07-43 -path=/afs/cern.ch/work/q/qzeng/gbb/DerivationFramework/JETM8/20.1.5.7/PhysicsAnalysis/JetTagging/JetTagAlgs  -no_cleanup $* >${cmtBTaggingtempfile}"
  cmtsetupstatus=2
  /bin/rm -f ${cmtBTaggingtempfile}
  unset cmtBTaggingtempfile
  return $cmtsetupstatus
fi
cmtsetupstatus=0
. ${cmtBTaggingtempfile}
if test $? != 0 ; then
  cmtsetupstatus=2
fi
/bin/rm -f ${cmtBTaggingtempfile}
unset cmtBTaggingtempfile
return $cmtsetupstatus

