kpatch-test-rpm-spec
====================

A minimal rpm spec for a livepatch module.

To build the RPM, first install kpatch and the rpm devtools, then setup your
tree:

    $ rpmdev-setuptree

Copy the patch into the sources directory:

    $ cp module-add-livepatch.patch ~/rpmbuild/SOURCES/

Then build the package:

    $ rpmbuild -bb kpatch-patch-add-version.spec
