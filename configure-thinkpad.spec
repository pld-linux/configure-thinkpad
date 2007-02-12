%define		_name	thinkpad
Summary:	GNOME configuration tool for IBM ThinkPad laptops
Summary(pl.UTF-8):   Narzędzie konfiguracyjne GNOME do laptopów IBM ThinkPad
Name:		configure-thinkpad
Version:	0.9
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/tpctl/%{name}-%{version}.tar.gz
# Source0-md5:	b0d6c3dd3a0867248fb6bfc2d41881f5
Patch0:		%{name}-desktop.patch
URL:		http://tpctl.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libgnomeui-devel
BuildRequires:	pkgconfig
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME configuration tool for IBM ThinkPad laptops.

%description -l pl.UTF-8
Narzędzie konfiguracyjne GNOME do laptopów IBM ThinkPad

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln -sf %{name}/gnome-laptop.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
