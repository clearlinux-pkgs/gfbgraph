#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gfbgraph
Version  : 0.2.5
Release  : 13
URL      : https://download.gnome.org/sources/gfbgraph/0.2/gfbgraph-0.2.5.tar.xz
Source0  : https://download.gnome.org/sources/gfbgraph/0.2/gfbgraph-0.2.5.tar.xz
Summary  : GObject library for Facebook Graph API
Group    : Development/Tools
License  : LGPL-2.1
Requires: gfbgraph-data = %{version}-%{release}
Requires: gfbgraph-lib = %{version}-%{release}
Requires: gfbgraph-license = %{version}-%{release}
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : buildreq-gnome
BuildRequires : docbook-xml
BuildRequires : gettext-bin
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : libxslt-bin
BuildRequires : m4
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(goa-1.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(json-glib-1.0)
BuildRequires : pkgconfig(libsoup-2.4)
BuildRequires : pkgconfig(rest-0.7)
Patch1: 0001-Fix-doc-dir-location.patch

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


%package doc
Summary: doc components for the gfbgraph package.
Group: Documentation

%description doc
doc components for the gfbgraph package.


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
%setup -q -n gfbgraph-0.2.5
cd %{_builddir}/gfbgraph-0.2.5
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1664145310
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%reconfigure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1664145310
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gfbgraph
cp %{_builddir}/gfbgraph-%{version}/COPYING %{buildroot}/usr/share/package-licenses/gfbgraph/70e5b527a568a6a75b977976e2d392fadf9bd84a || :
%make_install

%files
%defattr(-,root,root,-)

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

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/libgfbgraph/AUTHORS
/usr/share/doc/libgfbgraph/COPYING
/usr/share/doc/libgfbgraph/ChangeLog
/usr/share/doc/libgfbgraph/INSTALL
/usr/share/doc/libgfbgraph/NEWS
/usr/share/doc/libgfbgraph/README
/usr/share/gtk-doc/html/gfbgraph-0.2/GFBGraphAlbum.html
/usr/share/gtk-doc/html/gfbgraph-0.2/GFBGraphGoaAuthorizer.html
/usr/share/gtk-doc/html/gfbgraph-0.2/GFBGraphNode.html
/usr/share/gtk-doc/html/gfbgraph-0.2/GFBGraphPhoto.html
/usr/share/gtk-doc/html/gfbgraph-0.2/GFBGraphSimpleAuthorizer.html
/usr/share/gtk-doc/html/gfbgraph-0.2/GFBGraphUser.html
/usr/share/gtk-doc/html/gfbgraph-0.2/annotation-glossary.html
/usr/share/gtk-doc/html/gfbgraph-0.2/api-index-full.html
/usr/share/gtk-doc/html/gfbgraph-0.2/ch01.html
/usr/share/gtk-doc/html/gfbgraph-0.2/ch02.html
/usr/share/gtk-doc/html/gfbgraph-0.2/ch03.html
/usr/share/gtk-doc/html/gfbgraph-0.2/gfbgraph-0.2.devhelp2
/usr/share/gtk-doc/html/gfbgraph-0.2/gfbgraph-GFBGraphAuthorizer.html
/usr/share/gtk-doc/html/gfbgraph-0.2/gfbgraph-GFBGraphConnectable.html
/usr/share/gtk-doc/html/gfbgraph-0.2/gfbgraph-gfbgraph-common.html
/usr/share/gtk-doc/html/gfbgraph-0.2/home.png
/usr/share/gtk-doc/html/gfbgraph-0.2/index.html
/usr/share/gtk-doc/html/gfbgraph-0.2/left-insensitive.png
/usr/share/gtk-doc/html/gfbgraph-0.2/left.png
/usr/share/gtk-doc/html/gfbgraph-0.2/object-tree.html
/usr/share/gtk-doc/html/gfbgraph-0.2/right-insensitive.png
/usr/share/gtk-doc/html/gfbgraph-0.2/right.png
/usr/share/gtk-doc/html/gfbgraph-0.2/style.css
/usr/share/gtk-doc/html/gfbgraph-0.2/up-insensitive.png
/usr/share/gtk-doc/html/gfbgraph-0.2/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgfbgraph-0.2.so.0
/usr/lib64/libgfbgraph-0.2.so.0.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gfbgraph/70e5b527a568a6a75b977976e2d392fadf9bd84a
