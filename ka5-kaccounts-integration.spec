%define		kdeappsver	18.12.1
%define		qtver		5.9.0
%define		kaname		kaccounts-integration
Summary:	Kaccounts integration
Name:		ka5-%{kaname}
Version:	18.12.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	1d93ef2d156d21b0638ae91fe7b1aab6
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	libaccounts-glib-devel >= 1.21
BuildRequires:	libaccounts-qt5-devel >= 1.13
BuildRequires:	libsignon-qt5-devel >= 8.55
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Administer web accounts for the sites and services across the Plasma
desktop.

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libkaccounts.so.1
%attr(755,root,root) %{_libdir}/libkaccounts.so.*.*.*
%attr(755,root,root) %{_libdir}/qt5/plugins/kcm_kaccounts.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/kded/accounts.so
%dir %{_libdir}/qt5/qml/org/kde/kaccounts
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/kaccounts/libkaccountsdeclarativeplugin.so
%{_libdir}/qt5/qml/org/kde/kaccounts/qmldir
%{_datadir}/kservices5/kcm_kaccounts.desktop
#%%{_datadir}/kservices5/kded/accounts.desktop

%files devel
%defattr(644,root,root,755)
%{_includedir}/KAccounts
%{_libdir}/cmake/KAccounts
%attr(755,root,root) %{_libdir}/libkaccounts.so
