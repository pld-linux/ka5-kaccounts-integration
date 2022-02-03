%define		kdeappsver	21.12.2
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		kaccounts-integration
Summary:	Kaccounts integration
Name:		ka5-%{kaname}
Version:	21.12.2
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	338bf0ab367f6bc7993820dac4d39026
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kcmutils-devel >= %{kframever}
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

%description -l pl.UTF-8
Zarządzaj kontami internetowymi w środowisku Plazmy.

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
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
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
%attr(755,root,root) %{_libdir}/libkaccounts.so.*.*.*
%dir %{_libdir}/qt5/qml/org/kde/kaccounts
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/kaccounts/libkaccountsdeclarativeplugin.so
%{_libdir}/qt5/qml/org/kde/kaccounts/qmldir
%{_datadir}/kservices5/kcm_kaccounts.desktop
%dir %{_datadir}/kpackage/kcms/kcm_kaccounts
%dir %{_datadir}/kpackage/kcms/kcm_kaccounts/contents
%dir %{_datadir}/kpackage/kcms/kcm_kaccounts/contents/ui
%{_datadir}/kpackage/kcms/kcm_kaccounts/contents/ui/Accounts.qml
%{_datadir}/kpackage/kcms/kcm_kaccounts/contents/ui/AvailableAccounts.qml
%{_datadir}/kpackage/kcms/kcm_kaccounts/metadata.desktop
%{_datadir}/kpackage/kcms/kcm_kaccounts/metadata.json
%ghost %{_libdir}/libkaccounts.so.2
%dir %{_libdir}/qt5/plugins/kaccounts
%dir %{_libdir}/qt5/plugins/kaccounts/daemonplugins
%attr(755,root,root) %{_libdir}/qt5/plugins/kaccounts/daemonplugins/kaccounts_kio_webdav_plugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kcms/kcm_kaccounts.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/kded/kded_accounts.so
%{_datadir}/kpackage/kcms/kcm_kaccounts/contents/ui/AccountDetails.qml
%{_datadir}/kpackage/kcms/kcm_kaccounts/contents/ui/MessageBoxSheet.qml
%{_datadir}/kpackage/kcms/kcm_kaccounts/contents/ui/RemoveAccountDialog.qml
%{_datadir}/kpackage/kcms/kcm_kaccounts/contents/ui/RenameAccountDialog.qml

%files devel
%defattr(644,root,root,755)
%{_includedir}/KAccounts
%{_libdir}/cmake/KAccounts
%{_libdir}/libkaccounts.so
