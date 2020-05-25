#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gfbgraph
Version  : 0.2.4
Release  : 7
URL      : https://download.gnome.org/sources/gfbgraph/0.2/gfbgraph-0.2.4.tar.xz
Source0  : https://download.gnome.org/sources/gfbgraph/0.2/gfbgraph-0.2.4.tar.xz
Summary  : GObject library for Facebook Graph API
Group    : Development/Tools
License  : LGPL-2.1
Requires: gfbgraph-data = %{version}-%{release}
Requires: gfbgraph-lib = %{version}-%{release}
Requires: gfbgraph-license = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : docbook-xml
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(goa-1.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(json-glib-1.0)
BuildRequires : pkgconfig(libsoup-2.4)
BuildRequires : pkgconfig(rest-0.7)

%description
LibGFBGraph
===========
A GObject library for Facebook Graph API
This library is in a very early stage of development,
don't use in a final application right now. Use it just
for test purposes at your own risk.

%package data
Summary: data components for the gfbgraph package.
Group: Data

%description data
data components for the gfbgraph package.


%package dev
Summary: dev components for the gfbgraph package.
Group: Development
Requires: gfbgraph-lib = %{version}-%{release}
Requires: gfbgraph-data = %{version}-%{release}
Provides: gfbgraph-devel = %{version}-%{release}
Requires: gfbgraph = %{version}-%{release}

%description dev
dev components for the gfbgraph package.


%package lib
Summary: lib components for the gfbgraph package.
Group: Libraries
Requires: gfbgraph-data = %{version}-%{release}
Requires: gfbgraph-license = %{version}-%{release}

%description lib
lib components for the gfbgraph package.


%package license
Summary: license components for the gfbgraph package.
Group: Default

%description license
license components for the gfbgraph package.


%prep
%setup -q -n gfbgraph-0.2.4
cd %{_builddir}/gfbgraph-0.2.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1590422600
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%autogen --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1590422600
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gfbgraph
cp %{_builddir}/gfbgraph-0.2.4/COPYING %{buildroot}/usr/share/package-licenses/gfbgraph/70e5b527a568a6a75b977976e2d392fadf9bd84a
%make_install

%files
%defattr(-,root,root,-)
/usr/doc/libgfbgraph/AUTHORS
/usr/doc/libgfbgraph/COPYING
/usr/doc/libgfbgraph/ChangeLog
/usr/doc/libgfbgraph/INSTALL
/usr/doc/libgfbgraph/NEWS
/usr/doc/libgfbgraph/README

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/GFBGraph-0.2.typelib
/usr/share/gir-1.0/*.gir

%files dev
%defattr(-,root,root,-)
/usr/include/gfbgraph-0.2/gfbgraph/gfbgraph-album.h
/usr/include/gfbgraph-0.2/gfbgraph/gfbgraph-authorizer.h
/usr/include/gfbgraph-0.2/gfbgraph/gfbgraph-common.h
/usr/include/gfbgraph-0.2/gfbgraph/gfbgraph-connectable.h
/usr/include/gfbgraph-0.2/gfbgraph/gfbgraph-goa-authorizer.h
/usr/include/gfbgraph-0.2/gfbgraph/gfbgraph-node.h
/usr/include/gfbgraph-0.2/gfbgraph/gfbgraph-photo.h
/usr/include/gfbgraph-0.2/gfbgraph/gfbgraph-simple-authorizer.h
/usr/include/gfbgraph-0.2/gfbgraph/gfbgraph-user.h
/usr/include/gfbgraph-0.2/gfbgraph/gfbgraph.h
/usr/lib64/libgfbgraph-0.2.so
/usr/lib64/pkgconfig/libgfbgraph-0.2.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgfbgraph-0.2.so.0
/usr/lib64/libgfbgraph-0.2.so.0.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gfbgraph/70e5b527a568a6a75b977976e2d392fadf9bd84a
